from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(num):
  
    time.sleep(1)
    return f"Number:{num}"

num=[1,2,3,4,5,4,3,3,4,2,3,1]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,num)

for result in results:
    print(result)    