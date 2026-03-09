import random


def random_integer():
    print("step into random_integer")
    return random.randint(0, 20)


def is_even_number():
    # 0 - 9
    num = random_integer()
    print("num is", num)
    if num % 2 == 0:
        return True
    # else:
    #     return False

    return False


# def is_even_number(randint):
#     # 0 - 9
#     num = randint()
#     if num % 2 == 0:
#         return True

#     return False


if __name__ == "__main__":
    # print(is_even_number())

    print(is_even_number(random_integer))

    # def random_integer_stub_2():
    #     return 2

    # print(is_even_number(random_integer_stub_2))
