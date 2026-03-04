"""
Input: n3_intervals
Output: preprocessed_data

Process:
Для каждого 5-минутного фрагмента:
- удаление bad channels 
- ремонтаж ? 
- реджекторные фильтры
- полосовая фильтрация
- спектральное выравнивание?
"""


import os 
import mne 


def preprocess_file(path_to_edf_file, LOW_FREQS, HIGH_FREQS):
    """
    path_to_edf_file - путь к целовому фрагменту сигнала
    LOW_FREQS - нижний порог фильтрации
    HIGH_FREQS - верхний порог фильтрации
    """
    interval = mne.io.read_raw_edf(path_to_edf_file, preload=True)

    interval.notch_filter(freqs=50)

    interval.filter(l_freq=LOW_FREQS, h_freq=HIGH_FREQS)

    return interval 


def main(path, sub_num, low_freqs, high_freqs):
    interval = preprocess_file(path, low_freqs, high_freqs)
    interval.save(f'data/filtered_data/sub_{sub_num}_preprocessed_raw.fif', overwrite=True, fmt='single')
    interval.plot()


if __name__ == '__main__':
    path = "/home/dmin/Code/EEG_Detectors_test/data/n3_intervals/sub_01/sub-01_ses-01_task-hfo_run-01_eeg.edf"
    sub_num = '01' # добавить автоматическое определение номера испытуемого
    LOW_FREQS = 80
    HIGH_FREQS = 500
    main(path, sub_num, LOW_FREQS, HIGH_FREQS)