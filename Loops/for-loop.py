for char in "hello":
  print(char)

for x in range(1, 10):
  print(x)

# RANGES 

range(7) # 0 thru 6 
range(1, 8) # 1 to 7
# It can take a third param "step" 
# how many to skip or which way to count, up or down
range(1, 10, 2) # odd numbers from 1 to 10 
range(7, 0, -1) # 7 to 1 

r = range(10)
list(r)