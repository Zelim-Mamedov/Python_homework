# 10.1[44]: Дан код, генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Статья про one hot вид https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

# Сделайте one hot вид с использованием get_dummies
# Сделайте one hot вид с использованием изученных методов группировки данных. Обратите внимание, что Nan это не ноль.

# import random
# import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

# Создание DataFrame
df = pd.DataFrame({'color': ['red', 'blue', 'green', 'green', 'red', 'blue']})

# Применение метода get_dummies()
one_hot = pd.get_dummies(df['color'])

# Вывод результата
print(one_hot)
