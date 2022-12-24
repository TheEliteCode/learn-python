sum = 0

# boolean expression is True
while True:
  n = input("Enter a number: ")
  n = float(n)   # converting to float

  if n < 0:    # check if number is negative
    break
  sum += n

print("sum =", sum)
