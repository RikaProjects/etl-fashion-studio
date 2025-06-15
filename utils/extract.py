import requests
from bs4 import BeautifulSoup
from datetime import datetime

def extract_products_from_page(soup):
    products = []
    product_cards = soup.find_all("div", class_="product-details")

    for card in product_cards:
        try:
            title_tag = card.find("h3", class_="product-title")
            price_tag = card.find("span", class_="price")

            title = title_tag.get_text(strip=True) if title_tag else ""
            price = price_tag.get_text(strip=True) if price_tag else ""

            # Skip jika tidak ada judul dan harga
            if not title and not price:
                print("Skipping product: missing both title and price")
                continue

            rating, colors, size, gender = "", "", "", ""
            for p in card.find_all("p"):
                text = p.get_text(strip=True)
                if "Rating" in text:
                    rating = text.replace("Rating: ⭐", "").replace("/ 5", "").strip()
                elif "Colors" in text:
                    colors = text.replace(" Colors", "").strip()
                elif "Size:" in text:
                    size = text.replace("Size: ", "").strip()
                elif "Gender:" in text:
                    gender = text.replace("Gender: ", "").strip()

            products.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Colors": colors,
                "Size": size,
                "Gender": gender,
                "timestamp": datetime.now().isoformat()
            })
        except Exception as e:
            print(f"Error parsing product: {e}")
    return products


def scrape_all_pages():
    all_products = []

    for page in range(1, 51):
        print(f"Scraping page {page}...")
        try:
            url = "https://fashion-studio.dicoding.dev/" if page == 1 else f"https://fashion-studio.dicoding.dev/page{page}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            products = extract_products_from_page(soup)

            all_products.extend(products)  # tanpa dedup
        except Exception as e:
            print(f"Error scraping page {page}: {e}")

    print(f"📦 Total data dikumpulkan: {len(all_products)} produk (termasuk duplikat)")
    return all_products

