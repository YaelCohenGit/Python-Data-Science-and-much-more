# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #תרגיל 1
# print("\"Shuffle, Shuffle, Shuffle\", say it together!\n Change colors and directions,\n Don\'t back down and stop the player! \n\tDo you want to play Taki? \n\tPress y\\n")
#
# # #תרגיל 2
# msg = "syzygy"
# print(len(msg))
# print(msg[-1::])
# print(msg[::2])
# print(msg[1] == msg[3] == msg[5])
#
# # #תרגיל 3
#
# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# print(encrypted_message[::-2])

# # #תרגיל 4
# string = input("Please enter a string")
# y=string[0]
# change_string=(string.replace(string[0],"r"))
# change_string=change_string[1:]
# print("{}{}".format(y, change_string))


# #תרגיל 6
word = "spaceship"
print(word.isspace())
print(word.count('p'))
print(word.find('sh'))
print(word.endswith('e'))
print(len(word))
print(word[-2::-4])
print(word.startswith('spa'))

# #תרגיל 1
# string=input("enter string")
# if string[0::]==string[::-1]:
#     print("ok")
# else:
#     print("not")
#
# #תרגיל2
# temp = input("enter temp")
# if temp[-1] == "c" or temp[-1] == "C":
#     a = int(temp[0:-1:])
#     print((9*a+160)/5,"f")
# elif temp[-1] == "f" or temp[-1] == "F":
#     a = int(temp[0:-1:])
#     print((5*a-160)/9,"c")
# else:
#     print("The input is worng")