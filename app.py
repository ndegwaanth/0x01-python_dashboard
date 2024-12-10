import pandas as pd
import numpy as np
import streamlit as st


@st.cache_data
def get_data():
    df = pd.read_excel('data/Telco_customer_churn.xlsx', index_col=0)
    return df

df = get_data()
df = df.rename(columns={'Payment Method': 'Payment-Method', 'Senior Citizen': 'Senior-Citizen', 'Internet Service': 'Internet-Service'})

# sidebars
st.sidebar.header("Please Filter Here")


gender = st.sidebar.radio(
    "select the Gender",
    options= df['Gender'].unique()
)

payment_method = st.sidebar.radio(
    "Select the payment Method",
    options=df['Payment-Method'].unique()
 )

senior_citizen = st.sidebar.radio(
    "Select whether your senior citizen or not",
    options=df['Senior-Citizen'].unique()
)

internet_service = st.sidebar.multiselect(
    "Select the Internet Service",
    options=df['Internet-Service'].unique(),
    default=df['Internet-Service'].unique()
)

## main page 
df_select = df.query(
    "`Internet-Service` in @internet_service and Gender == @gender and `Payment-Method` == @payment_method and `Senior-Citizen` == @senior_citizen"
)

if df_select.empty:
    st.warning('No data available based on the current filter')
    st.stop()


st.title("\U0001F4CA Customer Analysis Dashboard")
st.markdown('##') 


# Ensuring the 'Total Charges' column is numeric
df_select['Total Charges'] = pd.to_numeric(df_select['Total Charges'], errors='coerce')
df_select['Monthly Charges'] = pd.to_numeric(df_select['Monthly Charges'], errors='coerce')

# Droping rows with missing values
df_select = df_select.dropna(subset=['Total Charges', 'Monthly Charges'])

# KPIs calculations
average_charges = df_select['Total Charges'].mean()
gender_count = df_select.shape[0]
monthly_charges = df_select['Monthly Charges'].min()

first, second, third = st.columns(3)

with first:
    st.subheader('Average Charges')
    st.subheader(f'US: {average_charges:.2f}')

with second:
    st.subheader('Gender Count')
    st.subheader(f'US: {gender_count}')

with third:
    st.subheader('Monthly Charges')
    st.subheader(f'US: {int(monthly_charges)}')


st.dataframe(df_select)