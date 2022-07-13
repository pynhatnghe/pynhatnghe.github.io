from time import sleep, perf_counter

def task(id):
    print(f'Starting a task {id}...')
    sleep(1)
    print(f'done {id}')

start_time = perf_counter()
task(1)
task(2)
end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')