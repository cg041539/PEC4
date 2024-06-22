import unittest
import pandas as pd
from src.data_processing import breakdown_date, erase_month


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv('./Data/nics-firearm-background-checks.csv').head(10)

    def test_breakdown_date(self):
        df_broken_down = breakdown_date(self.df)
        self.assertIn('year', df_broken_down.columns)
        self.assertIn('month', df_broken_down.columns)
        self.assertEqual(df_broken_down.loc[0, 'year'], 2020)  # Ajustamos segun los datos
        self.assertEqual(df_broken_down.loc[0, 'month'], 3)  # Ajustamos segun los datos

    def test_erase_month(self):
        df_erased = erase_month(self.df)
        self.assertNotIn('month', df_erased.columns)


if __name__ == '__main__':
    unittest.main()
