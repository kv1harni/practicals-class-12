def isPalidome(arg):
    if len(arg)<=1:
        return True
    else:
        if arg[0] == arg[-1]:
            return isPalidome(arg[1:-1])
        else:
            return False

uinput = input("Enter a Word: ")
val =  isPalidome(uinput)

print("yes its a pallidome" if val == True else "not a pallidome")