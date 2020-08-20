# Note that these implementations are naive - uselist-comprehensions/ numpy if you have to generate/multiply two matrices! This is just to show the benefits of static typing!
from typing import List,Set

def mat_mult_unsafe(a,b):
  a_rows = len(a)
  b_rows = len(b)
  a_cols = len(a[0])
  b_cols = len(b[0])
  result = [ [ 0 for i in range(len(b[0]))] for j in range(len(a))] 
  for i in range(a_rows):
   for j in range(b_cols):
       for k in range(b_rows):
           result[i][j] += a[i][k] * b[k][j]
  return result

def mat_mult_safe(a:List[List[int]],b:List[List[int]])->List[List[int]]:
  a_rows = len(a)
  b_rows = len(b)
  a_cols = set()
  b_cols = set()
  result = [[]]
  for i in range(a_rows):
    a_cols.add(len(a[i]))
  for i in range(b_rows):
    b_cols.add(len(b[i]))
  if(len(a_cols) == 1 and len(b_cols) == 1):
    if(list(a_cols)[0] != 1 and list(b_cols)[0] !=1 and a_rows == list(b_cols)[0]):
      a_cols = list(a_cols)[0]
      b_cols = list(b_cols)[0]
      result = [ [ 0 for i in range(len(b[0]))] for j in range(len(a))]    
  else:
    raise Exception("Go and look at the definition of a matrix")
  for i in range(a_rows):
   for j in range(b_cols):
       for k in range(b_rows):
           result[i][j] += a[i][k] * b[k][j]

  return result

print(mat_mult_safe([[1,2],[3,4]],[[1,2],[3,4]]))
print(mat_mult_unsafe([[1,2],[3,4]],[[1,2],[3,4]]))
