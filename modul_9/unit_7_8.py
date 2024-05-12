import numpy as np
mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,-9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)
# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
#print(nans_index)
# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)
#print(n_nan)
# Скопируйте массив `mystery` в массив `mystery_new`. Заполните пропущенные 
# значения в массиве `mystery_new` нулями
mystery_new = mystery.copy()
mystery_new[nans_index] = 0
#print(mystery_new)
# Поменяйте тип данных в массиве mystery на int32
mystery_int = np.int32(mystery)
# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)
# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3), order='F')
#  Сохраните в переменную col столбец 2
col = table[:, 1]