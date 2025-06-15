import unittest
from bs4 import BeautifulSoup
from unittest.mock import patch, Mock
from utils.extract import extract_products_from_page, scrape_all_pages

class TestExtract(unittest.TestCase):

    def test_extract_single_product(self):
        html = '''
        <div class="product-details">
            <h3 class="product-title">Nice Shirt</h3>
            <div class="price-container"><span class="price">$50.00</span></div>
            <p>Rating: ⭐ 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: L</p>
            <p>Gender: Men</p>
        </div>
        '''
        soup = BeautifulSoup(html, "html.parser")
        products = extract_products_from_page(soup)

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["Title"], "Nice Shirt")
        self.assertEqual(products[0]["Price"], "$50.00")
        self.assertEqual(products[0]["Rating"], "4.5")
        self.assertEqual(products[0]["Colors"], "3")
        self.assertEqual(products[0]["Size"], "L")
        self.assertEqual(products[0]["Gender"], "Men")
        self.assertIn("timestamp", products[0])

    @patch("utils.extract.requests.get")
    def test_scrape_all_pages_mocked(self, mock_get):
        # Dummy HTML untuk 1 produk
        html = '''
        <div class="product-details">
            <h3 class="product-title">Mocked Shirt</h3>
            <div class="price-container"><span class="price">$40.00</span></div>
            <p>Rating: ⭐ 4.0 / 5</p>
            <p>2 Colors</p>
            <p>Size: M</p>
            <p>Gender: Women</p>
        </div>
        '''

        # Setup mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html
        mock_get.return_value = mock_response

        # Jalankan fungsi
        products = scrape_all_pages()

        # Assertions
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 0)
        self.assertEqual(products[0]["Title"], "Mocked Shirt")
        self.assertEqual(products[0]["Price"], "$40.00")
        self.assertEqual(products[0]["Rating"], "4.0")
        self.assertEqual(products[0]["Colors"], "2")
        self.assertEqual(products[0]["Size"], "M")
        self.assertEqual(products[0]["Gender"], "Women")

if __name__ == '__main__':
    unittest.main()
