import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials

def save_to_csv(df, filename='products.csv'):
    """Menyimpan DataFrame ke file CSV."""
    if df.empty:
        print("Warning: DataFrame kosong. Tidak ada data yang disimpan.")
        return

    try:
        df.to_csv(filename, index=False)
        print(f"✅ Data berhasil disimpan ke '{filename}'")
    except Exception as e:
        print(f"❌ Gagal menyimpan ke CSV: {e}")

def save_to_gsheet(df, json_keyfile='google-sheets-api.json', sheet_name='fashionStudio'):
    """Menyimpan DataFrame ke Google Sheets menggunakan service account."""
    if df.empty:
        print("Warning: DataFrame kosong. Tidak ada data yang dikirim ke Google Sheets.")
        return

    try:
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(json_keyfile, scopes=scopes)
        client = gspread.authorize(creds)

        sheet = client.open(sheet_name).sheet1
        sheet.clear()
        set_with_dataframe(sheet, df)
        print("✅ Data berhasil disimpan ke Google Sheets.")
    except Exception as e:
        print(f"❌ Gagal menyimpan ke Google Sheets: {e}")
