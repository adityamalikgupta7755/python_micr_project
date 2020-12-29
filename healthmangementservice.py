import datetime
a = datetime.datetime.now()
while True:
    print("""\
        Welcome to HMS
        1. Are you want enter data
        2. Are you want see record
        3. exit
        """)
    option = int(input("enter your option"))
    print(option)
    if option == 1:

        print("""\
        Select client name
        1. Add Exercise
        2. Add Dite
        4. exit
            """)
        option1 =int(input("enter your option"))
        if option1 == 1:
            print("""\
                1. Aditya
                2. harsh
                3. shivam
                4. exit
            """)
            list=['Aditya', 'harsh','shivam']
            option2 =int(input("enter your option"))
            option2 = option2-1
            name = list[option2]
            dec = input("enter the exercise name")
            f = open(name,"a")
            decs = dec+'--'+str(a)+'\n'
            f.write(decs)
            f.close()
            print('successfuly data enter')
        elif option1 == 2:
            print("""\
                1. Aditya
                2. harsh
                3. shivam
                4. exit
            """)
            list=['Aditya', 'harsh','shivam']
            option2 =int(input("enter your option"))
            option2 = option2-1
            name = list[option2]
            dec = input("enter the dite")
            f = open(name,"a")
            decs = dec+'--'+str(a)+'\n'
            f.write(decs)
            f.close()
            print('successfuly data enter')   
        else:
            break     
    elif option == 2:
        print("""\
            select name whose record you want see
            1. Aditya
            2. harsh
            3. shivam
            4. exit
            """)
        list=['Aditya', 'harsh','shivam']
        option3 =int(input("enter your option"))
        option3 = option3-1
        name = list[option3]
        f = open(name,"rt")
        content =f.read()  
        print(content)    
    else:
        break




