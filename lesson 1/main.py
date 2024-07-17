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
# kovetz IDLE
#lesson 1
# #targil 1
name = input("enter your name:")
print("hello" + name)
# targil 2
first_number = int(input("enter a number"))
second_number = int(input("enter another number"))
print("numbers sum")
print(first_number + second_number)


# אגדת שלושת הברווזונים
x = input("הכנס מס' תלת ספרתי שכל ספרה בו מייצגת א, מס' הלבנים שאסף ברווז אחר")
x = int(x)
number1 = x % 10    #sifrat hayechidot
number2 = (x % 100 // 10)   #sifrat haasrot
number3 = (x // 100)   #sifrat hameot
print(number1)
print(number2)
print(number3)
print("numbers sum:", number1 + number2 + number3)

print("מספר הלבנים שיקבל כל ברווז אם יחלקו את מספר הלבנים הכולל שווה בין כולם" ,(number1 + number2 + number3) / 3)
print("שארית חלוקת הלבנים " ,(number1 + number2 + number3) % 3)
sum2 = ((number1 + number2 + number3) % 3)

ccc = sum2 % 3 == 0
print("the number is divided to 3? ", ccc)

#lesson 2
# print("\'Shuffle, Shuffle, Shuffle," "say it together!\'" \n "Change colors and directions," \n "Don\'t back down and stop the player!" \n "Do you want to play Taki?" \n "Press y\\n")
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[-1:0:-2])