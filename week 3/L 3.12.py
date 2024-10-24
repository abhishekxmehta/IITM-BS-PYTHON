# #1 find all prime number less than the given number

# num=int(input('Enter a number: '))
# if(num > 2):
#     print(2,end='')
# for i in range(3,num):
#     flag=False
#     for j in range(2,i):
#         if(i%j==0):
#             flag=False
#             break
#         else:
#             flag=True
#     if(flag):
#         print(i,end=' ')


# #2 find the total profit/loss of each trader working in a trading firm. information regarding number of traders and number of transactions in unknown

# empID =(input('Enter the employee ID: '))
# while(empID != '-1'):
#     trade = int(input('Enter the trade amount: '))
#     profit_loss = 0
#     while(trade != 0):
#         profit_loss += trade
#         trade = int(input('Enter the trade amount: '))
#     print(f'profit/loss for employee {empID} is {profit_loss}')   
#     empID = int(input('Enter the employee ID: '))

# #3 find the day wise total rainfall for the entered duration of time e.g week,month,etc.

# days = int(input('Enter the number of days: '))
# for i in range(1,days+1):
#     total = 0
#     rainfall=int(input('Enter the rainfall: '))
#     while(rainfall != -1):
#         total += rainfall
#         rainfall  = int(input('Enter the rainfall: '))
#     print('Total rainfall for the day {0} is {1} '.format(i, total))    

# #4 find the length of the longest word from the set of words entered by the user

# word = input('Enter a word: ')
# maxLen = 0
# while(word != '-1'):
#     count=0
#     for letter in word:
#         count += 1
#     if(count > maxLen):
#         maxLen = count
#     word = input('Enter a word: ')
# print('The length of the longest word in %s'%maxLen)            


