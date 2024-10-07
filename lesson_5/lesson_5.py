text_with_names = ("One sunny afternoon, Alex and Maria decided to go for a picnic in the park. They packed sandwiches "
                   "and drinks, excited to enjoy the beautiful weather. On their way, they met their friend John, who"
                   " was jogging nearby. “Hey, why don’t you join us?” Maria invited him. Soon, they found a nice spot"
                   " under a big tree and spread out their blanket. As they ate, they shared stories about their recent"
                   " adventures and laughed together, making it a day to remember.")

list_with_text = text_with_names.split()

list_of_names = []
for word in list_with_text:
    print(f'check {word}: {word.istitle()}')
    if word.istitle():
        list_of_names.append(word)

print(list_of_names)

for word in list_of_names:
    list_with_text.remove(word)

print(' '.join(list_with_text))


print(['A', 'B', 'C', 'B', 'b'].count('B'))