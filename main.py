import argparse
from src.data_cleaning import read_csv, clean_csv, rename_col, clean
from src.data_processing import breakdown_date, erase_month
from src.agrupar import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
from src.analisis_temporal import time_evolution
from src.analisis_estados import groupby_state, clean_states, merge_datasets, calculate_relative_values, handle_outliers
from src.mapas import generate_and_save_maps


def main():
    parser = argparse.ArgumentParser(
        description="Ejecutar funciones especificas del proyecto PEC4"
    )
    parser.add_argument(
        '--module',
        type=str,
        choices=['data_cleaning', 'data_processing', 'agrupar', 'analisis_temporal',
                 'analisis_estados', 'generate_and_save_maps'],
        help="El módulo a ejecutar"
    )
    parser.add_argument(
        '--function',
        type=str,
        choices=[
            'read_csv', 'clean_csv', 'rename_col',
            'breakdown_date', 'erase_month',
            'groupby_state_and_year', 'print_biggest_handguns', 'print_biggest_longguns',
            'time_evolution',
            'groupby_state', 'clean_states', 'merge_datasets', 'calculate_relative_values', 'handle_outliers'
        ],
        help="La función a ejecutar dentro del módulo"
    )
    parser.add_argument(
        '--file_path',
        type=str,
        default='./Data/nics-firearm-background-checks.csv',
        help="La ruta o URL del archivo CSV"
    )

    args = parser.parse_args()

    df = None

    if args.module == 'data_cleaning':
        if args.function == 'read_csv':
            read_csv(args.file_path)
        elif args.function == 'clean_csv':
            df = read_csv(args.file_path)
            df_cleaned = clean_csv(df)
            print(df_cleaned.head())
        elif args.function == 'rename_col':
            df = read_csv(args.file_path)
            df_renamed = rename_col(df)
            print(df_renamed.head())
        else:
            df = clean(args.file_path)
            print(df.head())

    elif args.module == 'data_processing':
        if df is None:
            df = read_csv(args.file_path)  # Lee el CSV si no se ha leído ya
            # df = clean_csv(df) # Limpia el CSV si no se ha limpiado ya
            # df = rename_col(df)  # Renombra las columnas si no se ha renombrado ya
        if args.function == 'breakdown_date':
            df = breakdown_date(df)
            print(df.head())
        elif args.function == 'erase_month':
            df = erase_month(df)
            print(df.head())
        else:
            df = breakdown_date(df)
            df = erase_month(df)
            print(df.head())

    elif args.module == 'agrupar':
        if df is None:
            df = read_csv(args.file_path)
            # df = clean_csv(df)
            # df = rename_col(df)
            df = breakdown_date(df)
            df = erase_month(df)
        if args.function == 'groupby_state_and_year':
            df = groupby_state_and_year(df)
            print(df.head())
        elif args.function == 'print_biggest_handguns':
            df = groupby_state_and_year(df)
            print_biggest_handguns(df)
        elif args.function == 'print_biggest_longguns':
            df = groupby_state_and_year(df)
            print_biggest_longguns(df)
        else:
            df = groupby_state_and_year(df)
            print(df.head())
            # print_biggest_handguns(df)
            # print_biggest_longguns(df)
    elif args.module == 'analisis_temporal':
        if df is None:
            df = read_csv(args.file_path)
            df = breakdown_date(df)
            df = erase_month(df)
        if args.function == 'time_evolution':
            time_evolution(df)
        else:
            time_evolution(df)
    elif args.module == 'analisis_estados':
        df = read_csv(args.file_path)
        df = breakdown_date(df)
        df = erase_month(df)
        df_grouped = groupby_state_and_year(df)
        if args.function == 'groupby_state':
            df_state = groupby_state(df_grouped)
            print(df_state.head())
        elif args.function == 'clean_states':
            df_state = groupby_state(df_grouped)
            df_cleaned_states = clean_states(df_state)
            print(df_cleaned_states.head())
        elif args.function == 'merge_datasets':
            df_state = groupby_state(df_grouped)
            df_cleaned_states = clean_states(df_state)
            df_merged = merge_datasets(df_cleaned_states, './Data/us-state-populations.csv')
            print(df_merged.head())
        elif args.function == 'calculate_relative_values':
            df_state = groupby_state(df_grouped)
            df_cleaned_states = clean_states(df_state)
            df_merged = merge_datasets(df_cleaned_states, './Data/us-state-populations.csv')
            df_relative = calculate_relative_values(df_merged)
            print(df_relative.head())
        elif args.function == 'handle_outliers':
            df_state = groupby_state(df_grouped)
            df_cleaned_states = clean_states(df_state)
            df_merged = merge_datasets(df_cleaned_states, './Data/us-state-populations.csv')
            df_relative = calculate_relative_values(df_merged)
            df_outliers_handled = handle_outliers(df_relative)
            print(df_outliers_handled.head())
        else:
            df_state = groupby_state(df_grouped)
            df_cleaned_states = clean_states(df_state)
            df_merged = merge_datasets(df_cleaned_states, './Data/us-state-populations.csv')
            df_relative = calculate_relative_values(df_merged)
            df_outliers_handled = handle_outliers(df_relative)
            print(df_outliers_handled.head())
    else:
        # Si no se especifica módulo ni función, ejecuta todo el flujo
        df = clean(args.file_path)
        df = breakdown_date(df)
        df = erase_month(df)
        df = groupby_state_and_year(df)
        # Imprimir el estado y el año con el mayor número de hand_guns
        print_biggest_handguns(df)
        print_biggest_longguns(df)
        time_evolution(df)
        df_state_grouped = groupby_state(df)
        df_cleaned_states = clean_states(df_state_grouped)
        df_merged = merge_datasets(df_cleaned_states, './Data/us-state-populations.csv')
        df_relative = calculate_relative_values(df_merged)
        df_outliers_handled = handle_outliers(df_relative)
        print(df_outliers_handled.head())
        generate_and_save_maps(df_outliers_handled)


if __name__ == "__main__":
    main()
