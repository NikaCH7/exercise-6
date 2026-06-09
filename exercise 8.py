# import requests

# =====================================================================
# დავალება 1 SQL დავალება
# =====================================================================
"""
# SELECT ProductName, CategoryID, Unit, Price
# FROM Products
# WHERE Price BETWEEN 18 AND 25
# ORDER BY Price DESC;
"""
import requests

# =====================================================================
# დავალება 2 SQL დავალება2
# =====================================================================
"""
# SELECT *
# FROM OrderDetails
# WHERE Quantity = 15
#    OR Quantity = 12
# ORDER BY Quantity ASC;
# """

# =====================================================================
# დავალება 3
# =====================================================================
# print("--- პროდუქტი ---")
# products = [
#     {"id": 1, "price": 50},
#     {"id": 2, "price": 200},
#     {"id": 3, "price": 150}
# ]
#
# expensive_products = [prod for prod in products if prod["price"] > 100]
# print("პროდუქტები 100-ზე მეტი ფასით:", expensive_products)
# print("\n" + "=" * 50 + "\n")

# =====================================================================
# დავალება 4
# =====================================================================
# print("--- სახელები 4 ---")
# company_data = {
#     "company": {
#         "departments": [
#             {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#             {"name": "HR", "employees": [{"name": "Nino"}]}
#         ]
#     }
# }
#
# print("თანამშრომლების სახელები:")
# for department in company_data["company"]["departments"]:
#     for employee in department["employees"]:
#         print(employee["name"])
# print("\n" + "=" * 50 + "\n")
#
# =====================================================================
# დავალება 5
# =====================================================================
# print("--- სტუდენტები ---")
# students = [
#     {"name": "Ana", "grades": [90, 80, 95]},
#     {"name": "Beka", "grades": [70, 85, 88]},
#     {"name": "Nino", "grades": [100, 95, 99]}
# ]
#
# best_student = None
# highest_average = 0
#
# for student in students:
#     grades = student["grades"]
#     average = sum(grades) / len(grades)
#
#     if average > highest_average:
#         highest_average = average
#         best_student = student["name"]
#
# print(f"საუკეთესო სტუდენტი: {best_student} (საშუალო ქულა: {highest_average:.2f})")
# print("\n" + "=" * 50 + "\n")
#
# =====================================================================
# დავალება 6
# =====================================================================
# print("--- კომპანიები ---")
# corporate_data = {
#     "companies": [
#         {
#             "name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#             ]
#         },
#         {
#             "name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#             ]
#         }
#     ]
# }
#
# print("თანამშრომლები 4000-ზე მეტი ხელფასით:")
# for company in corporate_data["companies"]:
#     for employee in company["employees"]:
#         if employee["salary"] > 4000:
#             print(f"{employee['name']} + {company['name']}")
# print("\n" + "=" * 50 + "\n")
#
# =====================================================================
# დავალება 7
# =====================================================================
# print("--- მომხმარებელი ---")
# users_url = "https://jsonplaceholder.typicode.com/users"
# users_response = requests.get(users_url)
#
# if users_response.status_code == 200:
#     users_list = users_response.json()
#     print("პირველი მომხმარებლის სახელი:", users_list[0]["name"])
# else:
#     print("შეცდომა მონაცემების წამოღებისას")
# print("\n" + "=" * 50 + "\n")

# =====================================================================
# დავალება 8
# =====================================================================
# print("--- მოთხოვნა ---")
# posts_url = "https://jsonplaceholder.typicode.com/posts"
# new_post_data = {
#     "title": "Test",
#     "body": "Hello World",
#     "userId": 5
# }
#
# post_response = requests.post(posts_url, json=new_post_data)
# print("სერვერის პასუხი (სტატუს კოდი):", post_response.status_code)
# print("შექმნილი ობიექტი:", post_response.json())
# print("\n" + "=" * 50 + "\n")
# #
# =====================================================================
# დავალება 9
# =====================================================================
# print("--- completed ---")
# todos_url = "https://jsonplaceholder.typicode.com/todos"
# todos_response = requests.get(todos_url)
#
# if todos_response.status_code == 200:
#     todos_list = todos_response.json()
#     uncompleted_count = 0
#
#     print("შეუსრულებელი ტასკები:")
#     for task in todos_list:
#         if not task["completed"]:
#             print(f"- {task['title']}")
#             uncompleted_count += 1
#
#     print(f"\nსულ შეუსრულებელი ტასკების რაოდენობა: {uncompleted_count}")
# else:
#     print("შეცდომა მონაცემების წამოღებისას")
# print("\n" + "=" * 50 + "\n")

# =====================================================================
# დავალება 10
# =====================================================================
# print("--- პოსტი ---")
# # წამოვიღოთ პოსტები და მომხმარებლები ერთდროულად
# all_posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
# all_users_response = requests.get("https://jsonplaceholder.typicode.com/users")
#
# if all_posts_response.status_code == 200 and all_users_response.status_code == 200:
#     posts = all_posts_response.json()
#     users = all_users_response.json()
#
#     # შევქმნათ მომხმარებლების ID-ების და სახელების ლექსიკონი ოპტიმიზაციისთვის
#     user_dict = {user["id"]: user["name"] for user in users}
#
#     print("პირველი 5 პოსტი და ავტორი:")
#     for post in posts[:5]:
#         author_name = user_dict.get(post["userId"], "უცნობი ავტორი")
#         print(f"{post['title']} – {author_name}")
# else:
#     print("შეცდომა API-დან მონაცემების წამოღებისას")