import time
def slow_function():
    time.sleep(2)
start = time.time()
slow_function()
end = time.time()
execution_time = end - start
print(f"Время выполнения: {execution_time:.2f} секунд")