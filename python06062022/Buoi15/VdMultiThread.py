from time import sleep, perf_counter
from threading import Thread

def task(id):
    print(f'Starting a task {id}...')
    sleep(1)
    print(f'done {id}')

start_time = perf_counter()
# Single thread
# task(1)
# task(2)

# Demo Multi thread
# Step 1: Init thread
t1 = Thread(target=task, args=(1,))
t2 = Thread(target=task, args=(2,))
# Step 2: Thread start
t1.start()
t2.start()
# Step 3: Chờ Thread finish
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')