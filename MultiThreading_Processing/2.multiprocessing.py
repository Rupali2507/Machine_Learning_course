# Multiprocessing is a Python module that allows you to run multiple processes in parallel, each with its own Python interpreter and memory space. This is useful for CPU-bound tasks that need to utilize multiple CPU cores, such as data processing, computations, or simulations.

# Use multiprocessing when:
# - Your program is CPU-bound (heavy computations).
# - You want to bypass Python’s Global Interpreter Lock (GIL).
# - You need true parallelism (not just concurrency).

# For I/O-bound tasks (like network or file operations), threading or async may be more efficient.


import multiprocessing

import time

def square_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"Square:{i*i}")

def cube_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"Cube:{i*i*i}")    

if __name__ == "__main__":
  p1 = multiprocessing.Process(target=square_numbers)
  p2=multiprocessing.Process(target=cube_numbers)
  t =time.time()
  p1.start()
  p2.start()

  p1.join()
  p2.join()
  finished = time.time()-t

  print(finished)


