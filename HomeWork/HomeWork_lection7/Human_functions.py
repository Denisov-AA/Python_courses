from Human_class import Human
import pickle

number_of_humans = input("How much humans you wanna create? \n")


def create_serialise(number):
    print("Humans to serialise: \n")
    data = []
    for i in range(int(number)):
        human = Human()
        data.append(human)
    with open("human.data", "wb") as file:
        pickle.dump(data, file)


def read_deserialise():
    print("Humans from human.data\n")

    with open("human.data", "rb") as file:
        data = pickle.load(file)
    cnt = 1
    for item in data:
        item.introduce()
        cnt += 1


create_serialise(number_of_humans)

read_deserialise()
