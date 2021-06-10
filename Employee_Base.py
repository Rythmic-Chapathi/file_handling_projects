run=True

def exit():
    global run
    run=False

def add():
    user_id= int(input('Enter the ID'))
    name = input('Employee name')
    salary = input('Employees salaries')
    
    a = open('employees.txt','a')
    a.write(user_id+','+name+','+salary+'\n')
    a.close()

def search():
    check=input("Enter your Salary\n")
    f=open("employees.txt","r")
    lines=f.readlines()
    for line in lines:
        data=line.split(',')
        if data[2]==check:
            print("ID: "+str(data[0])+"\nName: "+data[1]+"\nSalary: "+str(data[2]))



   



    


while run:
    print('1) Add a new worker')
    print('2) Search for an employee by salary')
    print('3) Exit')
    option=int(input("Enter your option "))

    print("the option is ",option ,"\n")

    if option==1:
        add()

    elif option==2:
        search()
        

    elif option==3:
        exit()
       
    else:
        print('INVALID')