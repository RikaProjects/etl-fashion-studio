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
│
├── extract.py         # Modul untuk mengambil data dari website
├── transform.py       # Modul untuk membersihkan dan memformat data
├── load.py            # Modul untuk menyimpan data
├── main.py            # Alur utama ETL
├── .gitignore         # File untuk mengabaikan file rahasia atau tidak perlu
├── requirements.txt   # Daftar dependensi Python
└── tests/             # Folder untuk unit test
```

## ⚙️ Teknologi yang Digunakan

- Python
- BeautifulSoup (untuk scraping)
- pandas (untuk manipulasi data)
- gspread + Google API (opsional, untuk Google Sheets)
- PostgreSQL (opsional)

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
