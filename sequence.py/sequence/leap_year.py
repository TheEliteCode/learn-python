# this program tests for leap years

year = 2000

if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print(year, 'is a leap year')
    else:
      print(year, 'is not a leap year')
  else:
       print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

# Output: 2000 is a leap year
