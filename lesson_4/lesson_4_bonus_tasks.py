# На вхід функції потрапляють строки лог-файлу виду:
# 2023-04-27 15:30:45 - TestCase: login_successful
# 2023-04-27 15:35:12 - TestCase: invalid_password
# Після строки 'TestCase: ' іде назва тесту.
# Зробити так, щоб функця виводила лише назву тесту.
# Увага! Замість print у функії використовуйте return.
# Тести
# Щоб здати задачу усі тести повинні бути пройдені.
# Позитивна перевірка строкою
# Перевірка строкою
# "2023-04-27 15:30:45 - TestCase: login_successful"
# Негативна перевірка строкою
# Перевірка строкою
# "2023-04-27 15:30:45 - test PASS"

log_1 = "2023-04-tewt: 27 15: 30:45 - TestCase: login_successful"
log_2 = "2023-04-27 15:35 : 12 - TestCase: invalid_password"

def solution(test_string):
    result = test_string.split('TestCase: ')[1]
    print(result)
    return result

solution("2023-04-27 15:30:45 - TestCase: login_successful")
solution("2023-04-27 15:35:12 - TestCase: invalid_password")


# sent = ('2023-04-27 15:35:12 - TestCase: invalid_password')
# test_case_index = sent.find('TestCase')
# result = sent[test_case_index:]


# print(result)
# print('\n')
# print(f'first phrase = {my_phrase[0]}')
# print(f'second phrase = {my_phrase[1]}')
# print(f'third phrase = {my_phrase[2]}')