# targil 1
# def sort_prices(list_of_tuples):
#     list_of_tuples.sort(key=min)
#     list_of_tuples.reverse()
#     return list_of_tuples
#     # targil 2
#     # def new_dict = {"first_name":"Mariah","last_name":"Carey","birth_date":"27.03.1970","hobbies":"[Sing, Compose, Act]"}
#     # print(sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]))

# targil 5
import functools
def double_letter(my_str):
    my_str = ((functools.reduce(split(), my_str))*2).join()
    print(my_str)


if __name__ == '__main__':
    # matzeget shiur 8
    # squares = []
    # for i in range(100):
    #     squares.append(i**2)
    # print(squares)
    #
    # squares = [i ** 2 for i in range(100)]
    # print(squares)
    #
    # Letters = "python"
    # upper_list = [Letters.upper() for l in Letters]
    # print(upper_list)
    #
    # numbers = list(range(1, 7))
    # letters = "python"
    # pairs = [(n, l) for n in numbers for l in letters]
    # print(pairs)

#     lesson 8
# targil 1
    lst_1 = [1,1,1,1]
    lst_2 = [4,3,2,1]
    diff_avg = [(lst_1 = lst_1 + i for i in lst_1)/i] - [(lst_2 = lst_2 + i for i in lst_2)/i]
    print(diff_avg)
# targil 2
    x = (lambda string : [string.remove(b) for b in (string.split())], ("bython"))
    print(x)
# targil 3
    lambda int : int + 2
# targil 4
    lambda x : x.abs()
    list = [2, -8, 5, -6, -1, 3]
    y = list.sort()

