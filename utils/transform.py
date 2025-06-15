import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)

    # Drop duplikat berdasarkan kolom penting
    df.drop_duplicates(subset=["Title", "Price", "Size", "Gender"], inplace=True)
    

    # Filter produk tidak valid
    df = df[df['Title'] != "Unknown Product"]
    df = df[df['Price'].str.startswith("$")]

    # Ubah Price ke float dan konversi ke Rupiah
    df['Price'] = pd.to_numeric(
        df['Price'].str.replace("$", "", regex=False), errors='coerce'
    )
    df = df.dropna(subset=['Price'])
    df['Price'] = df['Price'].apply(lambda x: round(x * 16000, 2))

    # Bersihkan Rating
    def parse_rating(rating_str):
        try:
            return float(str(rating_str).split("/")[0].strip())
        except:
            return None

    df['Rating'] = df['Rating'].apply(parse_rating)
    df = df.dropna(subset=['Rating'])

    # Ambil angka dari kolom Colors
    df['Colors'] = df['Colors'].str.extract(r'(\d+)')
    df['Colors'] = pd.to_numeric(df['Colors'], errors='coerce')
    df = df.dropna(subset=['Colors'])
    df['Colors'] = df['Colors'].astype(int)

    return df
