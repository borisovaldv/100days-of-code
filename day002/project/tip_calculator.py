print('Welcome to the tip calculator')
bill = float(input('What was the bill? $'))
percentage = int(input('What much tip would you like to give? 10, 12, or 15? '))
people = int(input('How much people split the bill? '))
result = bill * (percentage / 100) + (bill / people)
print(f'Each person should pay: ${round(result, 2)}')