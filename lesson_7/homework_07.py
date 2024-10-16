# task 1
# Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)


# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
#   Написати функцію, яка обчислює суму двох чисел.
def sum_of_two_nums(num1, num2):
    result = num1 + num2
    return result


print(sum_of_two_nums(60, 19))

# task 3
# Написати функцію, яка розрахує середнє арифметичне списку чисел.

# v.1
list_of_nums = list()


def avereg(list_of_nums):
    sum_result = sum(list_of_nums)
    sum_devide_by_count = sum_result / len(list_of_nums)
    return sum_devide_by_count


print(avereg([10, 20, 30]))


# v.2 офігів як поняв шо можна це написати по суті в 1 рядок)))
def avr(numbers):
    return sum(numbers) / len((numbers))


print(avr([10, 20, 30]))


# task 4
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# v.1
input_value = str


def str_backward(input_value):
    input_value = input('Please enter your text: ')
    return print(input_value[::-1])


str_backward(input_value)


# v.2
def str_backward_2():
    input_value_2 = input('Plz enter the text: ')
    print(input_value_2[::-1])


str_backward_2()


# task 5
# Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def find_longest_word():
    words = input("Please enter a list of words separated by spaces: ").split()
    if not words:
        return None  # Якщо список порожній
    longest_word = max(words, key=len)
    return longest_word

# Виклик функції
print(find_longest_word())


# task 6
# Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка


def find_substring(str1, str2):
    index = str1.find(str2)
    return index if index != -1 else -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# task 7
def calculate_total_trees(apple_trees):
    """
    Обчислює загальну кількість дерев у саду, де відомо кількість яблунь.
    Груш більше на 5, а слив менше на 2.

    :param apple_trees: Кількість яблунь.
    :return: Загальна кількість дерев.
    """
    pear_trees = apple_trees + 5
    plum_trees = apple_trees - 2
    total_trees = apple_trees + pear_trees + plum_trees
    return total_trees


# Приклад використання
print(calculate_total_trees(4))

# task 8ʼ

def calculate_evening_temp(morning_temp):
    """
    Обчислює температуру повітря ввечері за умови відомої ранкової температури,
    пониження на 10 градусів після обіду і підвищення на 4 градуси до вечора.

    :param morning_temp: Температура зранку.
    :return: Температура ввечері.
    """
    after_lunch_temp = morning_temp - 10
    evening_temp = after_lunch_temp + 4
    return evening_temp


# Приклад використання
print(calculate_evening_temp(5))

# task 9

def calculate_kids_present(boys, girls_doesnt_cum):
    """
    Обчислює кількість дітей, присутніх сьогодні в театральному гуртку,
    де захворів 1 хлопець і не прийшли 2 дівчинки.

    :param boys: Кількість хлопців.
    :param girls_doesnt_cum: Кількість відсутніх дівчат.
    :return: Кількість присутніх дітей.
    """
    girls = boys // 2
    boys_sick = boys - 1
    present_girls = girls - girls_doesnt_cum
    total_present_kids = boys_sick + present_girls
    return total_present_kids


# Приклад використання
print(calculate_kids_present(24, 2))


# task 10

def calculate_books_cost(first_book_price):
    """
    Обчислює загальну вартість трьох книжок, де відома ціна першої книги,
    друга дорожча на 2 грн, а третя — половина вартості першої і другої разом.

    :param first_book_price: Вартість першої книжки.
    :return: Загальна вартість трьох книжок.
    """
    second_book_price = first_book_price + 2
    third_book_price = (first_book_price / 2) + (second_book_price / 2)
    total_cost = first_book_price + second_book_price + third_book_price
    return total_cost


# Приклад використання
print(calculate_books_cost(8))

# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
