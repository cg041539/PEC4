import unittest
import pandas as pd
from src.data_processing import breakdown_date, erase_month
from src.agrupar import groupby_state_and_year

class TestAgrupar(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv('./Data/nics-firearm-background-checks.csv').head(10)
        self.df = breakdown_date(self.df)
        self.df = erase_month(self.df)

    def test_groupby_state_and_year(self):
        df_grouped = groupby_state_and_year(self.df)
        print(df_grouped)
        self.assertEqual(df_grouped.loc[0, 'totals'], 92652)  # Ajustamos segun los datos
        self.assertEqual(
            df_grouped[(df_grouped['year'] == 2020) & (df_grouped['state'] == 'Alabama')]['totals'].values[0], 92652)
        self.assertEqual(
            df_grouped[(df_grouped['year'] == 2020) & (df_grouped['state'] == 'Alaska')]['totals'].values[0], 9939)

if __name__ == '__main__':
    unittest.main()

