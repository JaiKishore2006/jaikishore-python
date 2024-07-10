try :
     x=int(input( "enter a year "))
     y=str(input("enter a month "))
    
except TypeError :
     print("something went wrong")

except Exception :
     print(" nothing is wrong")

finally :
     print("done")