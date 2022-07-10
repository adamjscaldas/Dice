import random

dice = ['1', '2', '3', '4',
        '5', '6', '7', '8',
        '9', '10', '11', '12',
        '13', '14', '15', '16',
        '17', '18', '19', '20']

random_value = [dice]
sequence = []
repetitions = {'1': 0, '2': 0, '3': 0, '4': 0,
               '5': 0, '6': 0, '7': 0, '8': 0,
               '9': 0, '10': 0, '11': 0, '12': 0,
               '13': 0, '14': 0, '15': 0, '16': 0,
               '17': 0, '18': 0, '19': 0, '20': 0
               }
count = 0

# Quantidade de vezes que o Dado vai rodar
cycles = 50
for y in range(cycles):
    random.shuffle(random_value)
    value_to_append = random.choice(dice)
    sequence.append(value_to_append)

print(f"sequence = {sequence}")

# Cria um dict com a quantidade de vezes que cada item apareceu
for z in range(len(dice)):
    dice_value = dice[z]
    count = 0
    while dice_value in sequence:
        sequence.remove(dice_value)
        count += 1
    if count > 0:
        up_dict = {str(dice_value): count}
        repetitions.update(up_dict)
    else:
        pass

for key in dict(repetitions):
    key_value = repetitions.get(key)
    if key_value != 0:
        if key_value == 1:
            print(f"{key} appeared {key_value} times.")
        else:
            print(f"{key} appeared {key_value} times.")
