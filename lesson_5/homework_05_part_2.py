# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1
my_record = ('Orest', 'Provornyy', 29, 'QA Engineer', 'Lviv')
people_records.insert(0, my_record)

# 2
people_records[1], people_records[5] = people_records[5], people_records[1]

# Виводимо результат після обміну
print("Список після обміну елементів з індексами 1 і 5:")
for person in people_records:
    print(person)

# 3
indices_to_check = [6, 10, 13]
age_check = True

for i in indices_to_check:
    if people_records[i][2] < 30:
        age_check = False
        break


# Виводимо
print(people_records[6])
print("\nЧи всі люди з індексами 6, 10, 13 мають вік ≥ 30?:", age_check)

# Перевірка чи дійсно має бути False
person = people_records[6]
print(f"Ім'я: {person[0]}, Прізвище: {person[1]}, Вік: {person[2]}, Професія: {person[3]}, Місто: {person[4]}")

person = people_records[10]
print(f"Ім'я: {person[0]}, Прізвище: {person[1]}, Вік: {person[2]}, Професія: {person[3]}, Місто: {person[4]}")

person = people_records[13]
print(f"Ім'я: {person[0]}, Прізвище: {person[1]}, Вік: {person[2]}, Професія: {person[3]}, Місто: {person[4]}")