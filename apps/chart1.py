import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


def app():
    st.title('Grafik')

    st.write('Ini adalah Halaman Grafik dari multi-page app.')

    st.write('Ini adalah Halaman Grafik Data Per Provinsi.')

    # Load dataset
    df_a_prov = pd.read_csv('apps/data.csv')
    total= df_a_prov.jml.sum()
    df_a_prov['persen'] = round(((df_a_prov['jml'] / total) * 100),2)

    # Gambar grafik
    dt100 = df_a_prov.jml >= 100
    up100 = df_a_prov[dt100]
    up100 = up100.sort_values('jml',ascending=False)
    

    fig = plt.figure(figsize=(14, 8))
    ax = fig.subplots()
    up=sns.barplot(y="provinsi",x="jml",data=up100, palette="bright", ax=ax)
    for i, (txt, pct) in enumerate(zip(up100.jml, up100.persen)):
        up.annotate('{} dari {} = {}%'.format(txt, total, pct), 
        (txt, i),
         ha = 'left', va = 'center', 
         xytext = (0, 0),
          textcoords = 'offset pixels', weight='bold', size=14)
    up.set_xlabel("Jumlah", size=14)
    up.set_ylabel("Provinsi      ", size=14, rotation=360)
    up.set_title("Jumlah Data per provinsi diatas 100", size=20)
    plt.yticks(size=14)
    st.pyplot(fig)

    kr100 = df_a_prov.jml < 100
    lbh10 = df_a_prov.jml > 10
    antara = df_a_prov[lbh10 & kr100]
    antara = antara.sort_values('jml',ascending=False)
    
    fig2 = plt.figure(figsize=(14, 14))
    ax2 = fig2.subplots()
    btw=sns.barplot(y="provinsi",x="jml",data=antara, palette="hls", ax=ax2)
    for i, (txt, pct) in enumerate(zip(antara.jml, antara.persen)):
        btw.annotate('{} dari {} = {}%'.format(txt, total, pct),
                    (txt, i),
                   ha = 'left', va = 'center', 
                   xytext = (0, 0), 
                   textcoords = 'offset pixels', weight='bold', size=14)
    btw.set_xlabel("Jumlah", size=14)
    btw.set_ylabel("Provinsi            ", size=14, rotation=360)
    btw.set_title("Jumlah Data per provinsi antara 10 sampai 100", size=20)
    plt.yticks(size=14)
    st.pyplot(fig2)

    dt10 = df_a_prov.jml <= 10
    dw10 = df_a_prov[dt10]
    dw10 = dw10.sort_values('jml',ascending=False)
    
    fig3 = plt.figure(figsize=(14, 20))
    ax3 = fig3.subplots()
    bw=sns.barplot(y="provinsi",x="jml",data=dw10, palette="pastel", ax=ax3)
    for i, (txt, pct) in enumerate(zip(dw10.jml, dw10.persen)):
        bw.annotate('{} dari {} = {}%'.format(txt, total, pct),
                    (txt, i),
                   ha = 'left', va = 'center', 
                   xytext = (0, 0), 
                   textcoords = 'offset pixels', weight='bold', size=14)
    bw.set_xlabel("Jumlah", size=14)
    bw.set_ylabel("Provinsi      ", size=14, rotation=360)
    bw.set_title("Jumlah Data provinsi dibawah 10", size=20)
    plt.yticks(size=14)
    st.pyplot(fig3)
