"""
Нарезает ЭЭГ из raw_data на 5-минутные фрагменты на основе данных из DataIntervals.tsv

Сохраняет в n3_intervals

Input: DataIntervals.tsv + raw_data/.edf
Output: n3_intervals/sub_**/n3_interval_**.edf
"""


"""
создаём пустой словарь (номер эпохи, начало, конец)
зайти в папку derivatives/sub_01/ses_01/eeg 

открыть файл DataIntervals: 
    для строк, в которых столбец RunNb != 0 берем начало и конец эпохи из столбцов StartInd EndInd, сохраняет в словарь, присваивая номер эпохи 

открыть файл .edf:
    вырезвает из него фрагменты
    каждый фрагмент записывает в файл n3_intervals/sub_**/n3_interval_**.edf
"""

