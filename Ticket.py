#Daniel Brookins:
#12/16/2024
#Ticket Generator

#Initialize
import turtle
t = turtle.Turtle()




#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

#Main
def ticket_generator():

#1. Introduce the customer to your app
    print("Welcome to the six flags ticket generator app")

#2. Collect the pertinent information
name= input("Enter name:")#string(Good!)
age= int(input("Enter age:"))#Integer(Good!)
#Day of the week
dayofweek= input("Enter Day of the week:")
y_location = 7
couponcode=input("Enter Coupon Code:")
#Name
#Age
#Day of the week
#Coupon code

#3.Algorithm for setting the price
if age <= 3:
    price = 0#baby price
elif age >= 4 and age <= 17 and dayofweek=="Monday" or "Tuesday" or "Wensday" or "Thursday" or "Friday" :
    price = 50

elif age >= 4 and age <= 17 and dayofweek=="Saturday" or "Sunday":
    price = 100

if age <=18:
    price = 100

if age >=4 and age<= 17 and dayofweek== "Monday" or "Tuesday" or "Wensday" or "Thursday" or "Friday" and couponcode=="FREEFRIDAY":
    price= 0

if age >=4 and age<= 17 and dayofweek=="Sunday" and couponcode=="SUNDAY10":
    price= 0



#4.Print the ticket

draw_ticket(name,price,dayofweek,7)

#Main

ticket_generator()

