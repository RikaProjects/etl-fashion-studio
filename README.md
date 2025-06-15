# 🧵 Proyek ETL Fashion Studio

**Proyek ETL (Extract, Transform, Load) untuk Data Fashion**  
Proyek ini dibuat untuk mengambil data dari website fashion, membersihkannya, dan menyimpannya dalam format yang siap digunakan untuk analisis lebih lanjut.

## 📌 Deskripsi Proyek

ETL pipeline ini dirancang untuk mengambil data produk fashion dari website:

🔗 [https://fashion-studio.dicoding.dev/](https://fashion-studio.dicoding.dev/)

Prosesnya mencakup tiga tahap utama:

- **Extract (Ekstraksi)**: Mengambil data produk fashion dari website dengan teknik web scraping.
- **Transform (Transformasi)**: Membersihkan dan merapikan data mentah menjadi format yang lebih terstruktur.
- **Load (Pemuatan)**: Menyimpan data hasil transformasi ke dalam file CSV (dan opsional ke Google Sheets atau PostgreSQL).

## 📁 Struktur Proyek

```bash
etl-fashion-studio/
etl-fashion-studio/
│
├── utils/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── test_extract.py
├── test_transform.py
├── test_load.py
│
├── main.py
├── products.csv
├── requirements.txt
├── submission.txt
├── README.md
├── .coverage
└── .gitignore
```
## ⚙️ Teknologi yang Digunakan

- Python
- BeautifulSoup (untuk scraping)
- pandas (untuk manipulasi data)
- gspread + Google API (opsional, untuk Google Sheets)
- PostgreSQL (opsional)

```

## 🔧 Cara Menjalankan

Petunjuk lengkap cara menjalankan proyek ini, termasuk perintah menjalankan skrip ETL dan testing, dapat ditemukan di file:

📄 [`submission.txt`](./submission.txt)

## Hasil Output (Google Sheets)

[🔗 Link Google Sheets hasil ETL](https://docs.google.com/spreadsheets/d/1IEXeOoRdHBoe-YE_stC2hkOJHE2OkOZ50Ps5-eAscC8/edit?usp=sharing)

## Dependensi

Pastikan sudah menginstal dependensi yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## 🧪 Pengujian

Proyek ini dilengkapi dengan unit test yang berada di folder `tests/`. Untuk menjalankan semua test:

```bash
pytest
```

## 🚫 Keamanan & File Rahasia

Semua file rahasia seperti `google-sheets-api.json` sudah ditambahkan ke dalam `.gitignore` dan tidak diikutsertakan ke GitHub.  
Jika ingin menggunakan fitur penyimpanan ke Google Sheets, silakan buat dan atur kredensial pribadi kamu sendiri.

## 📄 Lisensi

Proyek ini bersifat open-source dan ditujukan untuk keperluan pembelajaran.
