import random
print('choose difficulty:')
x=input('easy,hard')
if x==('easy'):
    print('you choose easy ')
    a=random.randint(1,50)
    attempt=0
    while attempt < 7:
      y=int(input('pick a number between 1-50'))
      if y==a:
          print(f'you won the number was {a}')
          break
      else:
          print('try againg')
          y=int(input('pick a number between 1-50'))
          attempt=attempt+1

elif x==('hard'):
    print('you choose hard ')
    b=random.randint(1,100)
    z=int(input('guess a number between 1-100:'))
   whie attempt<10:
       if z==b:
           print(f'yah you won the number was{b}')
       else:
           print('you lost')    
           z=int(input('guess a number between 1-100:'))
           attempt=attempt+1
else:('wrong input')