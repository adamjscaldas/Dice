import random
import easygui


# Creates an easygui box to choose which dice will be used
def select_dice() -> str:
    return easygui.buttonbox(msg="Qual dado você quer rodar?\n"
                                 "Which dice do you want to roll?",
                             choices=["d3", "d6", "d10", "d20", "d100"],
                             title="ESCOLHER DADO / CHOOSE DICE")


# Removes all unwanted characters from the cycles input
def clean_number(number_to_clean: str) -> str:
    items_removed = """ ,.+-=()_;:|\\/´`~^[]{}*&¨%$#@!?'"><
    AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÇç"""
    cleaned_number = number_to_clean
    for x in range(len(items_removed)):
        cleaned_number = cleaned_number.replace(items_removed[x], '')
    return cleaned_number


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


d3_list = [
    '1', '2', '3'
]
d6_list = [
    '1', '2', '3',
    '4', '5', '6'
]
d10_list = [
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '10'
]
d20_list = [
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12',
    '13', '14', '15', '16',
    '17', '18', '19', '20'
]
d100_list = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
    '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
    '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
    '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
    '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
    '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'
]
d3_dict = {
    '1': 0, '2': 0, '3': 0
}
d6_dict = {
    '1': 0, '2': 0, '3': 0,
    '4': 0, '5': 0, '6': 0
}
d10_dict = {
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
    '6': 0, '7': 0, '8': 0, '9': 0, '10': 0
}
d20_dict = {
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
    '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
    '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
    '16': 0, '17': 0, '18': 0, '19': 0, '20': 0
}
d100_dict = {
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
    '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0,
    '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0,
    '31': 0, '32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '40': 0,
    '41': 0, '42': 0, '43': 0, '44': 0, '45': 0, '46': 0, '47': 0, '48': 0, '49': 0, '50': 0,
    '51': 0, '52': 0, '53': 0, '54': 0, '55': 0, '56': 0, '57': 0, '58': 0, '59': 0, '60': 0,
    '61': 0, '62': 0, '63': 0, '64': 0, '65': 0, '66': 0, '67': 0, '68': 0, '69': 0, '70': 0,
    '71': 0, '72': 0, '73': 0, '74': 0, '75': 0, '76': 0, '77': 0, '78': 0, '79': 0, '80': 0,
    '81': 0, '82': 0, '83': 0, '84': 0, '85': 0, '86': 0, '87': 0, '88': 0, '89': 0, '90': 0,
    '91': 0, '92': 0, '93': 0, '94': 0, '95': 0, '96': 0, '97': 0, '98': 0, '99': 0, '100': 0
}


# ["d3", "d6", "d10", "d20", "d100"]
def select_dice_dict(chosen_dice: str) -> dict:
    while True:
        if chosen_dice == "d3":
            return d3_dict
        elif chosen_dice == "d6":
            return d6_dict
        elif chosen_dice == "d10":
            return d10_dict
        elif chosen_dice == "d20":
            return d20_dict
        elif chosen_dice == "d100":
            return d100_dict
        else:
            chosen_dice = select_dice()


def select_dice_list(chosen_dice_dict: dict) -> list:
    while True:
        if chosen_dice_dict == d3_dict:
            return d3_list
        elif chosen_dice_dict == d6_dict:
            return d6_list
        elif chosen_dice_dict == d10_dict:
            return d10_list
        elif chosen_dice_dict == d20_dict:
            return d20_list
        elif chosen_dice_dict == d100_dict:
            return d100_list
        else:
            chosen_dice_dict = select_dice()


def roll_dice(cycles: int, random_value: list, chosen_list: list, chosen_dict: dict):
    # Roda o dado e retorna uma lista com a ordem em que os números apareceram
    # Rolls the dice and returns a list with the order each number appeared
    sequence = cycling(cycles=cycles, random_value_used=random_value, dice_used=chosen_list)

    # Cria um dict com a quantidade de vezes que cada item apareceu
    # Creates a dict that saves how many times each number was rolled
    created_dict = create_dict(dice_list_used=chosen_list, chosen_dict_to_use=chosen_dict, sequence=sequence)

    # Faz a checagem de quantas vezes cada número apareceu
    # Check how many times each number appeared
    return check_appearance(dice_dict_used=created_dict)


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

        chosen_dict = select_dice_dict(chosen_dice=choose_dice)
        chosen_list = select_dice_list(chosen_dice_dict=chosen_dict)

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
