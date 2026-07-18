
expenses = []

while True:
    a = input('write the name of expense (or done to stop): ')
    
    if a == "done":
        break
    
    b = float(input('enter the amount: '))
    c = {"name": a, "amount": b}
    expenses.append(c)

for i,e in enumerate(expenses):
    print(f'{i+1}.  {e['name']} - {e['amount']}')

total=0
for e in expenses:
    total=total+e["amount"]
print(f'the total is{total}')
biggest=max(expenses, key=lambda e: e["amount"])
print(f'The biggest expense is {biggest['name']} and ammount {biggest['amount']}')
