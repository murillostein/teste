import pandas as pd
import numpy as np
import streamlit as st
#from PIL import Image
import cv2
import easyocr
import tempfile
import streamlit as st
from PIL import Image

def ocr_reader():
    
    st.title('Leitura de caracteres')
    st.subheader('Faça leitura de caracteres através de imagens ou vídeos!')

    # adiciona caixa de seleção à Sidebox
    formato = st.sidebar.selectbox("Escolha o formato", ['Imagem','Vídeo'])

    # carrega modelo ocr
    reader = easyocr.Reader(['en'], gpu=True)

    if formato == 'Vídeo':
            
        video_file = st.file_uploader("Anexe um vídeo",type = ['mp4'])

        i = 0
        if video_file is not None:
            
            # manipulação para deixar em formato legível para opencv
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())

            vid_capture = cv2.VideoCapture(tfile.name)

            with st.spinner("Vídeo em análise"):
                while True:
                    print(i)
                    i += 1

                    conectado, frame = vid_capture.read()
                                        
                    if not conectado:
                        break

                    frame_cp = frame.copy()

                    # aplica modelo ao frame
                    resultados = reader.readtext(frame_cp,paragraph=False,rotation_info=[0,0,0])
                    if resultados != []:
                    #st.write("input frame")
                    #st.image(frame)
                    for (bbox, text, prob) in resultados:

                        print("{:.4f}: {}".format(prob, text))
                        #st.write(text)

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

                        #df_previsoes = pd.DataFrame()
                        #df_previsoes[f'{i}'] = [text]
                        #st.dataframe(df_previsoes)

                        list.append(str(text))

                    
                    #break
                    df_previsoes = pd.DataFrame()
                    df_previsoes[f'frame: {i}'] = list
                    st.dataframe(df_previsoes)

                    st.image(frame_cp)
                    #st.write(text)
                    #print("{:.4f}: {}".format(text))
            #st.write("output frame")
            st.image(frame_cp)
            

    else:
            
        #image uploader
        image = st.file_uploader(label = "Anexe uma imagem",type=['png','jpg','jpeg'])

        if image is not None:

            input_image = Image.open(image) #read image
            st.image(input_image) #display image


            input_img_arr = np.array(input_image)
            frame_cp = input_img_arr.copy()
            with st.spinner("Imagem em análise"):
                resultados = reader.readtext(frame_cp,paragraph=False,rotation_info=[0,0,0])
                result_text = [] #empty list for results
                
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
                
                


                #for text in resultados:
                    result_text.append(text)
                st.image(frame_cp)
                st.write(result_text)
            #st.success("Here you go!")
            # st.balloons()