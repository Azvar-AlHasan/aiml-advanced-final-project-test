import streamlit as st
import pandas as pd
import joblib
import datetime

# --- CUSTOM FUNCTIONS ---
# Karena model di-train dengan function kustom ini, kita wajib mendefinisikannya
# agar model.joblib bisa di-load dengan sukses.
def bin_time_of_day(hour):
    if 6 <= hour < 12:
        return 'morning'
    elif 12 <= hour < 17:
        return 'afternoon'
    elif 17 <= hour < 21:
        return 'evening'
    else:
        return 'night'

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    return joblib.load('model.joblib')

model = load_model()

# --- STREAMLIT UI ---
st.set_page_config(page_title="Taxi Fare Prediction", page_icon="🚕", layout="centered")

st.title("🚕 Taxi Fare Prediction App")
st.write("Aplikasi ini memprediksi tarif taksi berdasarkan waktu, lokasi penjemputan, lokasi tujuan, dan jarak.")

# Input Form
with st.form("prediction_form"):
    st.header("Masukkan Detail Perjalanan")
    
    col1, col2 = st.columns(2)
    with col1:
        pickup_date = st.date_input("Tanggal Penjemputan", datetime.date.today())
        pickup_time = st.time_input("Waktu Penjemputan", datetime.datetime.now().time())
        pickup_location_id = st.number_input("Pickup Location ID", min_value=1, max_value=265, value=132)
        
    with col2:
        trip_distance = st.number_input("Estimasi Jarak (miles)", min_value=0.0, max_value=100.0, value=2.5, step=0.1)
        dropoff_location_id = st.number_input("Dropoff Location ID", min_value=1, max_value=265, value=138)
    
    submit_button = st.form_submit_button(label="🚕 Hitung Estimasi Harga")

if submit_button:
    # 1. Ekstrak fitur waktu dari input pengguna
    day_of_week = pickup_date.weekday() # 0 = Monday, 6 = Sunday
    hour_of_day = pickup_time.hour
    
    # 2. Siapkan DataFrame untuk input model
    # Sesuaikan nama kolom dengan yang digunakan saat training di notebook!
    # Fitur yang digunakan oleh model: ['trip_distance', 'hour_of_day', 'pickup_location_id', 'dropoff_location_id', 'day_of_week']
    input_data = pd.DataFrame([{
        'trip_distance': trip_distance,
        'hour_of_day': hour_of_day,
        'pickup_location_id': pickup_location_id,
        'dropoff_location_id': dropoff_location_id,
        'day_of_week': day_of_week
    }])
    
    # 3. Prediksi menggunakan model
    try:
        prediction = model.predict(input_data)
        fare_amount = prediction[0]
        
        st.success("Berhasil memprediksi harga!")
        st.metric(label="Estimasi Tarif Taksi", value=f"${fare_amount:.2f}")
        
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memprediksi: {e}")
        st.info("Pastikan fitur-fitur di atas sesuai dengan fitur yang Anda gunakan saat men-train model di Google Colab. Buka app.py dan sesuaikan bagian `input_data`.")

st.markdown("---")
st.caption("Dibuat untuk Final Project - Weekly Class AI/ML Advanced GDGOC")
