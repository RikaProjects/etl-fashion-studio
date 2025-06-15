import unittest
import pandas as pd
from utils.transform import clean_data

class TestTransform(unittest.TestCase):

    def test_clean_data_valid(self):
        raw_data = [
            {
                "Title": "Cool T-Shirt",
                "Price": "$25.00",
                "Rating": "4.8",
                "Colors": "3 Colors",
                "Size": "L",
                "Gender": "Men",
                "timestamp": "2025-06-08T10:00:00"
            },
            {
                "Title": "Unknown Product",
                "Price": "$15.00",
                "Rating": "Invalid Rating",
                "Colors": "Colors",
                "Size": "",
                "Gender": "",
                "timestamp": "2025-06-08T10:00:00"
            }
        ]

        cleaned_df = clean_data(raw_data)

        # Hanya 1 data valid yang lolos
        self.assertEqual(len(cleaned_df), 1)
        self.assertEqual(cleaned_df.iloc[0]["Title"], "Cool T-Shirt")
        self.assertEqual(cleaned_df.iloc[0]["Price"], 25.00 * 16000)
        self.assertIsInstance(cleaned_df.iloc[0]["Rating"], float)
        self.assertEqual(cleaned_df.iloc[0]["Colors"], 3)
        self.assertIsInstance(cleaned_df.iloc[0]["Size"], str)
        self.assertIsInstance(cleaned_df.iloc[0]["Gender"], str)

if __name__ == '__main__':
    unittest.main()
