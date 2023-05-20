# simple app to test streamlit

import streamlit as st

st.title("Hello World")  #titre de la page

st.header("A header")
st.subheader("subheader")

st.write('simple test for streamlit')

if st.button("Click"):
    st.write("Horrayyyy")
    st.balloons()

st.sidebar.header("it's a sidebar")  
  
    
#create 2 columns

col1, col2 = st.columns(2)

#les colonnes ne sont visibles qu'apres avoir cliquer sur le bouton du sidebar

if st.sidebar.button("click here"):
    col1.header("Column 1")
    col1.write("this is column 1 ")
    col2.header("Column 2")
    col2.write("this is column 2 ")


#to create 2 columns avc differentes proportions (ici 3/4 la premiere et la seconde 1/4 de la largeur de la page)
# col1, col2 = st.columns([3,1])

#to create a selectbox to the sidebar
option = st.sidebar.selectbox("how would you like to be contacted", ("email","phone", "adress"))

st.write('you selected', option)

#to upload a file 
st.file_uploader('upload your file')
