import ecgreader as er
import ecgstore as es
import pandas as pd
import  os
records = pd.read_csv('records_names.csv', header=None, squeeze=True, index_col=0)

choose = int(input('if you want to store signals Enter "1" ,to store Annotations Enter "2" for both Enter 3\n'))
for record in records:

    record_name = str(record)
    if choose == 1 or choose == 3:
        signals, field = er.read_ecg_signal(record_name)
        folder_name = 'RawECG'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        es.store_ecg_data(record_name,signals, columns=['Lead1', 'Lead2'], file_path=folder_name)
    if choose == 2 or choose == 3:
        sample, symbol = er.read_ecg_ann(record_name)
        folder_name = 'Annotation'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        data = {'Sample': sample,
                'Symbol': symbol}
        es.store_ecg_data(record_name,data, columns=None, file_path=folder_name)
