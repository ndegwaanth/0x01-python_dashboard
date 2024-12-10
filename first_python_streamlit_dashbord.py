import pandas as pd
import streamlit as st
import numpy as np


df = pd.read_excel('data/Telco_customer_churn.xlsx')
print(df.head(5))