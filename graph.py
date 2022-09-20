import pandas as pd
import matplotlib.pyplot as plt

print("Введите путь до файла, включая его")
map = input()

# print("Введите ось X")
# xlabel = input()

print("Введите ось Y")
ylabel = input()

print("Введите толщину граифка")
width = input()

print("Введите название файла для сохранения с .png")
file_name = input()

data = pd.read_csv(map, sep='\s+', header=None)
data = pd.DataFrame(data)

time = data[0]
signal = data[1]

plt.xlim(0, max(time))

plt.xlabel("Time")
plt.ylabel(ylabel)
plt.title("huy")

plt.plot(time, signal, label='test', linewidth=width)

plt.grid()
plt.legend(loc='upper left')

plt.savefig(file_name)

plt.show()