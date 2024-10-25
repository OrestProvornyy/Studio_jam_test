
# Функція 1: Обчислення кількості дерев у саду
def calculate_total_trees(apple_trees):
    pear_trees = apple_trees + 5
    plum_trees = apple_trees - 2
    total_trees = apple_trees + pear_trees + plum_trees
    return total_trees


# --------------------------------------------------------------------------
# Функція 2: Обчислення загальної площі морів
def calculate_total_sea_area(blacksea_square, azovsea_square):
    return blacksea_square + azovsea_square


# --------------------------------------------------------------------------
# Функція 3: Фільтрація автомобілів
def find_cars(car_data, search_criteria):
    filtered_cars = sorted(
        [(car, details) for car, details in car_data.items()
         if details[1] >= search_criteria[0] and  # Рік >=
         details[2] >= search_criteria[1] and  # Об'єм двигуна >=
         details[4] <= search_criteria[2]],  # Ціна <=
        key=lambda x: x[1][4]  # Сортування за ціною
    )
    return filtered_cars[:5]


# --------------------------------------------------------------------------
# Функція 4: Обробка списку людей (обмін і перевірка віку)
def swap_and_check_age(people_records, swap_indices, age_indices, age_threshold):
    people_records[swap_indices[0]], people_records[swap_indices[1]] = people_records[swap_indices[1]], people_records[swap_indices[0]]
    age_check = all(people_records[i][2] >= age_threshold for i in age_indices)
    return people_records, age_check


# --------------------------------------------------------------------------
# Функція 5: Підрахунок суми чисел у рядку
def sum_of_numbers_in_string(string):
    try:
        numbers = string.split(',')
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"
