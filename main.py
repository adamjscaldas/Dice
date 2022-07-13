import random
import easygui


# Creates an easygui box to choose which dice will be used
def select_dice() -> str:
    return easygui.buttonbox(msg="Qual dado você quer rodar?\n"
                                 "Which dice do you want to roll?",
                             choices=["d3", "d4", "d6", "d8", "d10", "d12", "d20", "d100"],
                             title="ESCOLHER DADO / CHOOSE DICE")


def return_dice_value(inputed_value: str) -> dict:
    inputed_value = inputed_value.replace("d", "")
    return {str(i + 1): 0 for i in range(int(inputed_value))}


def return_dice_list(inputed_value: str) -> list:
    inputed_value = inputed_value.replace("d", "")
    return [str(i + 1) for i in range(int(inputed_value))]


# Removes all unwanted characters from the cycles input
def clean_number(number_to_clean: str) -> str:
    items_removed = """ ,.+-=()_;:|\\/´`~^[]{}*&¨%$#@!?'"><
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÇç"""
    cleaned_number = number_to_clean
    for x in range(len(items_removed)):
        cleaned_number = cleaned_number.replace(items_removed[x], '')
    return cleaned_number


# Returns a str that will be used to print an easygui box showing how many times each number appeared
def roll_dice(cycles: int, random_value: list, chosen_list: list, chosen_dict: dict) -> str:
    sequence = cycling(cycles=cycles, random_value_used=random_value, dice_used=chosen_list)
    print(sequence)
    created_dict = create_dict(dice_list_used=chosen_list, chosen_dict_to_use=chosen_dict, sequence=sequence)
    return check_appearance(dice_dict_used=created_dict)


# "Rolls the dice" and defines the sequence that the numbers appeared
def cycling(cycles: int, random_value_used: list, dice_used: list) -> list:
    sequence_returned = []
    for y in range(cycles):
        random.shuffle(random_value_used)
        value_to_append = random.choice(dice_used)
        sequence_returned.append(value_to_append)
    return sequence_returned


# Creates the dict that will be used to calculate how many times each number appeared
def create_dict(dice_list_used: list, chosen_dict_to_use: dict, sequence: list) -> dict:
    for z in range(len(dice_list_used)):
        dice_value = dice_list_used[z]
        counting = 0
        while dice_value in sequence:
            sequence.remove(dice_value)
            counting += 1
        if counting > 0:
            up_dict = {str(dice_value): counting}
            chosen_dict_to_use.update(up_dict)
        else:
            pass
    return chosen_dict_to_use


# Uses the dict created with "create_dict()" to check how many times each number appeared
def check_appearance(dice_dict_used: dict) -> str:
    string_returned = ''

    for key in dict(dice_dict_used):
        key_value = dice_dict_used.get(key)
        if key_value != 0:
            string_returned += f""""{key}" was rolled {key_value} times\n"""
    return string_returned


# Code structure
def game() -> bool:
    choose_dice = select_dice()
    if choose_dice is not None:
        cycles = easygui.enterbox(msg=f"Quantas vezes o {choose_dice} será rodado?\n"
                                      f"How many times will the {choose_dice} be rolled?",
                                  title="CICLOS / CYCLES")
        while True:
            if cycles is not None:
                try:
                    cycles = int(clean_number(cycles))
                    break
                except ValueError:
                    cycles = easygui.enterbox(msg=f"Quantas vezes o {choose_dice} será rodado?\n"
                                                  f"How many times will the {choose_dice} be rolled?",
                                              title="CICLOS / CYCLES")
                except AttributeError:
                    cycles = easygui.enterbox(msg=f"Quantas vezes o {choose_dice} será rodado?\n"
                                                  f"How many times will the {choose_dice} be rolled?",
                                              title="CICLOS / CYCLES")
                finally:
                    pass
            else:
                return False

        chosen_dict = return_dice_value(inputed_value=choose_dice)
        chosen_list = return_dice_list(inputed_value=choose_dice)

        random_value = [chosen_list]

        numbers_ordered = roll_dice(cycles=cycles,
                                    random_value=random_value,
                                    chosen_list=chosen_list,
                                    chosen_dict=chosen_dict)

        easygui.msgbox(title="Resultado / Result",
                       msg=numbers_ordered)
        repeat = easygui.buttonbox(title="Repetir? / Repeat?",
                                   msg="Rodar o dado novamente?\nRoll the dice again?",
                                   choices=["Sim / Yes", "Não / No"])
        if repeat == "Não / No":
            return False
        elif repeat == "Sim / Yes":
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    while True:
        play = game()
        if play is True:
            pass
        else:
            break
