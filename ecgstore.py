import pandas as pd


def store_ecg_data(record_name, data, columns, file_path):
    data_path = file_path + '/' + record_name + '.csv'
    data_df = pd.DataFrame(data, columns=columns)
    data_df.to_csv(data_path)
