import random
input_list = []
print("H A N G M A N\n")
print("Type 'play' to play the game, 'exit' to quit:")
ini = input()
if ini == "play":
    word_list = ['python', 'java', 'kotlin', 'javascript']
    selected = random.choice(word_list)
    i = 8
    hidden = list('-' * len(selected))
    while i > 0:
        str1 = "".join(hidden)
        print()
        print(str1)
        if str1 == selected:
            print("You guessed the word!")
            print("You survived!")
            break

        inp = input("Input a letter: ")
        inp_low = inp.islower()
        inp_list = list(inp)
        if len(inp_list) > 1:
            print("You should input a single letter")
        else:
            if inp_low is True:
                if inp in input_list:
                    print("You already typed this letter")
                    input_list.append(inp)
                elif inp not in input_list:
                    input_list.append(inp)
                    if inp in selected:
                        for j in range(len(selected)):
                            if inp in hidden[j]:
                                print("No improvements")
                                # i = i - 1
                                break
                            elif inp == selected[j]:
                                hidden[j] = inp
                    else:
                        print("No such letter in the word")
                        i = i - 1
            else:
                print("It is not an ASCII lowercase letter")
    else:
        print("You are hanged!")
elif ini == "exit":
    print()