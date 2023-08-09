try:
    import os
    from colorama import Fore
    from random import randint, choice
    from math import floor

    answers = {}

    def CLInput(type, prompt):
        def validate (type, input):
            try:
                type(input)
                return True
            except ValueError:
                return False
        answer = input(prompt)
        if validate(type, answer):
            return type(answer)
        else:
            print("\n"*2)
            print(Fore.RED + "Invalid input!" + Fore.RESET)
            print("Please enter a valid " + type.__name__ + "!")
            print(Fore.BLACK + "-"*15 + Fore.RESET+ "\n"*2 )
            return CLInput(type, prompt)
        
    print(Fore.GREEN + "Welcome to the questions!" + Fore.RESET)
    questions = CLInput(int, "How many questions? ")

    for q in range(1, questions+1):
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        operator = choice(["+", "-"])
        os.system('cls' if os.name == 'nt' else 'clear')
        question = f"{num1 if num1>num2 else num2} {operator} {num1 if num1<num2 else num2}"
        answers[question] = CLInput(int, f"{q}. {Fore.WHITE}{question}{Fore.RESET} \n{Fore.YELLOW}> {Fore.RESET}")

    print(Fore.GREEN + "Thanks for answering the questions!" + Fore.RESET)
    correct = 0
    total = questions
    for i, q in enumerate(answers):
        
        if eval(q) == int(answers[q]):
            correct += 1
            print(f"{i+1}. {q} = {Fore.GREEN + str(answers[q]) + Fore.RESET}")
        else:
            print(f"{i+1}. {q} = {Fore.RED + str(answers[q]) + Fore.RESET}")
    score = floor(correct/total*100)
    if score >= 85:
        print(f"{Fore.GREEN + str(score) + Fore.RESET}%")
    elif score >= 60:
        print(f"{Fore.YELLOW + str(score) + Fore.RESET}%")
    else:
        print(f"{Fore.RED + str(score) + Fore.RESET}%")

except KeyboardInterrupt:
    print("\n"*2)
    print(Fore.RED + "Exiting..." + Fore.RESET)
    exit()