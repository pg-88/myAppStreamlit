import streamlit as st
from PIL import Image 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

st.write("hello world!")

st.title('Titolo')

st.header('Header')

st.subheader('')

st.write('Streamlit **non** è fatto per il deployment di web app, però permette di creare interfacce semplici per capire se il codice python per il backend fa quello che deve fare.')
st.write('non si può usare per il frontend *serio* perchè è lento ed è moolto limitato.')

st.code('streamlit run myApp.py')

st.latex('\sigma_{c} = \\frac {N} {A}')#occhio allo slash indietro!!!

with Image.open('img/latexquickreference.jpeg') as lat_cs:
    st.image(lat_cs)


st.markdown('# ma la vera figata è che possiamo metterci i grafici :heart_eyes:')

df = pd.DataFrame(data=np.random.randint(1, 501, (6,13)))

st.dataframe(df)
y = df[0].tolist()
x = df.index.tolist()
st.dataframe(y)
figure = plt.plot(x, y)
st.area_chart(df)

