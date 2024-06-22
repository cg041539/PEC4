import unittest
import pandas as pd
from src.data_cleaning import read_csv, clean_csv, rename_col, clean


class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        # Leer un subconjunto del archivo CSV original para los tests
        self.df = pd.read_csv('./Data/nics-firearm-background-checks.csv').head(10)

    def test_clean_csv(self):
        cleaned_df = clean_csv(self.df)
        self.assertEqual(list(cleaned_df.columns), ['month', 'state', 'permit', 'handgun', 'long_gun'])

    def test_rename_col(self):
        renamed_df = rename_col(self.df)
        self.assertIn('longgun', renamed_df.columns)
        self.assertNotIn('long_gun', renamed_df.columns)


if __name__ == '__main__':
    unittest.main()
