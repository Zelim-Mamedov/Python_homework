# 9.2[42]: Работа в Google Colab. Файл california_housing_train.csv, который находится в папке sample_data
# Узнать какая максимальная households в зоне минимального значения population

from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing(as_frame=True)

filtered_housing = housing.data[(housing.data['population'] >= 0) & (housing.data['population'] <= 500)]

print(filtered_housing['median_house_value'])