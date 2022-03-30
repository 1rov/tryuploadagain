import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import altair as alt


def app():
    st.title('Grafik Interaktif')

    st.write('Ini adalah Halaman Grafik dari multi-page app.')

    st.write('Ini adalah Halaman Grafik Data Per Provinsi.')

    # Load dataset
    df_a_prov = pd.read_csv('data.csv')
    total= df_a_prov.jml.sum()
    df_a_prov['persen'] = round(((df_a_prov['jml'] / total) * 100),2)

    # Gambar grafik
    cbgalt = alt.Chart(df_a_prov).mark_bar(tooltip=True).encode(
            x=alt.X('jml', title='Jumlah'),
            y=alt.Y(
                'provinsi',
                sort=alt.EncodingSortField(field="jml", order="descending"),
                title="",
            ),
            color = alt.Color('provinsi', legend=None),
            tooltip=[
                alt.Tooltip("provinsi", title="Provinsi"),
                alt.Tooltip("jml", title="Jumlah"),
                alt.Tooltip("persen", title="Dari total {} =%".format(total))
            ]
            )
    st.altair_chart(cbgalt, use_container_width=True)
