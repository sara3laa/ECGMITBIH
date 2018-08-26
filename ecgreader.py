import wfdb


def read_ecg_signal(record_name):
    signals, fields = wfdb.rdsamp(record_name, sampfrom=0, sampto=None, channels=None, pb_dir='mitdb')
    return signals, fields


def read_ecg_ann(record_name):
    annotation = wfdb.rdann(record_name, 'atr', pb_dir='mitdb')
    return annotation.sample, annotation.symbol
