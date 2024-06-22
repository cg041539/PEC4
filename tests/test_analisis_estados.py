import unittest
import pandas as pd
from src.analisis_estados import groupby_state, clean_states, merge_datasets, calculate_relative_values, handle_outliers
from src.data_processing import breakdown_date, erase_month


class TestAnalisisEstados(unittest.TestCase):

    def setUp(self):
        # Leer los datos del archivo CSV
        self.df = pd.read_csv('./Data/nics-firearm-background-checks.csv')
        self.pop_df = pd.read_csv('./Data/us-state-populations.csv')

        # Procesar los datos
        self.df = breakdown_date(self.df)
        self.df = erase_month(self.df)

    def test_groupby_state(self):
        df_grouped = groupby_state(self.df)
        self.assertIn('state', df_grouped.columns)
        self.assertIn('permit', df_grouped.columns)

    def test_clean_states(self):
        df_cleaned = clean_states(self.df)
        self.assertNotIn('Guam', df_cleaned['state'].values)
        self.assertNotIn('Puerto Rico', df_cleaned['state'].values)

    def test_merge_datasets(self):
        df_grouped = groupby_state(self.df)
        df_cleaned = clean_states(df_grouped)
        df_merged = merge_datasets(df_cleaned, './Data/us-state-populations.csv')
        self.assertIn('pop_2014', df_merged.columns)

    def test_calculate_relative_values(self):
        df_grouped = groupby_state(self.df)
        df_cleaned = clean_states(df_grouped)
        df_merged = merge_datasets(df_cleaned, './Data/us-state-populations.csv')
        df_relative = calculate_relative_values(df_merged)
        self.assertIn('permit_perc', df_relative.columns)

    def test_handle_outliers(self):
        df_grouped = groupby_state(self.df)
        df_cleaned = clean_states(df_grouped)
        df_merged = merge_datasets(df_cleaned, './Data/us-state-populations.csv')
        df_relative = calculate_relative_values(df_merged)
        df_outliers_handled = handle_outliers(df_relative)
        self.assertAlmostEqual(df_outliers_handled[df_outliers_handled['state'] ==
                                                   'Kentucky']['permit_perc'].values[0], 34.88, delta=0.1)


if __name__ == '__main__':
    unittest.main()
