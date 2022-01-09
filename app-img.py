import numpy as np
import streamlit as st
from PIL import Image
import cv2
import easyocr
import tempfile

@st.cache
def load_model(): 
    reader = easyocr.Reader(['en'],model_storage_directory='.')
    return reader 

# reader = load_model()

st.title('Identificação de Códigos')

st.write('Aplicação para detecção e leitura de códigos utilizando OCR.')


formato = st.sidebar.selectbox("Escolha o formato", ['video','imagem'])


if formato == video:
        
    video_file = st.file_uploader("Anexe um vídeo",type = ['mp4'])


    #if st.button('Gerar vídeo'):



    # configurando video de saida
    # output_video = cv2.VideoWriter('st_test_00.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 15, frame_size)

    i = 0

    st_empty = st.empty()


    if video_file is not None:
        reader = easyocr.Reader(['en'], gpu=True)
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        # st.write("Deu boa com tfile")
        vid_capture = cv2.VideoCapture(tfile.name)

        #video_bytes = video_file.read()

        #st.video(video_bytes)

        frame_width = int(vid_capture.get(3))
        frame_height = int(vid_capture.get(4))
        frame_size = (frame_width, frame_height)
        while True:
            print(i)
            
            i += 1

            conectado, frame = vid_capture.read()

            # st.write("deu boa com vid_capture.read")

            # input_image = Image.open(frame)
            
            frame_cp = frame.copy()

            #cv2_imshow(frame)
            
            if not conectado:
                break
            # st.write("nao breakou")
            # image = Image.open(frame)
            resultados = reader.readtext(frame_cp,paragraph=False,rotation_info=[0,0,0])
            
            # st.write("deu boa com em ler resultados")
            
            if resultados != []:
                #st.write("input frame")
                st.image(frame)
                for (bbox, text, prob) in resultados:

                    print("{:.4f}: {}".format(prob, text))

                    # coordenadas da bounding box do OCR
                    (tl, tr, br, bl) = bbox
                    tl = (int(tl[0]), int(tl[1]))
                    tr = (int(tr[0]), int(tr[1]))
                    br = (int(br[0]), int(br[1]))
                    bl = (int(bl[0]), int(bl[1]))

                    # cleanup the txt and draw the box surrounding the text along
                    # with the OCR'd text itself
                    #text = cleanup_text(text)
                    cv2.rectangle(frame_cp, tl, br, (0, 255, 0), 2)
                    #st.write('fez retangulo')
                    cv2.putText(frame_cp, text, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    # 
                    
                    #st.write('fez texto')
                    # cv2_imshow(frame)
                    result_text = [] #empty list for results


                    for text in result:
                        result_text.append(text[1])

                    st.write(result_text)
                    
                #df_previsoes = df_previsoes.append(df_texts)
                
                break
        #st.write("output frame")
        st_empty.image(frame_cp)

else:
        
    #image uploader
    image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

    if image is not None:

        input_image = Image.open(image) #read image
        st.image(input_image) #display image
        st.write('deu boa PIL')
        with st.spinner("🤖 AI is at Work! "):
            
            
            result = reader.readtext(np.array(input_image))
            st.write('deu boa lendo')
            result_text = [] #empty list for results


            for text in result:
                result_text.append(text[1])

            st.write(result_text)
        #st.success("Here you go!")
        st.balloons()
    else:
        st.write("Upload an Image")