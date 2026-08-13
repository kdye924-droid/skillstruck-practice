# string= " the number of miles we've kiked totals up to {}"
# miles=21
# print(string.format(miles))

# age=17

# birthday="{}"

# print(birthday.format(age)) #print age

Jasmine=int(input("how many bags does Jasmine have?"))

Chloe=int(input("how many bags does Chloe have?"))

bags_Jasmine= Jasmine * 12 

Chloe_bags= Chloe * 10

# bags=12

string=" If Jasmine had {} bags, she would have {} marbles total. If Chloe had {} bags, she would have {} marbles total."

print(string.format(Jasmine,bags_Jasmine,Chloe,Chloe_bags))