#Write a function for the cost of ground shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.
def ground_shipping(weight):
  if (weight <= 2):
    cost = 20.00 + weight * 1.50
  elif (weight > 10):
    cost = 20.00 + weight * 4.75
  elif (weight > 2) and (weight <= 6):
    cost = 20.00 + weight * 3.00
  else:
    cost = 20.00 + weight * 4.00
  return cost

eight_pound = ground_shipping(8.4)
print(eight_pound)

#Create a variable for the cost of premium ground shipping.
premium_ground_shipping = 125.00


#Write a function for the cost of drone shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.
def drone_shipping(weight):
  if (weight <= 2):
    cost = weight * 4.50
  elif (weight > 10):
    cost = weight * 14.25
  elif (weight > 2) and (weight <= 6):
    cost = weight * 9.00
  else:
    cost = weight * 12.00
  return cost

one_pound = drone_shipping(1.5)
print(one_pound)

#Using those two functions for ground shipping cost and drone shipping cost, as well as the cost of premium ground shipping, write a function that takes one parameter, weight and prints a statement that tells the user
def cheapest_option(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    option = "Ground Shipping"
    cost = ground_shipping(weight)
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    option = "Drone Shipping"
    cost = drone_shipping(weight)
  elif premium_ground_shipping < ground_shipping(weight) and premium_ground_shipping < drone_shipping(weight):
    option = "Premium Ground Shipping"
    cost = premium_ground_shipping
  return "You should using " + option + ", it will cost $" + str(cost) +"."


four = cheapest_option(4.8)
print(four)

fourty_one = cheapest_option(41.5)
print(fourty_one)

eleven = cheapest_option(11.5)
print(eleven)
