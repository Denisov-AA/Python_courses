import os


def spaces_to_tabs(string: str):
    return string.replace("    ", "\t")


def tabs_to_spaces(string: str):
    return string.replace("\t", "    ")


# Выбираем, что на что хотим менять
action = tabs_to_spaces

# При проверке обратить внимание на Working directory
input_file = open("for_task4.txt", "r", encoding="utf-8")
output_file = open("result.txt", "w")

for line in input_file:
    output_file.write(action(line))

input_file.close()
output_file.close()
