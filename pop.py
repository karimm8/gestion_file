print('gestion pass word')

def add():
    user = input('entre un user: ')
    pw = input('entre un pw: ')
    with open('pw.txt','a') as f:
        f.write(f'{user}|{pw}\n')

def view():
    with open('pw.txt','r') as f:
        lines = f.readlines()
        if lines:
            for line in lines:
                print(line.strip())
        else:
            print('vide')

def eff():
    with open('pw.txt','w') as f:
        pass

def dell():
    user_del = input('entre user avec delte: ')
    with open('pw.txt','r') as f:
        lines = f.readlines()
    with open('pw.txt','w') as f:
        for line in lines:
            user, pw = line.strip().split('|')
            if user != user_del:
                f.write(line)
    if not lines:
        print('aucun user')
    else:
        print('bien supp')

while True:
    answer = input('entre add or view or effacer or del par user or (q=quit): ').lower()
    if answer == 'q':
        quit()
    elif answer == 'add':
        add()
    elif answer == 'view':
        view()
    elif answer == 'eff':
        eff()
    elif answer == 'del':
        dell()
    else:
        print('invalid')