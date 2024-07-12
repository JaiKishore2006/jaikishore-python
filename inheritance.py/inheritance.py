# task1
# single inheritance

# class marvel():
#      def mystery(self):
#           print("has more fictious stories...........")

# class dc(marvel):
#      def dark(self):
#           print("more dark theme movies..............")

# justice_league=dc()
# justice_league.dark()
# justice_league.mystery()                    

# task2
# multiple inheritance

# class pogo():
#      def mrbean(self):
#           print("a cartoon show of channel")

# class hungama():
#      def shinchan(self):
#           print("a comedy show of channel")

# class chuttitv(pogo,hungama):
#       def jackiechan(self):
#         print("cartoon and adventure show")
        
# jai=chuttitv()
# jai.jackiechan()        
# jai.mrbean()   
# jai.shinchan()


# TASK3
# multilevel

# class grandfather():
#     def gold(self):
#         print("grandpa gold....")

# class father(grandfather):
#     def money(self):
#         print("father money")

# class son(father):
#     def diamond(self):
#         print("son diamond")        


# jai=son()
# jai.diamond()       
# jai.money() 
# jai.gold()

# heirachial inheritance
# task4

class navy():
    def weapons(self):
        print("all navy weapons")

class army():
      def missiles(self):
            print("all missiles")         

class soldier1(navy,army):        
        pass
class soldier2(army):
       pass
class soldier3(army):
      pass
        
jai=soldier1()
jai.missiles()       
jai.weapons()

jack=soldier2()
jack.missiles()

jake=soldier3()
jake.missiles()