alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n"That depends'
                       ' a good deal on where you want to get to," said'
                       ' the Cat.\n"I don\')t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," '
                       'said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure '
                       'to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)



    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі

# task 04
task_four_text = ("\nПлоща Чорного моря становить 436 402 км2, а площа Азовського моря становить 37 800 км2. Яку площу займають "
             "Чорне та Азов-ське моря разом?")
blacksea_square = 436402
azovsea_square = 37800
avov_and_black_total_square = blacksea_square + azovsea_square
print("\nПлоща Чорного моря становить",blacksea_square,"\b км2, а площа Азовського моря"
      " становить", azovsea_square, "\nЯк би ми обєднали ці два моря то вони б зайняли "
      "аж цілих", avov_and_black_total_square,"\b км2")
#Або так але перший варіант мені більше подобається
print(f"\nПлоща Чорного моря становить {blacksea_square} км², а площа Азовського моря становить {azovsea_square} км²."
      f"\nЯкби ми об'єднали ці два моря, то вони б зайняли аж цілих {avov_and_black_total_square} км².")

# task 05
print("\n")
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.

total_items = 375291
first_and_second_items = 250449
second_and_third_items = 222950

# Знаходимо кількість товарів на кожному складі
second_items = first_and_second_items + second_and_third_items - total_items
first_items = first_and_second_items - second_items
third_items = second_and_third_items - second_items

print(f"На першому складі знаходиться {first_items} товарів.")
print(f"На другому складі знаходиться {second_items} товарів.")
print(f"На третьому складі знаходиться {third_items} товарів.")



# task 06
#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.


months = 18
monthly_payment = 1179  # грн
computer_cost = months * monthly_payment
print("\nВартість комп'ютера становить", computer_cost, "грн.\n")

# task 07
# Остачі від ділення
remainder_a = 8019 % 8
remainder_b = 9907 % 9
remainder_c = 2789 % 5
remainder_d = 7248 % 6
remainder_e = 7128 % 5
remainder_f = 19224 % 9

print("Остача від ділення 8019 на 8:", remainder_a)
print("Остача від ділення 9907 на 9:", remainder_b)
print("Остача від ділення 2789 на 5:", remainder_c)
print("Остача від ділення 7248 на 6:", remainder_d)
print("Остача від ділення 7128 на 5:", remainder_e)
print("Остача від ділення 19224 на 9:", remainder_f)

# task 08
# Розрахунок вартості замовлення
pizza_large_count = 4
pizza_large_price = 274
pizza_medium_count = 2
pizza_medium_price = 218
juice_count = 4
juice_price = 35
cake_count = 1
cake_price = 350
water_count = 3
water_price = 21

total_cost = (pizza_large_count * pizza_large_price +
              pizza_medium_count * pizza_medium_price +
              juice_count * juice_price +
              cake_count * cake_price +
              water_count * water_price)

print("\nЗагальна вартість замовлення:", total_cost, "грн.\n")


# task 09
# Кількість сторінок для фотоальбому
total_photos = 232
photos_per_page = 8
pages_needed = (total_photos + photos_per_page - 1) // photos_per_page

print("\nІгорю знадобиться", pages_needed, "сторінок для всіх фотографій.\n")


# task 10
# Розрахунок бензину та кількості заправок
distance = 1600  # км
fuel_per_100km = 9  # літрів
tank_capacity = 48  # літрів

total_fuel_needed = (distance / 100) * fuel_per_100km
refuels_needed = (total_fuel_needed + tank_capacity - 1) // tank_capacity

print("\nЗагалом знадобиться", total_fuel_needed, "літрів бензину.")
print("Сім'ї доведеться заправитися щонайменше", int(refuels_needed), "разів.")

