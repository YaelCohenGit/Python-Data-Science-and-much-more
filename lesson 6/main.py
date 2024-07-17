
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# lesson 6
#targil 1
    def sort_prices(list_of_tuples):
        list_of_tuples=[('item', 'price'), ('item', 'price'), ('item', 'price')]
        list_of_keys=list_of_tuples.keys()
        list_of_values=list_of_tuples.values()
        sorted_list_of_values=list_of_values.sort()
        reversed_&_sorted_list_of_values=sorted_list_of_values.reverse()

        return

#targil 2
    def mult_tuple(tuple1, tuple2):
        list = []
        for i in range(0, len(tuple1)):
            for j in range(0, len(tuple2)):
                ntuple1 = tuple1[i], tuple2[j]
                list.append(ntuple1)
                ntuple2 = tuple2[i], tuple1[j]
                list.append(ntuple2)
        return tuple(list)

#targil 4
    num = int(input("Enter a number from 1-7: "))
    dict = {'first_name': 'mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}
    if num == 1:
        print(dict['last_name'])
    if num == 2:
        print(dict['birth_date'][3:5])
    if num == 3:
        print(len(dict['hobbies']))
    if num == 4:
        print(dict['hobbies'][-1])
    if num == 5:
        dict['hobbies'].append('cooking')
    if num == 6:
        dict['birth_date'] = (int(dict['birth_date'][0:2]), int(dict['birth_date'][3:5]), int(dict['birth_date'][6:]))
        print(dict['birth_date'])
    if num == 7:
        age = 2023 - int(dict['birth_date'][6:])
        print(age)

# targil 5
    def count_chars(string):
        dict = {}
        for letter in string:
            if letter != " ":
                dict[letter] = 0
        for letter in string:
            if letter != " ":
                dict[letter] += 1
        return dict

# targil 7
    data = ("self", "py", 1.543)
    format_string = "Hello %s. %s learner, you have only %f units left before you master the course!" % data
    print(format_string)
    format_string = "Hello . learner, you have only units left before you master the course!"
    print("Hello {}.{} learner, you have only {} units left before you master the course!".format("self", "py",
                                                                                                  (round(1.543, 1))))
    print("Hello %s.%s learner, you have only %f units left before you master the course!" % (
    "self", "py", (round(1.543, 1))))



if __name__ == '__main__':
    print_hi('PyCharm')
    #2
    print(mult_tuple((1, 2, 3), (4, 5, 6)))
    #5
    string = input("Enter a string: ")
    print(count_chars(string))


