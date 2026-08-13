
#find out how many people will come to dinnder
num_people=int(input(" How many people are comeing to dinnder? "))


# buy some food! Hamburgers are $1.29, Rolls are $0.49, and Corn is $0.80. total up the ithems

#prices
hamburger_price=1.29
rolls_price=0.49
corn_price=0.80

#how much will people have
hamburger_count= int(input(" How many hamburgers will everyone have? "))

rolls_count=int(input("How many rolls will everyone have? "))

corn_count=int(input("How many pieces of corn will you have? "))

total=0
total = total + (hamburger_count * hamburger_price * num_people)

total = total + ( rolls_count * rolls_price * num_people)

total = total + ( corn_count * corn_price * num_people)

noChange=int(total / num_people)
change=float(total / num_people)

print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.") 