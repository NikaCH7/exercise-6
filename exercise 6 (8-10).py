# დავალება 8

# from datetime import datetime, timedelta
# import random
# start = datetime.now()
# player1 = start + timedelta(seconds=random.randint(5, 20))
# player2 = start + timedelta(seconds=random.randint(5, 20))
# print(f"რბოლის დაწყების დრო: {start.strftime('%H:%M:%S')}")
# print(f"მოთამაშე 1-ის ფინიშის დრო: {player1.strftime('%H:%M:%S')}")
# print(f"მოთამაშე 2-ის ფინიშის დრო: {player2.strftime('%H:%M:%S')}")
# print("-" * 40)
# if player1 < player2:
#      time_difference = (player2 - player1).total_seconds()
#      print(f"გამარჯვებულია მოთამაშე 1! მან {time_difference} წამით ნაკლებ დროში დაასრულა გარბენი.")
# elif player2 < player1:
#     time_difference = (player1 - player2).total_seconds()
#     print(f"გამარჯვებულია მოთამაშე 2! მან {time_difference} წამით ნაკლებ დროში დაასრულა გარბენი.")
# else:
#     print("წარმოუდგენელი შედეგია! დაფიქსირდა ფრე, ორივემ ერთ დროში დაასრულა!")

# დავალება 9

# from datetime import date
# print("--- ინფორმაცია ---")
# birth_year = int(input("შეიყვანეთ დაბადების წელი (მაგ: 2000): "))
# birth_month = int(input("შეიყვანეთ დაბადების თვე (1-12): "))
# birth_day = int(input("შეიყვანეთ დაბადების დღე (1-31): "))
# birthday = date(birth_year, birth_month, birth_day)
# today = date.today()
# next_birthday = date(today.year, birthday.month, birthday.day)
# if next_birthday < today:
#     next_birthday = date(today.year + 1, birthday.month, birthday.day)
# days_left = (next_birthday - today).days
# print("-" * 40)
# print(f"დღეს არის: {today}")
# print(f"თქვენი დაბადების თარიღია: {birthday.strftime('%d %B %Y')}")
# if days_left == 0:
#     print("ვაშაა! გილოცავთ, თქვენი დაბადების დღე სწორედ დღეს არის!")
# else:
#     print(f"თქვენს შემდეგ დაბადების დღემდე დარჩენილია: {days_left} დღე.")

# დავალება 10

# import itertools
# import random
# digits = [1, 2, 3, 4, 5, 6]
# secret_password = tuple(random.choices(digits, k=4))
# secret_string = "".join(map(str, secret_password))
# print(f"🔒 კომპიუტერმა საცავი ჩაკეტა პაროლით: {secret_string}")
# print("სისტემა იწყებს ყველა ვარიანტის ავტომატურ გადარჩევას...\n")
# all_possibilities = itertools.product(digits, repeat=4)
# for guess in all_possibilities:
#     guess_string = "".join(map(str, guess))
#     print(f"ვცდი ვარიანტს: {guess_string}")
#     if guess == secret_password:
#         print("-" * 40)
#         print("პაროლი სწორია, საცავი გახსნილია! 🎉🔓")
#         print(f"საცავი გაიტეხა პაროლით: {guess_string}")
#         break