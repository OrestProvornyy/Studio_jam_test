input_str = input("Enter your text please: ")
uniq_char = set(input_str)
if len(uniq_char) > 10:
    print(True)
else:
    print(False)
