import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adwentures_of_tom_sawer)
print("\n")

# task 01 ==
# """ Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 1")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
print("\n")

# task 02 ==
# """ Замініть .... на пробіл """
print("Task 2")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
print("\n")

# task 03 ==
# Зробіть так, щоб у тексті було не більше одного пробілу між словами.
print("Task 3")
one_space_string = re.sub(r'\s+', " ", adwentures_of_tom_sawer)
print(one_space_string)
print("\n")

# task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h" """
print("Task 4")
count_h = len(re.findall("h", one_space_string))
print(f"Літера 'h' зутрічається {count_h} разів")
print("\n")

# task 05
# """ Виведіть, скільки слів у тексті починається з Великої літери? """
print("Task 5")
# Сидів розбирався, дивився конспект з заняття + гуглив, зробив ось такий варіант
words_with_big_first_letter = re.findall(r'[A-Z]', one_space_string)
count_big_letters = len(words_with_big_first_letter)
print("Великих букв в тексті -", count_big_letters, "\bшт")
print("\n")
print("Task 5 v2")
# Варіант другий, результат той самий, якщо чесно, не дуже зрозумів як краще Обвуглені
words_with_big_first_letter2 = re.findall(r'\b[A-Z][a-z]*', one_space_string)
count_big_letters_second = len(words_with_big_first_letter2)
print("Великих букв в тексті - ", count_big_letters_second)
print("\n")


# task 06
# """ Виведіть позицію, на якій слово Tom зустрічається вдруге """Обвуглені
print("Task 6")
second_tom_position = one_space_string.find("Tom", one_space_string.find("Tom") + 1)
print(f"Позиція другого слова 'Tom': {second_tom_position}")
print("\n")

# task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences """
print("Task 7")
adwentures_of_tom_sawer_sentences = one_space_string.split('.')
print(adwentures_of_tom_sawer_sentences)
print("\n")


# task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр. """
print("Task 8")
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_stripped = fourth_sentence.strip()
fourth_sentence_lower = fourth_sentence_stripped.lower()
print(f"Четверте речення в нижньому регістрі: {fourth_sentence_lower}")
print("\n")

# task 09
# """ Перевірте чи починається якесь речення з "By the time". """
print("Task 9")
#Варіант 1
found = re.search(r'\bBy the time\b', one_space_string)
if found:
    print("Є речення, яке починається з 'By the time'.")
else:
    print("Немає речень, які починаються з 'By the time'.")
print("\n")

#Варіант 2
sentences = one_space_string.split('. ')  # Розділяємо текст на речення
starts_with_by_the_time = any(sentence.startswith("By the time") for sentence in sentences)
if starts_with_by_the_time:
    print("Є речення, яке починається з 'By the time'.")
else:
    print("Немає речень, які починаються з 'By the time'.")

print("\n")

# task 10
# """ Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences. """
print("Task 10")

sentences = one_space_string.split('. ')
last_sentence = sentences[-1]
word_count_last_sentence = len(last_sentence.split())

print(f"Кількість слів в останньому реченні: {word_count_last_sentence}")