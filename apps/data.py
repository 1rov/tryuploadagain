import streamlit as st
import numpy as np
import pandas as pd
# from sklearn import datasets

def app():
    st.title('Data')

    st.write("Ini adalah halama data dari multi-page app.")

    st.write("Halaman ini menampilkan Data Provinsi")

    df_a_prov = pd.read_csv('data.csv')
    total= df_a_prov.jml.sum()
    df_a_prov['persen'] = round(((df_a_prov['jml'] / total) * 100),2)

    st.write(df_a_prov)
