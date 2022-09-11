#Write a program to display ASCII code of a character and vice-versa

#CODE FOR CHARACTER TO ASCII
char_input = input("Enter a charater: ")

print(f"ASCII value of {char_input} is {ord(char_input)}")

#CODE FOR ASCII TO CHARACTER
ascii_input = int(input("Enter an ASCII code: "))

print(f"Character of ASCII value {ascii_input} is {chr(ascii_input)}")