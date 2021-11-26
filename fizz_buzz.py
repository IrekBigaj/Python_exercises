# This program is child game Fizz Buzz

for numerek in range(1, 101):
    if numerek % 3 == 0 and numerek % 5 == 0:
        print("FizzBuzz")
    elif numerek % 5 == 0:
        print("Buzz")
    elif numerek % 3 == 0:
        print("Fizz")
    else:
        print(numerek)
