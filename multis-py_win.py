import os

print("hi this is a simple program i made in my free time.")

print("if you don't know how to use multis-py_win just type help or press enter to skip this message.")

r = input()

if r == 'help':
    print("multis-py_win is a simple program that displays system info.")


while True:

     str = "(1) display system info\n(2) list files and directories\n(3) display the weather\n(4) display system info in detail\n(5) start cmd\n(6) exit"
     print(str)


     e = input()

     if e == '1':
        os.system("neofetch")


     if e == '2':
       os.system("dir")


     if e == '3':
         os.system("(curl http://wttr.in/?Q0 -UserAgent curl )")


     if e == '4':
         os.system("systeminfo")


     if e == '5':
         os.system("start")


     if e == '6':
         os.system("exit")
         break
