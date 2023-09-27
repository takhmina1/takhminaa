

class Car:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
    def __str__(self):
        return say,car,color
    
    def say(self):
        return 'Hello'
    
    def color(self):
        return 'black'
    
    def car(self):
        return number
    
    
    
    
res = Car(name='dhfdf',age=43)
print(f'{res.age}')
print(f'{res.name}')
print(res.color())

















class BankAccount:
    def init(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print("Баланс:", account.get_balance())  

account.deposit(500)
print("Баланс после депозита:", account.get_balance())  

account.withdraw(200)
print("Баланс после снятия:", account.get_balance())  









class Person:
    
    def __init__(self):
        self.name = name
        self.age = age
        
        
    def say(self):

        return f"{self.}"
    
    
    
    
a = Person(name='Erdemi',age=23)
print(a.name)
print(a.age)








class Student:
    def __init__(self,stud):
        self.stud = stud
        
    def __str__():
        return b,bal
        
    def b(self):
        return f'{self.name} {self.age}'
    
    def bal(self):
        a = {'Alice':100,'Billi':85,'Eny':74,'Jon':58}
        bal_ = [bal for name,bal in a.items() if bal==100 ]
        return f'name:  bal: {bal_}'
     

student = Student(stud='Hello')
print(student.bal())    
   
    
    

    
    
    
class BankAccount:
    def init(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print("Баланс:", account.get_balance())  

account.deposit(500)
print("Баланс после депозита:", account.get_balance())  

account.withdraw(200)
print("Баланс после снятия:", account.get_balance())





class Person():
    
    def __init__(self,name,age,kol=2,butu=2,bashi=1):
        self.name = name
        self.age = age
        self.kol = kol
        self.butu = butu
        self.bashi = bashi
        
    def __str__(self):
        return basalat,suyloyalat,
    
    def basalat(self):
        return f'basalat'
    
    def suyloyalat(self):
        return f'suyloyalat '
    
    
    
    
    
    
a = Person(name='Alice',age=17,kol=2,butu=2,bashi=1)
print(a.basalat())
print(a.suyloyalat())
print(a.age)
print(a.bashi)
print(a.bashi)
print(a.name)


class Person2(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.name = name
        self.age = age
        

a2 = Person2(name='Eni',age=14)

print(a2.name)
print(a2.age)
print(a2.basalat())
print(a2.suyloyalat())




class Person3(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.name = name 
        self.age = age

a3 = Person3(name='Jon',age=24)

print(a3.name)
print(a3.age)
print(a3.basalat())
print(a3.suyloyalat())










"""

Создайте класс "Транспортное средство" с методом "двигаться". 
Создайте классы "Автомобиль" и "Велосипед", 
которые наследуют класс "Транспортное средство" и переопределите метод "двигаться" 
для каждого класса,
чтобы он выводил соответствующее сообщение.
Создайте объекты классов "Автомобиль" и "Велосипед" и вызовите их методы "двигаться".








# """

class Mbank:
    def __init__(self,name,age,surname,__cash,__gold):
        self.name = name
        self.age = age
        self.surname = surname
        self.__cash = 0
        self.__gold = False
    
    def __verification(self):
        self.__gold = True
        
    def get__cash(self):
        return f'Balance {self.__cash} som'
    
    def set__cash(self,x):
        self.__cash = self.__cash + x
        
    def info(self):
        return f'Name {self.name} \n Surname {self.surname}'
    
    def shopping(self, x):
        if self.__cash >= x:
            if x <= 100_000:
                self.__cash = self.__cash -x
                return 'Udacha'
            else:
                 if self.__gold:
                     self.__cash = self.__cash - x
                     return f'balance jetpey jetti: '
                 else:
                     return 'Vash status nizok'
        else:
            return f'jetpey jatat {self.get__cash()}'
        
    
    
    def get_gold(self):
        if self.__gold:
            return 'status cold'                
         
        else:
            self.__verification()
            return 
        
        


            
                
       def get_gold(self):
        if self.__gold:
            return 'status cold'                
         
        else:
            self.__verification()
            return 
        






online = Mbank('Sanjar','Ayazov')
print(online.info())
print(online.get__cash())
online.set__cash(10000)
print(online.get__cash())




class MyClass:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def public_method(self):
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")
        

obj = MyClass()
print(obj.public_var)  # Доступ к public_var без ограничений
print(obj._protected_var)  # Доступ к _protected_var, но это считается соглашением об ограниченном доступе
# print(obj.private_var)  # Ошибка, private_var недоступен извне класса

obj.public_method()  # Вызов public_method без ограничений
obj._protected_method()  # Вызов _protected_method, но это считается соглашением об ограниченном доступе
# obj.private_method()  # Ошибка, private_method недоступен извне класса




class Transaction:
    def __init__(self, amount):
        self.amount = amount
        self.commission = 0
     
    
    def calculate_commission(self):
        if self.amount < 100000:
            self.commission = self.amount * 0.03
        else:
            self.commission = 100 + self.amount * 0.012
    
    def make_transaction(self):
        self.calculate_commission()
        total_amount = self.amount + self.commission
        return total_amount


transaction1 = Transaction(1000)
total1 = transaction1.make_transaction()  
transaction2 = Transaction(1000000)
total2 = transaction2.make_transaction()  

print(total1)
print(total2)
print(transaction1)