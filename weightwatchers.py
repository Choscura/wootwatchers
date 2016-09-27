"""welcome to w00t watchers!"""
#import sqlite3      #
import sys          #       sys imported for exception handling

#DB_Connection = sqlite3.connect("Profiles.db")


def consoleinput():
    """
    This function exists to set Global Variables via console input.
    """
    weight                  = input("Please enter your weight in lbs:\n ")
    bodyfat_measurement     = input("please enter your most recent bodyfat measurement:\n")
    bodyweight_target       = input("please enter your target bodyweight:\n")
    bodyfat_target          = input("please enter target body fat (as %): \n") 

def goalmaker(weight, bodyfat_measurement, bodyweight_target, bodyfat_target):
    print("you have ", float(weight)-float(bodyweight_target), " pounds to lose.")
    print("according to the scale measurements, you need to lose ", 
            float(weight)               /100* float(bodyfat_measurement) + 
            float(bodyweight_target)    /100* float(bodyfat_target), " pounds.")
    
def leanmasscalculator(weight, bodyfat_measurement, bodyweight_target, bodyfat_target):
    current_lean_mass   =   float(weight)               -   (   float   (weight) * (   float(bodyfat_measurement)  /   100     )   )
    current_fat_mass    =   float(weight)               -       float   (current_lean_mass)
    goal_lean_mass      =   float(bodyweight_target)    -   (   float   (bodyweight_target) * (    float(bodyfat_target)/100   ))
    goal_fat_mass       =   float(bodyweight_target)    -       float   (goal_lean_mass)
    if( float(current_lean_mass) >= float(goal_lean_mass)   ):
        print(  "you have "   ,  float(current_lean_mass) - float(goal_lean_mass) , " pounds of lean mass to lose")
    elif(float(goal_lean_mass) >= float(current_lean_mass)):
        print(  "you have "   ,  float(goal_lean_mass) - float(current_lean_mass), "pounds of muscle to gain")
    print(  "you weigh "                                        ,   weight, 
            " pounds, of which "                                ,   current_fat_mass, 
            " is unhealthy ugly fat, which you need to lose "   ,   current_fat_mass - goal_fat_mass, 
            " pounds of.")

def loadprofile(person):
    print("ASSHOLE!")

def caloriesin(lbs):
    print("total calories in should be between ",   float(lbs)*10, " and ", float(lbs)*12, " for weight loss")
    print("between\t\t",    float(lbs)*14, " and ", float(lbs)*15, " for maintenance, and")
    print("between\t\t",    float(lbs)*16, " and ", float(lbs)*18, " for gaining muscle.")
    print("Total Range: ",  float(lbs)*10, " to ",  float(lbs)*18)

def preworkout(lbs):
    print("90 minutes before, you should have a meal with ", float(lbs)* 0.25, " grams of protein and carbohydrates, with normal fat content")
    print("")

def main():
    try:
        name = input("please identify yourself:")
        filename = name.lower() + "_measurements.csv"
        #example: kendall_measurements.csv
        print(filename)
        loadprofile(filename)  
        file = open("measurements.csv", "w") 
    except FileNotFoundError:
        weight                  = input("Please enter your weight in lbs:\n ")
        bodyfat_measurement     = input("please enter your most recent bodyfat measurement:\n")
        bodyweight_target       = input("please enter your target bodyweight:\n")
        bodyfat_target          = input("please enter target body fat (as %): \n")

    except:
        print("Unexpected error:", sys.exc_info()[0])
        caloriesin(weight)
        filename
    goalmaker(weight, bodyfat_measurement, bodyweight_target, bodyfat_target)
    leanmasscalculator(weight, bodyfat_measurement, bodyweight_target, bodyfat_target)
    preworkout(weight)

main()


