import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



data = [128, 100, 180, 150, 200, 90, 340, 105, 
        85, 270, 200, 65, 230, 150, 150, 120, 130, 80, 
        230, 200, 110, 126, 170, 132, 140, 112, 90, 340, 170, 190]

nilai_terkecil = min(data)
nilai_terbesar = max(data)

print("Nilai Terkecil:", nilai_terkecil)
print("Nilai Terbesar:", nilai_terbesar)

# plt.hist(data, bins=7)
# plt.show()

sns.set(color_codes=False)
sns.displot(data, bins=7, kde=False)
plt.show()

