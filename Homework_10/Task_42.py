import pandas as bd
import numpy as np
import random


# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = bd.DataFrame({'whoAmI':lst})
data.head()

data['human'] = np.where(data['whoAmI'] == 'human', '1', '0')
data['robot'] = np.where(data['whoAmI'] == 'robot', '1', '0')

print(data)