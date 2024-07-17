
def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# lesson 4
# targil 1
# start = int(input("enter a number between 1-9."))
# stop = int(input("enter a number between 1-9."))
# x=start
# y=stop
# print("the chezkot of the numbers range is: ")
# while x <= y:
#     print(x ** 2)
#     x += 1

# targil 2
# i = 1
# print(i)
# num1 = 1
# while i < 33323:
#     print(i)
#     num2 = num1
#     num1 = i
#     i = num1 + num2

# targil 3
# list_str = input("enter the list:")
# list = (list_str.split(", "))
# n = (int(input("enter the number:")))
# new_list = []
# for i in list:
#     num = int(i)
#     if num > n:
#         new_list.append(num)
# print(new_list)


# targil 4
# str = input("Enter a string:")
# list_str = list(str)
# count1 = 0
# count2 = 0
# for i in list_str:
#     if i in ("0", '1', '2', '3', '4', '5', '6', '7', '8', "9"):
#         count1 += 1
#     else:
#         count2 += 1
# print("numbers: {}, letter and symbols: {}".format(count1, count2))

# targil 5
# list = []
# x = int(input("please enter a number:"))
# i = 0
# while i <= x:
#     list.append(i)
#     if i % 7 == 0 or i % 10 == 7 or i / 10 == 7:
#         list[i] = "boom"
#     i += 1
# print(list)


# targil 8
# x = input("please enter a char:")
# num = int(input("please enter a number:"))
# for i in range(0, (num+1)):
#     print(i*x)
# for i in range(1, num):
#     print(x*(num-i))