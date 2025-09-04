import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("StressLevelDataset.csv")

# Sidebar filters
st.sidebar.header("Filters")

study_load = st.sidebar.multiselect(
    "Study Load", options=df["study_load"].unique(), default=df["study_load"].unique()
)

sleep_quality = st.sidebar.multiselect(
    "Sleep Quality", options=df["sleep_quality"].unique(), default=df["sleep_quality"].unique()
)

bullying = st.sidebar.multiselect(
    "Bullying", options=df["bullying"].unique(), default=df["bullying"].unique()
)

# Filtered dataset
df_filtered = df[
    (df["study_load"].isin(study_load)) &
    (df["sleep_quality"].isin(sleep_quality)) &
    (df["bullying"].isin(bullying))
]

# Main dashboard
st.title("📊 Stress Level Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Avg Anxiety", round(df_filtered["anxiety_level"].mean(), 2))
col2.metric("Avg Depression", round(df_filtered["depression"].mean(), 2))
col3.metric("Avg Sleep Quality", round(df_filtered["sleep_quality"].mean(), 2))

# Chart 1: Stress level by study load
st.subheader("Stress Level by Study Load")
fig1, ax1 = plt.subplots()
sns.barplot(x="study_load", y="stress_level", data=df_filtered, ax=ax1)
st.pyplot(fig1)

# Chart 2: Anxiety vs Depression
st.subheader("Anxiety vs Depression")
fig2, ax2 = plt.subplots()
sns.scatterplot(x="anxiety_level", y="depression", hue="stress_level", data=df_filtered, ax=ax2)
st.pyplot(fig2)

# Chart 3: Correlation heatmap
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.heatmap(df_filtered.corr(), annot=False, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# Data table
st.subheader("Filtered Dataset Preview")
st.dataframe(df_filtered.head(20))
