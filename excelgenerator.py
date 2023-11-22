import pandas as pd


def excel_generator(name, quote, ability, time):

    data = {'analyst_name': [name],
            'quote_difficulty': [quote],
            'analyst_ability': [ability],
            'completion_time': [int(time)]
            }
    
    df = pd.DataFrame(data)

    excel_file_path = "reporte.xlsx"

    try:
        with pd.ExcelWriter(excel_file_path, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name="datos_simulacion", header=None, startrow=writer.sheets["datos_simulacion"].max_row, index=False)
    
    except FileNotFoundError:
        with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='datos_simulacion', index=False)
