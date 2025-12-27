import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title="Customer Churn Analysis", layout="wide")
st.title("Customer Churn Analysis")

# Load data
df = pd.read_csv("telco.csv")

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Churn distribution
st.subheader("Churn Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x="Churn Label", data=df, ax=ax1)
st.pyplot(fig1)

# Churn vs Contract Type
st.subheader("Churn vs Contract Type")
fig2, ax2 = plt.subplots()
sns.countplot(x="Contract", hue="Churn Label", data=df, ax=ax2)
st.pyplot(fig2)

# Business insights
st.subheader("Business Insights")
st.write("""
- Month-to-month customers have a higher churn rate  
- Long-term contracts help reduce churn  
- Contract type strongly impacts customer retention  
""")
