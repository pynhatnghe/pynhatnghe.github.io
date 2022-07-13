import datetime
from time import sleep, perf_counter
from threading import Thread

def task(id):
    print(f'Starting a task {id}...')
    sleep(1)
    print(f'done {id}')

def say_hello(name, dob):
    print(f"Hello {name}")
    sleep(2)
    print(f"{datetime.datetime.now().year  - dob} tuổi")

start_time = perf_counter()

# Demo Multi thread
my_threads = []
# Step 1: Init thread
for i in range(1, 11):
    if i % 2 == 0:
        mt = Thread(target=task, args=(i,))
    else:
        mt = Thread(target=say_hello, args=(f"A{i}", 1979))
    my_threads.append(mt)
# Step 2: Thread start
for my_thread in my_threads:
    my_thread.start()
# Step 3: Chờ Thread finish
for my_thread in my_threads:
    my_thread.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')