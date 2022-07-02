def choose_player(first_player, second_player):
    print(f"Who will be the first ({first_player}, {second_player}):")
    beginning_player = input()
    while beginning_player not in [first_player, second_player]:
        print(f"Choose between '{first_player}' and '{second_player}'")
        beginning_player = input()
    i = 0
    if beginning_player == second_player:
        i = 1
    return i

def is_positive_number(x):
    if not x.isdigit():
        print("The number of pencils should be numeric")
        return False
    x = int(x)
    if x == 0:
        print("The number of pencils should be positive")
        return False
    return True

def take_pencils(x, n):
    if x not in ['1', '2', '3']:
        print("Possible values: '1', '2' or '3'")
        return 0
    x = int(x)
    if x > n:
        print("Too many pencils were taken")
        return 0
    return x


first_player = "Alice"
second_player = "Bob"
print("How many pencils would you like to use:")
n = input()
while not is_positive_number(n):
    n = input()
n = int(n)
i = choose_player(first_player, second_player)

while n > 0:
    print("|" * n)
    if i % 2 == 0:
        print(f"{first_player}'s turn")
    else:
        print(f"{second_player}'s turn")

    x = take_pencils(input(), n)
    while not x:
        x = take_pencils(input(), n)
    n = n - x
    i += 1
if i % 2 == 0:
    print(f"{first_player} won!")
else:
    print(f"{second_player} won!")
