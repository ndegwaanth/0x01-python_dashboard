import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Cusomer churn Dashboard', page_icon='\U0001F4CA' , layout='wide')

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
    st.subheader(f'US: $ {average_charges:.2f}')

with second:
    st.subheader('Gender Count')
    st.subheader(f'US: {gender_count}')

with third:
    st.subheader('Minimun Monthly Charges')
    st.subheader(f'US: $ {int(monthly_charges)}')


st.divider()

average_charges_per_city = df_select.groupby(by=['Internet-Service'])[['Total Charges']].sum().sort_values(by='Total Charges')

fig_average_price = px.bar(
    average_charges_per_city,
    x='Total Charges',
    y=average_charges_per_city.index,
    title='<b>Average Price in accordance with Gender<b>',
    orientation='h',
    color_discrete_sequence=['#0083B8'] * len(average_charges_per_city),
    template='plotly_white',
)

fig_average_price.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False))
)

monthly_charges_per_city = df_select.groupby(by=['Payment-Method'])[['Monthly Charges']].sum().sort_values(by='Monthly Charges')

fig_monthly_price = px.bar(
    monthly_charges_per_city,
    x='Monthly Charges',
    y=monthly_charges_per_city.index,
    title='<b>Monthly Price in accordance with Gender<b>',
    orientation='h',
    color_discrete_sequence=['#0083B8'] * len(monthly_charges_per_city),
    template='plotly_white',
)

fig_monthly_price.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False))
)

left, right = st.columns(2)
left.plotly_chart(fig_average_price, use_container_width=True)
right.plotly_chart(fig_monthly_price, use_container_width=True)

st.divider()

# adding more KPIS
max_price = df_select['Monthly Charges'].max()
min_price = df_select['Monthly Charges'].min()

left_col, mid_col, right_col = st.columns(3)

with left_col:
    min_price = df_select['Monthly Charges'].min()
    left_col.metric(
        label='Minimum Average Price',
        value=f'$ {int(min_price)}'
    )

with mid_col:
    mid_price = df_select['Monthly Charges'].median()
    mid_col.metric(
        label='Median Average Price',
        value=f'$ {int(min_price)}'
    )

with right_col:
    right_price = df_select['Monthly Charges'].max()
    right_col.metric(
        label='Maximum Average Price',
        value=f'$ {int(min_price)}'
    )


mid_col.plotly_chart(fig_monthly_price, use_container_width=False)


# monthly price histogram
monthly_charges_fig = px.histogram(
    df_select,
    x='Monthly Charges',
    title='Monthly Charges Distribution'
)

monthly_charges_fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    bargap=0.1,
    xaxis=dict(showgrid=False)
)

right_col.plotly_chart(monthly_charges_fig, use_container_width=False)


st.dataframe(df_select)
