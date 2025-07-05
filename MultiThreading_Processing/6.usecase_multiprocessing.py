'''
Real world example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial calculation
Factorial calculation for large numbers, involve significant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.

'''
import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def compute_factorial(num):
  print(f"Computing  factorial of {num}")
  result = math.factorial(num)
  print(f"Factorial of {num} is {result}")
  return result

if __name__ =="__main__":
  num=[5000,6000,7000]
  start_time =time.time()

  with multiprocessing.Pool() as pool:
    results  = pool.map(compute_factorial,num)

  end_time = time.time()

  print(f"Results: {results}")
  print(f"Time taken : {end_time - start_time} seconds")  

  