import logging

logging.basicConfig(
  
  level=logging.DEBUG,
  format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  handlers=[
    logging.FileHandler("app1.log"),
    logging.StreamHandler()
  ]
)

logger=logging.getLogger("AirthmeticApp")

def add(a,b):
  result = a+b
  logger.debug(f"Adding {a}+{b} ={result}")
  return result

def sub(a,b):
  result = a-b
  logger.debug(f"Subtracting {a}-{b}= {result}",)
  return result

def multiply(a,b):
  result = a*b
  logger.debug(f"multiplying {a}*{b} ={result}",)
  return result

def divide(a,b):
  try:
     result = a/b
     logger.debug(f"dividing {a}/{b}={result} ")
     return result
  except ZeroDivisionError:
    logger.error("Division by zero error")
    return None
  

add(4,7)
sub(6,2)
multiply(6,7)
divide(5,1)  