import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


def get_data(url:str,):
    pass 

def make_plt():
    pass

x = np.linspace(-3*np.pi, 3*np.pi, 555)
y = np.sin(x)

trig = plt.figure() 
seno = trig.add_subplot(1,1,1)
seno.plot(x,y)
lbl = 'f(x) = seno(x)'
    





def main():
    with Image.open('img/Everest.jpg') as everest:
        st.write( """
        <style>
            .main 
                {
                background: linear-gradient(red, yellow, blue);
                }
        </style>
        """, unsafe_allow_html=True)
    st.pyplot(trig)
    l = st.latex(lbl)

    




if __name__ == '__main__':
    main()