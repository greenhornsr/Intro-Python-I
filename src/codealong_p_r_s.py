#### INITIAL PASS
# import random


# #REPL
# wins = 0
# losses = 0
# ties = 0

# choices = ["r", "p", "s"]

# #LOOP
# while True: 
#     #READ
#     cmd = input("->")
#     cpu_move = random.choice(choices)
#     #EVAL
#     if cmd == "r":
#         if cpu_move == "r":
#             print("tie")
#             ties += 1
#         elif cpu_move == "p":
#             print("Lose")
#             losses += 1
#         elif cpu_move == "s":
#             print("win")
#             wins += 1
#     if cmd == "p":
#         if cpu_move == "p":
#             print("tie")
#             ties += 1
#         elif cpu_move == "s":
#             print("Lose")
#             losses += 1
#         elif cpu_move == "r":
#             print("win")
#             wins += 1
#     if cmd == "s":
#         if cpu_move == "s":
#             print("tie")
#             ties += 1
#         elif cpu_move == "r":
#             print("Lose")
#             losses += 1
#         elif cpu_move == "p":
#             print("win")
#             wins += 1
#     if cmd == "q":
#         #quit
#         print("goodbye")
#         break
#     else:
#         print("I did not recognize that command.")
#     #PRINT
#     print(f"Score: {wins} / {losses} / {ties}")



####  ************    REFACTORED    *****************
import random
def process_choices(player_move, cpu_move):
    '''
    Assume that both moves are r, p or s
    '''
    # This contains all winning pairs
    wins = {"r": "s", "p": "r", "s": "p"}
    if player_move == cpu_move:
        # tie
        print("Tie")
        return 0
    # If we match a winning pair, user wins
    elif wins[player_move] == cpu_move:
        # win
        print("Win!")
        return 1
    else:
        # lose
        print("You did not win")
        return -1

# REPL
wins = 0
losses = 0
ties = 0

choices = ["r", "p", "s"]

# LOOP
while True:
    # READ
    cmd = input("-> ")
    cpu_move = random.choice(choices)
    print(f"CPU picks {cpu_move}")
    # EVAL
    if cmd in choices:
        results = process_choices(cmd, cpu_move)
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        else:
            losses += 1
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        break
    else:
        print("I did not recognize that command")
    # PRINT
    print(f"Score: {wins} / {losses} / {ties}")
