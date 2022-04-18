# --> Hangman Game - GUESS MY WORD

def hangmam(word):
    wrong = 0
    stages = ["",
              "___________________         ",
              "|                           ",
              "|                  |        ",
              "|                  O        ",
              "|                / | \      ",
              "|                 / \       ",
              "|                           "
            ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to execution!")
    while wrong < len(stages) - 1:
        print('\n')
        msg = "Enter a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1 
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win! The word was guessed: ")
            print(" ".join(board))
            win = True
            break 
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! The word was guessed: {}.".format(word))

hangmam("max")


