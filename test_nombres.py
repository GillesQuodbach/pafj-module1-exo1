import sys


# https://github.com/GillesQuodbach/pafj-module1-exo1.git

def negative_or_positive(input_number):
    if input_number > 0:
        return "positif"
    elif input_number < 0:
        return "négatif"
    else:
        return "nul"


def odd_or_even(input_number):
    if input_number % 2 == 0:
        return "pair"
    else:
        return "impair"


if len(sys.argv) > 1:
    # Question 3
    try:
        # Question 1
        numbers = list(map(int, sys.argv[1:]))
        # Question 2
        for number in numbers:
            print(f"{number}: {negative_or_positive(number)} et {odd_or_even(number)}")
    except ValueError:
        print("Votre liste n'est pas valide, erreur de saisie !!!")





