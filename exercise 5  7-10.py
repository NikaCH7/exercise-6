# დავალება7
# text = input("შეიყვანე ტექსტი: ")
#
# result = ""
#
# for i in text:
#     if i.isalpha() or i == " ":
#         result += i
#
# print(result)

# დავალება8
# user_input = input("შეიყვანე რიცხვები გამოტოვებით: ")
#
# numbers = list(map(int, user_input.split()))

# while len(numbers) > 1:
#     print(numbers)
#
#     new_list = []
#
#     for i in range(len(numbers) - 1):
#         sum_pair = numbers[i] + numbers[i + 1]
#         new_list.append(sum_pair)
#
#     numbers = new_list
#
# print(numbers)

# დავალება9
# text = input("შეიყვანე ტექსტი: ").lower()
#
# words = text.split()
#
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# max_count = max(word_count.values())
#
# most_common = []
#
# for word, count in word_count.items():
#     if count == max_count:
#         most_common.append(word)
#
# print("ყველაზე ხშირი სიტყვ(ებ)ი:")
# print(*most_common)
# print(f"რაოდენობა: {max_count}")

# დავალება10
# sentence = input("შეიყვანე წინადადება: ")
#
# words = sentence.split()
#
# word_lengths = {}
#
# for word in words:
#     word_lengths[word] = len(word)
#
# print(word_lengths)