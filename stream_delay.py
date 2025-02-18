import pickle
import numpy as np
import streamlit as st

# Memuat model yang sudah disimpan
model = pickle.load(open('prediksi_delayFlight.sav', 'rb'))

# Judul web
st.title('PREDIKSI PENUNDAAN PENERBANGAN (DELAY FLIGHT)')

# Form input data
col1, col2 = st.columns(2)

with col1:
    year = st.number_input('Tahun', min_value=2000, max_value=2100, value=2024)
with col2:
    month = st.number_input('Bulan', min_value=1, max_value=12, value=7)
with col1:
    day = st.number_input('Hari', min_value=1, max_value=31, value=15)
with col2:
    day_of_week = st.number_input('Hari dalam Minggu (0=Senin, 1=Selasa, dll)', min_value=0, max_value=6, value=2)
with col1:
    airline = st.text_input('Maskapai (Contoh: AA)')
with col2:
    flight_number = st.number_input('Nomor Penerbangan', min_value=1, max_value=99999, value=1234)
with col1:
    origin_airport = st.text_input('Bandara Asal (Contoh: JFK)')
with col2:
    destination_airport = st.text_input('Bandara Tujuan (Contoh: LAX)')
with col1:
    scheduled_departure = st.number_input('Jadwal Keberangkatan (Contoh: 1000)')
with col2:
    distance = st.number_input('Jarak (Contoh: 300)', min_value=0, value=300)
with col1:
    scheduled_arrival = st.number_input('Jadwal Kedatangan (Contoh: 1500)')

# Kode untuk prediksi
flight_diagnosis = ''

# Membuat tombol prediksi
try:
    inputs = [year, month, day, day_of_week, airline, flight_number, origin_airport, destination_airport, 
              scheduled_departure, distance, scheduled_arrival]

    # Membuat tombol prediksi
    if st.button('Hasil Prediksi Penundaan Penerbangan'):
        flight_prediction = model.predict([inputs])

        if flight_prediction[0] == 1:
            flight_diagnosis = 'Penerbangan Terlambat'
        else:
            flight_diagnosis = 'Penerbangan Tidak Terlambat'

    st.success(flight_diagnosis)

except ValueError:
    st.error('Harap masukkan nilai numerik yang valid untuk semua bidang input.')
