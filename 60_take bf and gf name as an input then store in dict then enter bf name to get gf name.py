d = {}
while True :
    bf = input('enter the bf name :')
    gf = input('enter the gf name :')
    d[bf] = gf
    choice = input('do you want to add more item [Y/N]')

    if choice == 'N' :
        break
while True :
    bf = input('enter bf name to get gf name :')
    gf = d.get(bf)
    print(f'Hi {bf} your gf name is {gf}')

    choice == input('do you want to add more item [Y/N]')
    
    if choice == 'N' :
        break

