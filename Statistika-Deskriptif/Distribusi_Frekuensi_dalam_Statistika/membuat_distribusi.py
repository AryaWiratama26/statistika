import numpy as np

data = [128, 100, 180, 150, 200, 90, 340, 105, 85, 270, 200, 65, 230, 150, 150, 120, 130, 80, 230, 200, 110, 126, 170, 132, 140, 112, 90, 340, 170, 190]

n_class = 7

minn = min(data)
maxx = max(data)
rangee = maxx - minn

classWidth = rangee / n_class
print("Lebar Kelas:", np.ceil(classWidth))

# for i in range(n_class):
#     lower_bound = minn + i * classWidth
#     upper_bound = lower_bound + classWidth
#     count = sum(lower_bound <= x < upper_bound for x in data)
#     print(f"Kelas {i+1}: {lower_bound:.2f} - {upper_bound:.2f}, Frekuensi: {count}")

# interval 64-104

coba_data = []
for i in data:
    if i >= 64 and i <= 104:
        coba_data.append(i)
        
print(len(coba_data))