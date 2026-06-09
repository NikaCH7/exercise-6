# import random
# import string
#
#
# def check_answer(question):
#     attempts = 3
#
#     while attempts > 0:
#         answer = input(question).lower()
#
#         if answer in ["yes", "no"]:
#             return answer
#
#         attempts -= 1
#         print(f"შეიყვანეთ მხოლოდ yes ან no. დარჩენილი ცდები: {attempts}")
#
#     print("ცდები ამოიწურა!")
#     exit()
#
#
# attempts = 3
#
# while attempts > 0:
#     Length = input("შეიყვანეთ პაროლის სიგრძე: ")
#
#     if Length.isdigit():
#         Password_length = int(Length)
#         break
#
#     attempts -= 1
#     print(f"შეიყვანეთ მხოლოდ რიცხვი. დარჩენილი ცდები: {attempts}")
#
# if attempts == 0:
#     print("ცდები ამოიწურა!")
#     exit()
#
#
# Big_Letter = check_answer("გსურთ დიდი ასოები? (yes/no): ")
# Small_Letter = check_answer("გსურთ პატარა ასოები? (yes/no): ")
# Number = check_answer("გსურთ რიცხვები? (yes/no): ")
# Simbol = check_answer("გსურთ სიმბოლოები? (yes/no): ")
#
# Password_Choice = []
#
# if Big_Letter == "yes":
#     Password_Choice.extend(string.ascii_uppercase)
#
# if Small_Letter == "yes":
#     Password_Choice.extend(string.ascii_lowercase)
#
# if Number == "yes":
#     Password_Choice.extend(string.digits)
#
# if Simbol == "yes":
#     Password_Choice.extend(string.punctuation)
#
# if not Password_Choice:
#     print("შეცდომა: არცერთი სიმბოლო არ აგირჩევია!")
# else:
#     Password = ""
#
#     for i in range(Password_length):
#         Password += random.choice(Password_Choice)
#
#     print(f"თქვენი პაროლია: {Password}")
from cryptography.hazmat.asn1.asn1 import sequence


# დავალება2
# import string
#
# password = input("შეიყვანეთ პაროლი: ")
# score = 0
#
# if len(password) >= 8:
#     score += 2
# has_digit = False
# for char in password:
#     if char.isdigit():
#         has_digit = True
#         break
#
# if has_digit:
#     score += 2
# has_upper = False
# for char in password:
#     if char.isupper():
#         has_upper = True
#         break
#
# if has_upper:
#     score += 2
# has_lower = False
# for char in password:
#     if char.islower():
#         has_lower = True
#         break
#
# if has_lower:
#     score += 2
# has_symbol = False
# for char in password:
#     if char in string.punctuation:
#         has_symbol = True
#         break
#
# if has_symbol:
#     score += 2
# repeated = False
#
# for char in password:
#     if password.count(char) > 2:
#         repeated = True
#         break
#
# if repeated:
#     score -= 2
#
# if score < 0:
#     score = 0
#
# print(f"ქულა: {score}/10")
#
# if score <= 3:
#     print("Weak")
# elif score <= 7:
#     print("Medium")
# else:
#     print("Strong")

# დავალება3
# def Fibonacci(length):
#     sequence = [0,1]
#     while len(sequence) < length:
#         next_number = sequence[-1] + sequence[-2]
#         sequence.append(next_number)
#     return sequence
#
# while True:
#     user_input = input("შეიყვანე ფიბონაჩის სიგრძე: ")
#
#     if user_input.isdigit():
#         number = int(user_input)
#
#         if number <= 0:
#             print("შეიყვანე 1-ზე მეტი რიცხვი!")
#             continue
#
#         break
#
#     elif user_input.isalpha():
#         print("შენ შემოიტანე ტექსტი, მხოლოდ რიცხვი შეიყვანე!")
#
#     else:
#         print("შენ შემოიტანე სიმბოლო, მხოლოდ რიცხვი შეიყვანე!")
#
#
# result = Fibonacci(number)
#
# print("ფიბონაჩის რიგი:")
# print(result)