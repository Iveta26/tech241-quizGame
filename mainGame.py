#what spongebob character are you?


print("Hi! I want you to think of a spongebob character and answer questions, \n see if I can guess which one you picked")



def quizGame():
    flag = True
    characters = {
        "Spongebob": 0,
        "Mr Krabs": 0,
        "Squidward": 0,
        "Patrick Star": 0,
        "Plankton": 0
    }
    theCharacter = ""
    while flag:
        inp = input("what colour are you? \n")
        if inp.lower() == "yellow":
            characters["Spongebob"] += 1
        elif inp.lower() == "red":
            characters["Mr Krabs"] += 1
        elif inp.lower() == "green":
            characters["Squidward"] += 1
            characters["Plankton"] += 1
        elif inp.lower() == "pink":
            characters["Patrick Star"] += 1
        else:
            print("Don't know this colour :(((")
            continue
        if input("are you overly happy? \n Y/N \n").lower() == "y":
            characters["Spongebob"] += 1
        if input("Are you very VERY small? \n Y/N \n").lower() == "y":
            characters["Plankton"] += 1
        if input("Do you wear the same pair of floral shorts every day? \n Y/N \n").lower() == "y":
            characters["Patrick Star"] += + 1
        if input("Would you sell your soul for 1p? \n Y/N \n").lower() == "y":
            characters["Mr Krabs"] += 1
        if input("Are you very grumpy and your go to outfit is a t-shirt + no pants? \n Y/N \n").lower() == "y":
            characters["Squidward"] += 1
        flag = False


    for key, val in characters.items():
        if val == 2:
            print(f"You are {key}! \n")
            theCharacter = key

    print("Do you want to play again? \n Y/N")
    playAgain = input().lower()
    if playAgain == "y":
        quizGame()
    else:
        print(f"Goodbye, {theCharacter}!")

quizGame()
