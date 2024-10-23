import unittest
from homework_09 import calculate_total_trees, calculate_total_sea_area, find_cars, swap_and_check_age, sum_of_numbers_in_string



class TestHomeworks(unittest.TestCase):

    # --------------------------------------------------------------------------
    # Тести для функції calculate_total_trees
    def test_calculate_total_trees(self):
        self.assertEqual(calculate_total_trees(4), 15)
        self.assertEqual(calculate_total_trees(10), 33)
        self.assertEqual(calculate_total_trees(0), 3)


    # --------------------------------------------------------------------------
    # Тести для функції calculate_total_sea_area
    def test_calculate_total_sea_area(self):
        self.assertEqual(calculate_total_sea_area(436402, 37800), 474202)
        self.assertEqual(calculate_total_sea_area(500000, 30000), 530000)


    # --------------------------------------------------------------------------
    # Тести для функції find_cars
    def test_find_cars(self):
        car_data = {
            'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
            'Audi': ('black', 2020, 2.0, 'sedan', 55000),
            'BMW': ('white', 2018, 3.0, 'suv', 70000)
        }
        search_criteria = (2015, 1.6, 60000)
        result = find_cars(car_data, search_criteria)
        self.assertEqual(len(result), 2)  # Знайдено 2 авто
        self.assertEqual(result[0][0], 'Mercedes')  # Перше авто Mercedes
        self.assertEqual(result[1][0], 'Audi')  # Друге авто Audi

    # --------------------------------------------------------------------------
    # Тести для функції swap_and_check_age
    def test_swap_and_check_age(self):
        people_records = [
            ('John', 'Doe', 28, 'Engineer', 'New York'),
            ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
            ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
            ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
            ('Michael', 'Brown', 22, 'Student', 'Seattle'),
            ('Sophia', 'Davis', 40, 'Lawyer', 'Boston')
        ]
        swap_indices = (1, 5)
        age_indices = [1, 2, 5]  # Змінив на правильні індекси
        result, age_check = swap_and_check_age(people_records, swap_indices, age_indices, 30)
        self.assertTrue(age_check)
        self.assertEqual(result[1][0], 'Sophia')
        self.assertEqual(result[5][0], 'Alice')

    # --------------------------------------------------------------------------
    # Тести для функції sum_of_numbers_in_string
    def test_sum_of_numbers_in_string(self):
        self.assertEqual(sum_of_numbers_in_string("1,2,3,4"), 10)
        self.assertEqual(sum_of_numbers_in_string("10,20,30,40"), 100)
        self.assertEqual(sum_of_numbers_in_string("qwerty"), "Не можу це зробити!")


if __name__ == '__main__':
    unittest.main()
