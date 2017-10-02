def Module():
    a = []
    for x in range(10):
        number = int(input("Please input data here"))
        a.append(number)
    count = [number % 42 for number in a]
    print(len(set(count)))

Module()
