import streamlit as st
from multiapp import MultiApp
from apps import home, data, chart1, chart2, chart3 #model # import your app modules here
import pandas as pd
import numpy as np

app = MultiApp()
st.set_page_config(layout="centered", page_title="Aplikasi Data Provinsi")
st.markdown("""
# Multi-Page App

Ini adalah halaman multi pageaps Provinsi

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Grafik", chart1.app)
app.add_app("Grafik Semua", chart2.app)
app.add_app("Grafik Interaktif", chart3.app)
# The main app
app.run()
