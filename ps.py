# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 01:12:12 2023

@author: uth2001
"""

import pandas as pd
import numpy as np
import streamlit as st
import warnings
import openpyxl
warnings.filterwarnings('ignore')


st.title('LAC-Pseudo')
st.header('Field Mapping')
input1 = st.file_uploader("Upload input report")
output = st.file_uploader("Upload output file")
if input1 and output is not None:

    df = pd.read_excel(input1, engine='openpyxl')
    df1 = pd.read_excel(output, engine='openpyxl')
    for i in range(df1.shape[0]):
        if pd.isna(df1["GIC"][i]):
            temp = df[df["REFERENCE CODE"] ==
                      df1["REFERENCE CODE"][i]].index[0]
            for j in df1.columns[29:]:
                if pd.isna(df1[j][i]):
                    df1[j][i] = df[j][temp]
    df1['Pseudo Code'] = df1['Pseudo Code'].astype('Int64')
    df1['GIC'] = df1['GIC'].astype('Int64')
    test = df1.astype(str)
    st.dataframe(test)

    def convert_df(dff):
        return dff.to_csv().encode('utf-8')
    csv = convert_df(test)
    st.download_button(
        label="Download file",
        data=csv,
        file_name='output.csv',
        mime='text/csv',)
