from utils.extract import scrape_all_pages
from utils.transform import clean_data
from utils.load import save_to_csv, save_to_gsheet

def run_etl():
    print("🚀 Memulai proses ETL...")

    # --- Extract ---
    data = scrape_all_pages()
    print(f"📦 Data berhasil diambil: {len(data)} baris")

    if not data:
        print("❌ Tidak ada data yang berhasil diekstrak. ETL dihentikan.")
        return

    # --- Transform ---
    df_clean = clean_data(data)
    print(f"🧹 Data setelah dibersihkan: {len(df_clean)} baris")

    if df_clean.empty:
        print("❌ DataFrame kosong setelah transformasi. ETL dihentikan.")
        return

    # --- Load ---
    save_to_csv(df_clean, filename="products.csv")
    save_to_gsheet(df_clean)

    print("✅ Proses ETL selesai!")

if __name__ == "__main__":
    run_etl()
