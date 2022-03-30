import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


def app():
    st.title('Grafik Semua')

    st.write('Ini adalah Halaman Grafik dari multi-page app.')

    st.write('Ini adalah Halaman Grafik Data Per Provinsi.')

    # Load dataset
    df_a_prov = pd.read_csv('data.csv')
    total= df_a_prov.jml.sum()
    df_a_prov['persen'] = round(((df_a_prov['jml'] / total) * 100),2)

    # Gambar grafik
    df_a_prov = df_a_prov.sort_values('jml',ascending=False)
    

    fig4 = plt.figure(figsize=(16, 75))
    ax4 = fig4.subplots()
    smua=sns.barplot(y="provinsi",x="jml",data=df_a_prov, ax=ax4)
    for i, (txt, pct) in enumerate(zip(df_a_prov.jml, df_a_prov.persen)):
        smua.annotate('{} dari {} = {}%'.format(txt, total, pct),
                    (txt, i),
                   ha = 'left', va = 'center', 
                   xytext = (0, 0), 
                   textcoords = 'offset pixels', weight='bold', size=14)
    smua.set_xlabel("Jumlah", size=14)
    smua.set_ylabel("Provinsi      ", size=14, rotation=360)
    smua.set_title("Jumlah Data Per Provinsi", size=20)
    plt.yticks(size=14)
    st.pyplot(fig4)
