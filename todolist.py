a=[]
f=[]
while True:
    print('1-Add tasks')
    print('2-view tasks')
    print('3-mark tasks as done')
    print('4-quit')
    b=input('chose a number 1,2,3,4 for tasks')
    
    if b=='4':
        break
    
    elif b=='1':
        c=input('add tasks: ')
        a.append({'task':c,'done':False})
    
    elif b=='2':
        for i,t in enumerate(a):
            status='X' if t['done'] else ''
            print(f'{i+1}.[{status}] {t['task']}')
    
    elif b=='3':
        d=int(input('which task number is completed: '))
        a[d-1]['done']=True
        