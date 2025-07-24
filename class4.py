# def grade(score):
#     if score >= 80:
#         print("Grade A")
#     elif score >= 70:
#         print("Grade B")
#     elif score >= 60:
#         print("Grade C")
#     elif score >= 50:
#         print("Grade D")
#     else:
#         print("Grade F")

# grade(60)

# def my_sum(a, b):
#     return a + b

# print(my_sum(5, 6))

# def itemsPrice(price, frequency):
#     totalPrice = (price * frequency) * 1.07
#     return totalPrice

# def menuNav():
#     while True:
#         choice = int(input("Do you which to proceed (1) or to exit (2): "))
#         if choice == 1:
#             price = float(input("What is the price of the item?: "))
#             frequency = int(input("How many do you want?: "))
#             return itemsPrice(price, frequency)
#         elif choice == 2:
#             print("Quitting...")
#             break

# print("your total price is", menuNav())

my_list = [1, 2, "qu"]
# print("Before", my_list[1])
# my_list[1] = 3
# print("After", my_list[1])

# print("Before", my_list)
# my_list.append("TR")
# my_list.pop()
# print("After", my_list)

# for i in my_list:
#     print(i)

# my_dict = {"name" : "qu",
#            "age" : 18}
# print(my_dict["name"])

# my_dict["IT"] = 31
# print("After", my_dict)

students = [
    {"name" : "Qu", "age" : 18},
    {"name" : "Fi", "age" : 20}
]

for i in students:
    print(i["name"])