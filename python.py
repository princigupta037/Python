
#list
list = [[1,2,3],[3,4,5],[8,9,10]]
for item in list:
    for i in item: 
        print(i)
print(item)

#average

def average(n1,n2):
    return (n1+n2)/2
print(average(2,3))

#while loop

n =int(input())
while(n>1):
    print('no is ' ,n)
    break

#String

string='0123456789'
print(string[0:5])
print(string[-2:])
print(string[:-2])
print(string[:])

# to write file

file1= open("/home/princi/Documents/pythonnotes/w.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("hello ji","UTF-8"))
file1.close()

#to read file

file = open('/home/princi/Documents/pythonnotes/w.txt','r+')
text_to_read = file.read()
print(text_to_read)


#name , id and salary

class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self,name,id,salary):
        self.__name = name
        self.__id= id
        self.__salary = salary

    def set_salary(self,salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_name(self):
        return self.__name

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

princi =  Employee('princi',1,5000)

print(princi.get_name())
print(princi.get_id())
print(princi.get_salary())


#first name & lastname

class Person:
    
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def full_name(self):
        return f"{self.fname} {self.lname}"

p1 = Person('princi','gupta')
print(p1.full_name())
