# num = int(input('Enter a number: '))
# fact=1
# if(num<=0):
#     print('Not defined')
# else:    
#  while(num > 0):
#     fact = fact * num
#     num = num - 1
#  print (fact)

# num = int(input('Enter a number: '))
# fact=1
# if(num<=0):
#     print('Not defined')
# else:    
#    for i in range(num,1,-1):
#       fact = fact * i

# print(fact)

#problem 2 find the number of digits in the given number

# f = abs(int(input('Enter a number :')))
# digits = 1
# while(f > 10):
#  f = f // 10
#  digits += 1

# print(digits)

#''Problem 3: Reverse the digits in the given number'''

# num = int(input('Enter a number: '))
# absStrNum = str (abs (num))
# rev = ''
# for c in absStrNum:
#    rev = c + rev
# if (num >= 0):
#   print (rev)
# else:
#  print('-' + rev)