animal = input('Enter an animal: ')

try:
    with open(f"data/{animal}.csv") as animals:
        for line in animals.readlines()[1:]:
            arr = line.strip().split(', ')
            print(f"{arr[0]} is {arr[1]} year old {arr[2]}")
except Exception:
    print(f'Sorry we dont have {animal}')
