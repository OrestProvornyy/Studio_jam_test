while True:
    word = input("Enter a word with letter 'h' or 'H': ")
    if 'h' in word.lower():
        print("Great! You win")
        break
    else:
        print("You haven't write a letter 'h' or 'H' ")
