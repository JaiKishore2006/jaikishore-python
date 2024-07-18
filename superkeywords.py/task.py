# task
# 1.Create a base class called shape withe method area that return 0 .create a derived class called rectangle
# that inerit from shape and overrides the area method to calculate 
# and return the area of a rectangle.


# class shape():
#      def area(self):
#         return("0")   
     
# class rectangle(shape):
     
#     def __init__(self,height,width):
         
#      self.width=width
#      self.height=height
     
#      def area(self):
#          return("area of the rectangle")
     
#      def area(self):
#         return self.width * self.height


# rect = rectangle(5, 10)
# print( rect.area())


# 2.create a base class called person with constructor that takes a name as a parameter . Create a derived called student that inherits from  person has 
# constructor that takes a parameter called grade. 
# Write a method in student to display name and grade of student .
# Use super keywords to achieve this.


# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)  
#         self.grade = grade
    
#     def display_info(self):
#         print( self.name)
#         print(self.grade)

# student = Student("Alice", "A")

# student.display_info()

# create a base class called vehicle with a method start that print 
# " vehicle started" create a derived class called car that inherits from vehicle
#  and overrides the start method to print " car started”.

# class vehicle():
#     def start(self):
#      print("vehicle started")

# class Car(vehicle):
#     def start(self):
#         print("Car started")

# car = Car()
# car.start() 



# 1.Create a base class Animal with a method sound() that prints a generic sound.
#  Create a derived class Dog that inherits from Animal and overrides the sound() method to print "Woof".


# class Animal:
#     def sound(self):
#         print("Generic animal sound")


# class Dog(Animal):
#     def sound(self):
#         print("Woof")

# dog = Dog()

# dog.sound()  


# .Create classes A and B, then create a class C
# that inherits from both A and B. Each parent class
#  should have a method display() that prints a message specific to that class.


# class A():
#     def display(self):
#         print("Display method of class A")

# class B():
#     def display(self):
#         print("Display method of class B")

# class C(A, B):
#     pass


# objc = C()

# objc.display()  

# objc.display() 
