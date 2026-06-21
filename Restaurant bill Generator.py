# Restaurant Bill Generator

print("===== Restaurant Bill Generator =====")

# Menu
pizza = 150
burger = 100
cold_drink = 50

print("\nMenu")
print("Pizza      : ₹150")
print("Burger     : ₹100")
print("Cold Drink : ₹50")

# Quantity input
q1 = int(input("\nEnter quantity of Pizza: "))
q2 = int(input("Enter quantity of Burger: "))
q3 = int(input("Enter quantity of Cold Drink: "))

# Bill calculation
total = (pizza * q1) + (burger * q2) + (cold_drink * q3)

# Display bill
print("\n===== BILL =====")
print("Pizza      :", q1, "x 150 =", pizza * q1)
print("Burger     :", q2, "x 100 =", burger * q2)
print("Cold Drink :", q3, "x 50 =", cold_drink * q3)
print("----------------------")
print("Total Bill = ₹", total)
print("======================")