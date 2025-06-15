import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from utils.load import save_to_gsheet, save_to_csv

class TestLoad(unittest.TestCase):

    @patch("utils.load.set_with_dataframe")
    @patch("utils.load.gspread.authorize")
    @patch("utils.load.Credentials.from_service_account_file")
    def test_save_to_gsheet_success(self, mock_from_service_account_file, mock_authorize, mock_set_with_dataframe):
        df = pd.DataFrame({
            "Title": ["Mocked Shirt"],
            "Price": [50000],
            "Rating": [4.5],
            "Colors": [2],
            "Size": ["M"],
            "Gender": ["Women"]
        })

        # Mock credentials dan worksheet
        mock_creds = MagicMock()
        mock_from_service_account_file.return_value = mock_creds

        mock_sheet = MagicMock()
        mock_client = MagicMock()
        mock_client.open.return_value.sheet1 = mock_sheet
        mock_authorize.return_value = mock_client

        save_to_gsheet(df)

        mock_from_service_account_file.assert_called_once()
        mock_authorize.assert_called_once_with(mock_creds)
        mock_sheet.clear.assert_called_once()
        mock_set_with_dataframe.assert_called_once_with(mock_sheet, df)

    def test_save_to_csv_creates_file(self):
        df = pd.DataFrame({
            "Title": ["Mocked Shirt"],
            "Price": [50000],
            "Rating": [4.5],
            "Colors": [2],
            "Size": ["M"],
            "Gender": ["Women"]
        })

        test_filename = "test_output.csv"
        save_to_csv(df, test_filename)

        # Cek apakah file dibuat
        self.assertTrue(os.path.exists(test_filename))

        # Cek isi file sama
        saved_df = pd.read_csv(test_filename)
        pd.testing.assert_frame_equal(df, saved_df)

        # Hapus file setelah test
        os.remove(test_filename)

if __name__ == '__main__':
    unittest.main()
