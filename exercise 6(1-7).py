# დავაკება 1
# import itertools
# word = "ABCD"
# all = list(itertools.permutations(word))
# for variant in all:
#     combined_word = "".join(variant)
#     print(combined_word)
# print("-" * 20)
# total_count = len(all)
# print(f"სულ შესაძლო ვარიანტების რაოდენობაა: {total_count}")

# დავალება 2
# from datetime import date, timedelta
#
# today = date.today()
# print(f"დღევანდელი დღეა: {today} ({today.strftime('%A')})")
#
# current_weekday = today.weekday()
#
# days_to_next_tuesday = 7 - current_weekday + 1
#
# next_tuesday = today + timedelta(days=days_to_next_tuesday)
#
# print("-" * 30)
# print(f"მომდევნო კვირის პირველი სამშაბათი იქნება: {next_tuesday} ({next_tuesday.strftime('%A')})")

 # დავალება 3
# import calendar
# my = input("შეიყვანეთ წელი (მაგ: 2024): ")
# year = int(my)
# if calendar.isleap(year):
#     print(f"კი, {year} ნაკიანი წელია! (თებერვალს აქვს 29 დღე)")
# else:
#     print(f"არა, {year} არ არის ნაკიანი წელი. (თებერვალს აქვს 28 დღე)")

# დავალება 4

# from datetime import date
# today = date.today()
# next_new_year = date(today.year + 1, 1, 1)
# days_left = (next_new_year - today).days
# weeks_left = days_left // 7
# remaining_days = days_left % 7
# print(f"დღევანდელი თარიღი: {today}")
# print(f"ახალ წლამდე დარჩენილია: {weeks_left} კვირა და {remaining_days} დღე.")
# print(f"(სულ სუფთა დღეებში: {days_left} დღე)")

# დავალება 5

# import itertools
# numbers = [1, 2, 3, 4, 5]
# i= list(itertools.combinations(numbers, 3))
# for combo in i:
#     print(combo)
# print("-" * 20)
# total_count = len(i)
# print(f"სულ კომბინაციების რაოდენობაა: {total_count}")

# დავალება 6

# import itertools
# chars = "XYZ"
# for length in range(1, 4):
#     print(f"\n--- სიგრძე {length} ---")
# i= list(itertools.product(chars, repeat=length))
# for var in i:
#         combined_text = "".join(var)
#         print(combined_text)

# დავალება 7

# from datetime import datetime, timedelta
# import random
# import time
# secret_number = random.randint(1, 20)
# print("თამაში დაიწყო! კომპიუტერმა ჩაიფიქრა რიცხვი 1-დან 20-მდე.")
# print("თქვენ გაქვთ ზუსტად 5 წამი სწორი პასუხის მისაღებად და Enter-ზე დასაჭერად!")
# print("მომზადდით...")
# time.sleep(1)
# print("სტარტი!\n")
# start_time = datetime.now()
# user_input = input("შეიყვანეთ რიცხვი: ")
# end_time = datetime.now()
# time_taken = end_time - start_time
# if time_taken > timedelta(seconds=5):
#     print("დრო ამოიწურა, თქვენ დამარცხდით")
#     print(f"(თქვენ დაგჭირდათ: {time_taken.total_seconds():.2f} წამი)")
# else:
#     if user_input.isdigit() and int(user_input) == secret_number:
#         print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი ({secret_number}) და ჩაეტიეთ დროში!")
#         print(f"თქვენი დრო: {time_taken.total_seconds():.2f} წამი.")
#     else:
# #         print(f"დროში კი ჩაეტიეთ, მაგრამ პასუხი არასწორია! ჩაფიქრებული იყო: {secret_number}")
