"""
Input: 5-минутные фрагменты готовых к фильтрации данных
Output: н/к первично отфильтрованных событий и сами события (формат?) --> validation.py

Process: 
Для каждого фрагмента:
- рассчитать energy-based metrics
- отфильтровать по длительности
- склеить близкие сигналы
- сохранять начало и конец событий 
- вырезать события из raw_data и preprocessed_data и сохранить их
"""
import os 
import matplotlib
import mne 
import numpy as np
mne.viz.set_browser_backend('qt')

# путь к файлу из filtered data
path_to_fif_file = "/home/dmin/Code/EEG_Detectors_test/data/filtered_data/sub_01_preprocessed_raw.fif"
interval = mne.io.read_raw_fif(path_to_fif_file, preload=True)

# Исправление багнутого файла с амплитудой в вольтах
data = interval.get_data()
print(f"Максимум: {data.max()}, Минимум: {data.min()}, Среднее: {data.mean()}")
print(interval.get_channel_types())
interval.apply_function(lambda x: x * 1e-6)
interval.plot()

# Расчёт energy-based метрик
LOW_FREQS_ripples = 80
HIGH_FREQS_ripples = 250
LOW_FREQS_fast_ripples = 250
HIGH_FREQS_fast_ripples = 500

interval_ripples = interval.copy().filter(l_freq=LOW_FREQS_ripples, h_freq=HIGH_FREQS_ripples)
interval_fast_ripples = interval.copy().filter(l_freq=LOW_FREQS_fast_ripples, h_freq=HIGH_FREQS_fast_ripples)

hilbert_ripples = interval_ripples.apply_hilbert(envelope=True)
hilbert_fast_ripples = interval_fast_ripples.apply_hilbert(envelope=True)

hilbert_ripples.plot()
hilbert_fast_ripples.plot()

