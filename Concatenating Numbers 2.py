# string="I took my dog on a walk, we saw {} ducks and {}deer."
# ducks=3
# deer=2
# print(string.format(ducks, deer))

# dollars=int(input("How many dollars? "))
# cents=int(input("How many cents? "))
# num_cookies=int(input("How many cookies do you want to buy? "))

# cookie_price = dollars + (cents / 100)

# total_cost = cookie_price * num_cookies

# message = "The total cost of {} cookies is ${}."

# print(message.format(num_cookies, total_cost))


num=input("choose a three digit number")
first=int(num[0]) + int(num[1]) + int(num[2])

message="The sum of those digits is {}."
print(message.format(first))