def calculate(a, b, formula):
  if formula == '+':
    return a + b
  elif formula == '-':
    return a - b
  elif formula == '*':
    return a * b
  elif formula == '/':
    return a / b
  else:
    print('Enter a valid input')
    return 'Closing program...'

a = float(input('enter first number: '))
b = float(input('enter second number: '))

formula = input('would you like to * / - or + the number you entered? ')

answer=calculate(a, b, formula)
print(answer)