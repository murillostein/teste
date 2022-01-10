import streamlit as st
from PIL import Image

import warnings
warnings.filterwarnings('ignore')


import style as style
import home as home
import ocr_reader as ocr
import sobre_bix as sobre


# ----------------------------------SIDEBAR -------------------------------------------------------------
def main():

    #style.set_background('images/bg03.jpg')

    st.sidebar.header("Leitor de caracteres")
    n_sprites = st.sidebar.radio(
        "Escolha uma opção", options=["Home","Leitura de caracteres","Sobre a Bix-tecnologia"], index=0
    )

    #style.spaces_sidebar(15)
    st.sidebar.write('https://www.bixtecnologia.com/')
    #image = Image.open('images/logo_sidebar_sem_fundo.png')
    # st.sidebar.image(image, use_column_width=True)

    #st.image(image, use_column_width=True)  
    
# ------------------------------ INÍCIO ANÁLISE TÉCNICA E FUNDAMENTALISTA ----------------------------             

    if n_sprites == "Home":

        home.home()

    if n_sprites == "Leitura de caracteres":

        ocr.ocr_reader()

    if n_sprites == "Sobre a Bix-tecnologia":

        sobre.sobre()        


 
        
if __name__ == '__main__':
    main()