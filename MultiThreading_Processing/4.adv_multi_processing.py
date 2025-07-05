from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(i):
  time.sleep(2)
  return f"Square:{i*i}"

num=[1,2,3,4,5]

if __name__=="__main__":
  with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(square_numbers,num)

  for result in results:
    print(result)  