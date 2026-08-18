# Define a function that counts vowels and consonants in a word. Assume the input contains only alphabetic characters. The program should correctly handle both uppercase and lowercase letters while counting vowels and consonants.


def a(n):
    vowel=0
    constants=0

    for i in n:
        if i in "aeiouAEIOU":
            vowel+=1
        else:
            constants+=1

    print(f"vowel={vowel}\nconstants={constants}")

s=input("enter: ")

a(s)