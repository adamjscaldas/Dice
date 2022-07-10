import random


def cycling(cycles: int, random_value_used: list, dice_used: list) -> list:
    sequence_returned = []
    for y in range(cycles):
        random.shuffle(random_value_used)
        value_to_append = random.choice(dice_used)
        sequence_returned.append(value_to_append)
    print(f"The sequence of dices rolled is: {sequence_returned}", end="\n\n")
    return sequence_returned


def create_dict(dice_list_used: list) -> dict:
    for z in range(len(dice_list_used)):
        dice_value = dice_list_used[z]
        count = 0
        while dice_value in sequence:
            sequence.remove(dice_value)
            count += 1
        if count > 0:
            up_dict = {str(dice_value): count}
            repetitions.update(up_dict)
        else:
            pass
    return repetitions


def check_appearance(dice_dict_used: dict) -> None:
    print(f"""This was a cycle of {cycles} rolls.""", end="\n\n")
    for key in dict(dice_dict_used):
        key_value = dice_dict_used.get(key)
        if key_value != 0:
            print(f""""{key}" was rolled {key_value} times""")
    return None


d3_dict = {
    '1': 0, '2': 0, '3': 0
}
d3_list = [
    '1', '2', '3'
]

d6_list = [
    '1', '2', '3',
    '4', '5', '6'
]
d6_dict = {
    '1': 0, '2': 0, '3': 0,
    '4': 0, '5': 0, '6': 0
}

d10_list = [
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '10'
]
d10_dict = {
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
    '6': 0, '7': 0, '8': 0, '9': 0, '10': 0
}

d20_list = [
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12',
    '13', '14', '15', '16',
    '17', '18', '19', '20'
]
d20_dict = {
    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
    '6': 0, '7': 0, '8': 0, '9': 0, '10': 0,
    '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
    '16': 0, '17': 0, '18': 0, '19': 0, '20': 0
}

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

# dice e repetitions precisam ter o mesmo dado
# dice and repetitions need to use the same dice
dice = d20_list  # dice precisa ser list / dice needs to be a list
repetitions = d20_dict  # repetitions precisa ser dict / repetitions needs to be a dict


random_value = [dice]
count = 0


# Essa variável define quantas vezes o dado vai ser rolado
# This variable defines how many times the dice will be rolled
cycles = 20
sequence = cycling(cycles=cycles, random_value_used=random_value, dice_used=dice)

# Cria um dict com a quantidade de vezes que cada item apareceu
# Creates a dict that saves how many times each number was rolled
created_dict = create_dict(dice_list_used=dice)

# Faz a checagem de quantas vezes cada número apareceu
# Check how many times each number appeared
check_appearance(dice_dict_used=repetitions)
