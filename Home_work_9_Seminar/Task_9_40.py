# 9.1[40]: Работа в Google Colab. Файл california_housing_train.csv, который находится в папке sample_data
# Для домов, где кол-во людей от 0 до 500 (population) вывести информацию о цене дома(median_house_value):

# максимальное значение
# минимальное значение
# среднее
# медиану

import pandas as pd


df = pd.DataFrame({'column': ['a', 'b', 'c', 'a', 'c']})


one_hot = pd.get_dummies(df['column'])


df = pd.concat([df, one_hot], axis=1)


df.drop('column', axis=1, inplace=True)

print(df)
