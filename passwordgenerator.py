import random
import string
character=string.ascii_letters+string.digits+string.punctuation
a=int(input('how long u want your password to be'))
c=''
for i in range(a):
    b=random.choice(character)
    c=c+b

print(f'your password is {c}')

    