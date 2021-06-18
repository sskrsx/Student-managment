class std:
    def __init__(self,roll,name, add): 
        self.name = name
        self.add = add 
        self.roll=roll
#Take student details
    def inputdata(self):
        while(True):
            try:
                roll=int(input('Roll Number:-'))
                if type(roll) is int:
                    break
            except:
                print('!Please Enter Valid Input!')
        name=input('Name:-')
        add=input('Address:-')
        list.append(std(roll,name,add))
        
# Display student details  
    def display(self,n):
        i=n
        print()
        print('Roll Number:','%02d'%(list[i].roll))
        print('Name:',list[i].name.upper())
        print('Address:',list[i].add.upper())
# Search student student        
    def search(self):
        n=int(input('Enter Roll Number:-'))
        return n-1
# Edit student Details
    def edit(self,up):
        list[up].name=input('Enter New Name:')
        list[up].add=input('Enter New Address:')
#To print in file
    def printfile(self,n):
        i=n
        f.write('Roll Number:')
        f.write('%02d'%(list[i].roll))
        f.write('\nName:')
        f.write(list[i].name.upper())
        f.write('\nAddress:')
        f.write(list[i].add.upper())
        f.write('\n\n')
        

list=[]
obj1=std(0,' ', ' ')
count=1
while(True):
    print('Student Number:',"%02d"%(count))
    obj1.inputdata()
    count+=1
    print('-----------------------------------')
    exit=int(input('Enter 0 to exit \nEnter 1 to feed more student details:'))
    print('-----------------------------------')
    if (exit==0):
        break
    
print('-----------------------------------')
while(True):
    operation=int(input('Enter 1 For Search\nEnter 2 For Print all Details:\nEnter 3 for Edit:'))
    if(operation==1):
        search=obj1.search()
        obj1.display(search)
    elif(operation==2):
        for i in range(list.__len__()):
            obj1.display(i)
    elif(operation==3):
        up=int(input('Enter Roll Number for edit:'))
        obj1.edit(up-1)
        print('Update details is:')
        obj1.display(up-1)
    inp=input('Enter --close-- to close the program\nEnter any key to continue:')
    if inp=='close':
        break
prt=int(input('0 to exit with print details\n1 to exit without print details:'))
if prt == 0:
    f=open('student.doc','w')
    for i in range(list.__len__()):
        obj1.printfile(i)
    f.close
    print('THANKYOU\nSTUDENT DETAILS PRINTED')
else:
    print('THANKYOU!')

input()