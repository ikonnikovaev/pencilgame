first_player = "Alice"
second_player = "Bob"
print("How many pencils would you like to use:")
n = int(input())
print(f"Who will be the first ({first_player}, {second_player}):")
beginning_player = input()
i = 0
if beginning_player == second_player:
    i = 1

while n > 0:
    print("|" * n)
    if i % 2 == 0:
        print(f"{first_player}'s turn")
    else:
        print(f"{second_player}'s turn")
    x = int(input())
    n = max(0, n - x)
    i += 1
