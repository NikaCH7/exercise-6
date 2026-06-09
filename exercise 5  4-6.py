# დავალება4
# text = input("შეიყვანე ტექსტი: ")
#
# if text == text[::-1]:
#     print("პალინდრომია!")
# else:
#     print("პალინდრომი არ არის!")
#
#     found = False
#
#     for i in range(len(text)):
#         candidate = text[:i] + text[i + 1:]
#
#         if candidate == candidate[::-1]:
#             print(f"უახლოესი პალინდრომი: {candidate}")
#             found = True
#             break
#
#     if not found:
#         print("ერთი წაშლით პალინდრომი ვერ მოიძებნა")

# დავალება5
# import random
# word = input("შეიყვანე ერთი სიტყვა: ")
#
# if " " in word:
#     print("შეიყვანე მხოლოდ ერთი სიტყვა!")
#
# elif not word.isalpha():
#     print("გამოიყენე მხოლოდ ასოები!")
#
# else:
#     print("\nშესაძლო ზედმეტსახელები:")
#
#     print(word.capitalize() + "King")
#     print("Super" + word.capitalize())
#     print(word.capitalize() + "X")
#     print("Dark" + word.capitalize())
#     print("The" + word.capitalize())
#     print(word + str(random.randint(10, 99)))

# დავალება6
# import random
#
# user_input = input("შეიყვანე რიცხვები გამოტოვებით: ")
#
# numbers = user_input.split()
#
# try:
#     numbers = list(map(int, numbers))
# except ValueError:
#     print("შეიყვანე მხოლოდ რიცხვები!")
#     exit()
#
# print("\nაირჩიე:")
# print("1 - ზრდადობით")
# print("2 - კლებადობით")
# print("3 - random")
# print("4 - მხოლოდ უნიკალური")
#
# choice = input("შენი არჩევანი: ")
#
# if choice == "1":
#     numbers.sort()
#     print(numbers)
#
# elif choice == "2":
#     numbers.sort(reverse=True)
#     print(numbers)
#
# elif choice == "3":
#     random.shuffle(numbers)
#     print(numbers)
#
# elif choice == "4":
#     print(list(set(numbers)))
#
# else:
#     print("არასწორი არჩევანი!")