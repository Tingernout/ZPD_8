import time
start = time.time()

for i in range(0, 10000):
    g = 0
    g += i
print(i)


end = time.time()
print(f"Время выполнения: {end - start} секунд")