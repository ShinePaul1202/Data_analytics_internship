# Seven different symbols represent Roman numerals with the following values:

# Symbol Value
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9, use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times, use the subtractive form

# Given an integer, convert it to a Roman numeral.


def numToRoman(num):
    result=""

    while num>=1000:
        result+="M"
        num-=1000

    while num>=900:
        result+="CM"
        num-=900

    while num>=500:
        result+="D"
        num-=500

    while num>=400:
        result+="CD"
        num-=400

    while num>=100:
        result+="C"
        num-=100

    while num>=90:
        result+="XC"
        num-=90

    while num>=50:
        result+="L"
        num-=50

    while num>=40:
        result+="XL"
        num-=40

    while num>=10:
        result+="X"
        num-=10

    while num>=9:
        result+="IX"
        num-=9

    while num>=5:
        result+="V"
        num-=5

    while num>=4:
        result+="IV"
        num-=4

    while num>=1:
        result+="I"
        num-=1

    return result

while True:

    try:   
        num=int(input("Enter a number: "))

        if 1<=num<=3999:
            break

        print("enter a number btw 1 and 3999")

    except ValueError:
        print("please enter a vaild integer")

print(numToRoman(num))