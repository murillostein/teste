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

reader = load_model()

st.title('Identificação de Códigos')

st.write('Aplicação para detecção e leitura de códigos utilizando OCR.')


img = st.file_uploader("Anexe uma imagem")

st_empty = st.empty()
st.write("deu boa com fileupload")
if img is not None:    

    input_image = Image.open(img)
    st.write("deu boa com PIL")
    # image = Image.open(frame)
    resultados = reader.readtext(np.array(input_image))
    
    st.write("deu boa com em ler resultados")
    st.write(resultados)
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
        cv2.rectangle(img, tl, br, (0, 255, 0), 2)
        st.write('fez retangulo')
        cv2.putText(img, text, (tl[0], tl[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        # 
        
        st.write('fez texto')
        # cv2_imshow(frame)
        
    #df_previsoes = df_previsoes.append(df_texts)

    st_empty.image(img)

    #output_video.write(frame)

#st_video.video(output_video)