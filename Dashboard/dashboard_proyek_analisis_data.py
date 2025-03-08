import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    
    # Data preprocessing
    day_df.drop(columns=["instant", "casual", "registered"], inplace=True)
    hour_df.drop(columns=["instant", "casual", "registered"], inplace=True)
    
    return day_df, hour_df

day_df, hour_df = load_data()

st.title("Dashboard Analisis Peminjaman Sepeda")

# Korelasi variabel numerik dengan peminjaman
st.subheader("Korelasi Variabel terhadap Jumlah Peminjaman")
correlation = day_df.select_dtypes(include=['number']).corr()["cnt"].sort_values()
st.bar_chart(correlation.drop("cnt"))

# Visualisasi peminjaman berdasarkan musim
st.subheader("Distribusi Peminjaman Berdasarkan Musim")
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_mapping)
avg_rent_season = day_df.groupby("season_label")["cnt"].mean()
st.bar_chart(avg_rent_season)

# Peminjaman sepeda berdasarkan jam
st.subheader("Rata-rata Peminjaman Sepeda per Jam dalam Sehari")
avg_rent_hour = hour_df.groupby("hr")["cnt"].mean()
st.bar_chart(avg_rent_hour)

# Peminjaman sepeda bulanan
st.subheader("Tren Peminjaman Sepeda Bulanan")
day_df['mnth'] = pd.to_datetime(day_df['mnth'], format='%m').dt.month
total_rent_month = day_df.groupby("mnth")["cnt"].sum()
st.line_chart(total_rent_month)

# Peminjaman di hari kerja vs akhir pekan
st.subheader("Perbandingan Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
day_df["workingday_label"] = day_df["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})
avg_rent_workingday = day_df.groupby("workingday_label")["cnt"].mean()
st.bar_chart(avg_rent_workingday)

st.write("Copyright R 2025")
