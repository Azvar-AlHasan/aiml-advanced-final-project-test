# Taxi Fare Prediction 🚕

Repositori ini berisi Final Project untuk **Weekly Class AI/ML Advanced** dari GDGOC. Proyek ini merupakan solusi Machine Learning end-to-end untuk memprediksi tarif taksi berdasarkan beberapa fitur perjalanan seperti waktu penjemputan, lokasi, dan jumlah penumpang.

## Struktur Direktori

```text
AIML-Final-Project/
├── assets/                  # Untuk menyimpan gambar/logo
├── data/                    # Untuk menyimpan dataset .csv, .xlsx
├── app.py                   # File utama aplikasi Streamlit
├── model.joblib             # Model Machine Learning yang sudah dilatih
├── notebook.ipynb           # Notebook eksperimen (Eksplorasi Data & Training Model)
├── requirements.txt         # Daftar dependency package Python
└── README.md                # Dokumentasi proyek ini
```

## Deskripsi Kasus
Dalam industri ride-hailing dan taksi modern, transparansi harga adalah kunci untuk mendapatkan kepercayaan pelanggan. Sebagai seorang Machine Learning Engineer, kami ditugaskan untuk membangun fitur **"Upfront Pricing" (Estimasi Harga di Muka)**. Aplikasi web cerdas berbasis model Regresi ini mampu memprediksi tarif taksi sebelum pelanggan menekan tombol "Pesan Sekarang".

## Cara Menjalankan Aplikasi Secara Lokal

1. **Clone repository ini**
   ```bash
   git clone https://github.com/Azvar-AlHasan/aiml-advanced-final-project-test.git
   cd AIML-Final-Project
   ```

2. **Buat Virtual Environment (Opsional namun disarankan)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi Streamlit**
   ```bash
   streamlit run app.py
   ```
