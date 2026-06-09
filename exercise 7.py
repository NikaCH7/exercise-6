# # დავალება 1
# # word = "CODE"
# #
# # # გენერატორის შექმნა ფრჩხილების გამოყენებით
# # gen = (char for char in word)
# #
# # # შეგვიძლია ციკლითაც დავბეჭდოთ, რომ სათითაოდ არ ვწეროთ next()
# # for char in gen:
# #     print(char)
#
# # დავალება 2
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # try:
# #     user_input = input("შემოიყვანეთ ინდექსი (0-დან 8-მდე): ")
# #     index = int(user_input)
# #
# #     element = arr[index]
# #     print(f"თქვენ მიერ არჩეული ელემენტია: {element}")
# #
# # except ValueError:
# #     print("შეცდომა: შემოიყვანეთ მხოლოდ ციფრები! ასოები ან სიმბოლოები არ შეიძლება.")
# #
# # except IndexError:
# #     print("შეცდომა: ასეთი ინდექსით ელემენტი ლისტში არ არსებობს (მიაწვდით საზღვრებს გარეთ).")
#
#
# # დავალება 3
#
# # def counter(func):
# #     count = 0
# #
# #     def wrapper(*args, **kwargs):
# #         nonlocal count
# #         count += 1
# #         print(f"გამოძახება: {count}")
# #
# #         return func(*args, **kwargs)
# #
# #     return wrapper
# #
# # @counter
# # def say():
# #     print("Hi")
# #
# # say()
# # say()
#
#
# # დავალება 4
#
# # import random
# # import logging
# #
# # logging.basicConfig(
# #     filename='game.log',
# #     level=logging.INFO,
# #     format='%(asctime)s - შედეგი: %(message)s',
# #     filemode='a'
# # )
# #
# # def play_math_game():
# #     score = 0
# #     total_questions = 5
# #
# #     print(f"--- მათემატიკური თამაში ---")
# #     print(f"გაგვაჩნია {total_questions} შეკითხვა. თითოეული სწორი პასუხი = 10 ქულა.\n")
# #
# #     for i in range(1, total_questions + 1):
# #         num1 = random.randint(1, 10)
# #         num2 = random.randint(1, 10)
# #         correct_answer = num1 * num2
# #
# #         try:
# #             user_input = input(f"შეკითხვა {i}: რამდენია {num1} * {num2}? ")
# #             user_answer = int(user_input)
# #
# #             if user_answer == correct_answer:
# #                 print("სწორია! (+10 ქულა)")
# #                 score += 10
# #             else:
# #                 print(f"არასწორია. სწორი პასუხი იყო {correct_answer}.")
# #
# #         except ValueError:
# #             print("შეცდომა: უნდა შეიყვანოთ მხოლოდ ციფრები! (ამ შეკითხვაზე 0 ქულა)")
# #
# #
# #     logging.info(f"{score} ქულა")
# #
# #     print("\n--------------------------")
# #     print(f"თამაში დასრულდა! თქვენი საბოლოო ქულაა: {score}")
# #     print("შედეგი ჩაიწერა game.log ფაილში.")
# #
# # if __name__ == "__main__":
# #     play_math_game()
#
# # დავალება 5
#
# # import logging
# #
# # logging.basicConfig(
# #     filename='quiz.log',
# #     level=logging.INFO,
# #     format='%(asctime)s - %(message)s',
# #     filemode='a',
# #     encoding='utf-8'
# # )
# #
# # def quiz_generator():
# #     questions = [
# #         "1. რა ჰქვია პითონში ფუნქციას, რომელიც 'ზარმაცად' (lazy) აბრუნებს მნიშვნელობებს?",
# #         "2. რომელი ბლოკი გამოიყენება ერორების (შეცდომების) დასაჭერად პითონში?",
# #         "3. tuple არის ცვლადი (mutable) თუ უცვლადი (immutable) ობიექტი?",
# #         "4. რომელი მოდულით ვწერთ პროგრამის მუშაობის ისტორიას ფაილში?",
# #         "5. რა ეწოდება ფუნქციას, რომელიც ცვლის სხვა ფუნქციის ქცევას მისი კოდის შეუცვლელად?"
# #     ]
# #
# #     for question in questions:
# #         yield question
# #
# # def run_quiz():
# #     print("--- ვიქტორინა დაიწყო ---")
# #     print("უპასუხეთ შეკითხვებს. თქვენი პასუხები ჩაიწერება quiz.log-ში.\n")
# #
# #     questions_gen = quiz_generator()
# #
# #     for q in questions_gen:
# #         print(q)
# #         user_answer = input("თქვენი პასუხი: ")
# #         print("-" * 40)
# #
# #         logging.info(f"შეკითხვა: {q} | პასუხი: {user_answer}")
# #
# #     print("\nვიქტორინა დასრულდა! ყველა პასუხი წარმატებით შეინახა quiz.log ფაილში.")
# #
# #
# # if __name__ == "__main__":
# #     run_quiz()
#
# # davaleba 6
#
# # import random
# # import logging
# #
# # logging.basicConfig(
# #     filename='rps_game.log',
# #     level=logging.INFO,
# #     format='%(asctime)s - %(message)s',
# #     filemode='a',
# #     encoding='utf-8'
# # )
# #
# #
# # def play_rps():
# #     choices = ["ქვა", "ბადე", "მაკრატელი"]
# #     user_score = 0
# #     computer_score = 0
# #     round_number = 1
# #
# #     print("=== ქვა, ბადე, მაკრატელი ===")
# #     print("თამაში მიმდინარეობს 3 მოგებამდე! წარმატებები!\n")
# #     logging.info("--- ახალი თამაში დაიწყო ---")
# #
# #     while user_score < 3 and computer_score < 3:
# #         print(f"--- რაუნდი {round_number} ---")
# #         user_input = input("შეიყვანეთ (ქვა, ბადე, მაკრატელი): ").strip()
# #
# #         if user_input not in choices:
# #             print("არასწორი არჩევანი! გთხოვთ ჩაწეროთ: ქვა, ბადე ან მაკრატელი.\n")
# #             continue
# #
# #         computer_choice = random.choice(choices)
# #         print(f"კომპიუტერის არჩევანია: {computer_choice}")
# #
# #         if user_input == computer_choice:
# #             result_text = "ფრეა"
# #             print("ამ რაუნდში ფრეა!\n")
# #         elif (user_input == "ქვა" and computer_choice == "მაკრატელი") or \
# #                 (user_input == "ბადე" and computer_choice == "ქვა") or \
# #                 (user_input == "მაკრატელი" and computer_choice == "ბადე"):
# #             result_text = "მოიგო მომხმარებელმა"
# #             user_score += 1
# #             print(f"თქვენ მოიგეთ ეს რაუნდი! (თქვენ: {user_score} | კომპიუტერი: {computer_score})\n")
# #         else:
# #             result_text = "მოიგო კომპიუტერმა"
# #             computer_score += 1
# #             print(f"კომპიუტერმა მოიგო ეს რაუნდი! (თქვენ: {user_score} | კომპიუტერი: {computer_score})\n")
# #
# #         logging.info(
# #             f"რაუნდი {round_number}: მომხმარებელი [{user_input}] - კომპიუტერი [{computer_choice}] | "
# #             f"შედეგი: {result_text} | მიმდინარე ანგარიში: {user_score}:{computer_score}"
# #         )
# #
# #         round_number += 1
# #
# #     print("=========================================")
# #     if user_score == 3:
# #         winner_message = "მომხმარებელმა გაიმარჯვა!"
# #         print(f"გილოცავთ! {winner_message}")
# #     else:
# #         winner_message = "კომპიუტერმა გაიმარჯვა!"
# #         print(f"სამწუხაროდ, {winner_message}")
# #
# #     print("თამაშის სრული ისტორია შენახულია rps_game.log ფაილში.")
# #     logging.info(f"თამაში დასრულდა. საბოლოო გამარჯვებული: {winner_message}\n")
# #
# #
# # if __name__ == "__main__":
# #     play_rps()
#
# # დავალება 7
#
# # import random
# #
# #
# # def roll_dice():
# #     return random.randint(1, 6)
# #
# #
# # def start_dice_game():
# #     print("=== კამათლის თამაში: Gamer 1 VS Gamer 2 ===")
# #     game_round = 1
# #
# #     while True:
# #         print(f"\n--- რაუნდი {game_round} ---")
# #
# #         while True:
# #
# #             input("Gamer 1, დააჭირეთ Enter-ს კამათლის გასაგორებლად...")
# #             g1_score = roll_dice()
# #             print(f"Gamer 1-მა გააგორა: {g1_score}")
# #
# #             input("Gamer 2, დააჭირეთ Enter-ს კამათლის გასაგორებლად...")
# #             g2_score = roll_dice()
# #             print(f"Gamer 2-მა გააგორა: {g2_score}\n")
# #
# #             if g1_score == g2_score:
# #                 print("ანგარიში თანაბარია (ფრე)! კამათელს ვაგორებთ ხელახლა...\n")
# #                 print("-" * 30)
# #             else:
# #                 break
# #
# #         if g1_score > g2_score:
# #             winner = "Gamer 1"
# #             loser = "Gamer 2"
# #         else:
# #             winner = "Gamer 2"
# #             loser = "Gamer 1"
# #
# #         print(f"🏆 ამ რაუნდში გაიმარჯვა: {winner}-მა!")
# #         print("-----------------------------------------")
# #
# #
# #         print(f"კითხვა {winner}-ს:")
# #         rematch_choice = input(f"მისცემთ კიდევ 1 შანსს {loser}-ს? (კი/არა): ").strip().lower()
# #
# #         if rematch_choice == "კი" or rematch_choice == "ki":
# #             print(f"\n{winner}-მა მისცა შანსი {loser}-ს! ახალი თამაში იწყება...")
# #             game_round += 1
# #             print("=" * 40)
# #         else:
# #             print(f"\n{winner}-მა უარი თქვა ახალ შანსზე. თამაში საბოლოოდ დასრულდა!")
# #             break
# #
# #
# # if __name__ == "__main__":
# #     start_dice_game()
#
# # დავალება 8
#
# import random
#
#
# def play_word_game():
#
#     words = ["პითონი", "პროგრამა", "კამათელი", "კომპიუტერი", "ეკრანი", "ფაილი", "ლოგიკა", "ცვლადი", "ფუნქცია", "ციკლი"]
#
#
#     chosen_words = random.sample(words, 2)
#
#     obscured_words = []
#
#
#     for word in chosen_words:
#         word_letters = list(word)
#
#         indices_to_remove = random.sample(range(len(word)), 2)
#
#         for index in indices_to_remove:
#             word_letters[index] = "_"
#
#
#         obscured_words.append("".join(word_letters))
#
#     print("=== გამოიცანი სიტყვები ===")
#     print("სიტყვებში გამოტოვებულია 2 ასო (აღნიშნულია '_' სიმბოლოთი).\n")
#
#
#     print(f"პირველი სიტყვა: {obscured_words[0]}")
#     guess1 = input("ჩაწერეთ პირველი სიტყვა სრულად: ").strip()
#
#     print(f"\nმეორე სიტყვა: {obscured_words[1]}")
#     guess2 = input("ჩაწერეთ მეორე სიტყვა სრულად: ").strip()
#
#
#     correct_guesses = 0
#     if guess1 == chosen_words[0]:
#         correct_guesses += 1
#     if guess2 == chosen_words[1]:
#         correct_guesses += 1
#
#
#     print("\n--------------------------")
#     if correct_guesses == 2:
#         print("“გამარჯვება”")
#     elif correct_guesses == 1:
#         print("“50%”")
#     else:
#         print("“დამარცხდი”")
#
#
# if __name__ == "__main__":
#     play_word_game()