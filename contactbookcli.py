import json
try:
    with open('contact.json', 'r') as j:
        contact = json.load(j)
except:
    contact = []
while True:
    print('1-add contact')
    print('2-view contact')
    print('3-search contact')
    print('4-delete contact')
    print('5-quit')
    a=int(input('what you want to do select with nunber'))
    if a==5:
        break
    
    elif a==1:
        b=input('enter the name of the person')
        c=input('enter the number of the person')
        contact.append({'name':b,'number':c})
        with open('contact.json','w') as j:
            json.dump(contact,j)
    
    elif a==2:
        for i,person in enumerate(contact):
            print(f'{i+1} . {person['name']}--{person['number']}')
    
    elif a==3:
        d=input('enter the name of ther person')
        for person in contact:
            if d == person['name']:
                print(person)
    
    elif a==4:
        e=input('enter the contact name you want to delete')
        for person in contact:
            if e == person['name']:
                contact.remove(person)
                with open('contact.json', 'w') as j:
                    json.dump(contact, j)
                print('deleted!')
                break
        