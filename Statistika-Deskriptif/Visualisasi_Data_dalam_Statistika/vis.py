import pandas as pd
import matplotlib.pyplot as plt

kopi_data = {
    'jenis_kopi' : ['Latte', 'Capuccino', 'Americano', 'Espresso'],
    'total_omset' : [942, 1716, 731, 220]
}

kopi_df = pd.DataFrame(kopi_data)

print(kopi_df)



# Pie Chart
# kopi_df.plot(kind='pie', y='total_omset', labels=kopi_df['jenis_kopi'], figsize=(12,8), legend=False,)
# plt.show()

# Bar Plot

# kopi_df.plot(kind='bar', x='jenis_kopi', y='total_omset', legend=False, figsize=(12,8))
# plt.show()

# Dataset Iris

from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print(iris_df)

plt.figure(2, figsize=(10,6))
plt.scatter(data=iris_df, x='petal length (cm)', y='petal width (cm)')
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.show()