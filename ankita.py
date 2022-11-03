import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)



# Web App Title
st.markdown('''
# EDA on covid 19 CountryWise Data 
This is the **EDA report** created in Streamlit using the **pandas-profiling** library.
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/Ankitakanse/AnkitaKanse-Python-project/main/covid%2019%20CountryWise.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to generate EDA report on covid 19 CountryWise data'):
        # Example data
        @st.cache
        def load_data():
            a = pd.read_csv('https://raw.githubusercontent.com/Ankitakanse/AnkitaKanse-Python-project/main/covid%2019%20CountryWise.csv')
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
