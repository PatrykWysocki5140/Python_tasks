from itertools import permutations
from itertools import combinations


def reverse(x):
    string = str(x)
    int_min = -2147483648
    int_max = 2147483647
    if x < 0:
        string = '-' + string[::-1][:-1]
        x = int(string)
    else:
        string = string[::-1]
        x = int(string)           
    if (x >= int_min and x <= int_max):
        print(x)
    else:
        print(0, "number", x ,"outside the borders")

def phone(x):
    list2 = ["a","b","c"]
    list3 = ["d","e","f"]
    list4 = ["g","h","i"]
    list5 = ["j","k","l"]
    list6 = ["m","n","o"]
    list7 = ["p","q","r","s"]
    list8 = ["t","u","v"]
    list9 = ["w","x","y","z"]
    string = list(str( x )) 
    numbers = []
    tab = []
    tab_to_sort = []
    for char in string:
        number = int(char)
        numbers.append( number )
        if number == 2:
            tab = tab + list2
            if char in string[0]:
                tab_to_sort = tab_to_sort + list2
        elif number == 3:
            tab = tab + list3
            if char in string[0]:
                tab_to_sort = tab_to_sort + list3
        elif number == 4:
            tab = tab + list4
            if char in string[0]:
                tab_to_sort = tab_to_sort + list4
        elif number == 5:
            tab = tab + list5
            if char in string[0]:
                tab_to_sort = tab_to_sort + list5
        elif number == 6:
            tab = tab + list6
            if char in string[0]:
                tab_to_sort = tab_to_sort + list6
        elif number == 7:
            tab = tab + list7
            if char in string[0]:
                tab_to_sort = tab_to_sort + list7
        elif number == 8:
            tab = tab + list8
            if char in string[0]:
                tab_to_sort = tab_to_sort + list8
        elif number == 9:
            tab = tab + list9
            if char in string[0]:
                tab_to_sort = tab_to_sort + list9
        else:
            print('[]')
    length = len(numbers)
    tab_to_print = []
    for char in tab_to_sort:
        tab_to_print = tab_to_print + tab
        if char in list2:            
            tab_to_print.remove("a")
            tab_to_print.remove("b")
            tab_to_print.remove("c")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list3:            
            tab_to_print.remove("d")
            tab_to_print.remove("e")
            tab_to_print.remove("f")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list4:            
            tab_to_print.remove("g")
            tab_to_print.remove("h")
            tab_to_print.remove("i")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list5:           
            tab_to_print.remove("j")
            tab_to_print.remove("k")
            tab_to_print.remove("l")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list6:            
            tab_to_print.remove("m")
            tab_to_print.remove("n")
            tab_to_print.remove("o")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list7:            
            tab_to_print.remove("p")
            tab_to_print.remove("q")
            tab_to_print.remove("r")
            tab_to_print.remove("s")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list8:            
            tab_to_print.remove("t")
            tab_to_print.remove("u")
            tab_to_print.remove("v")
            tab_to_print.append(str(char))
            tab_to_print.sort()
            perm(tab_to_print, length)
            del tab_to_print[:]
        elif char in list9:            
            tab_to_print.remove("w")
            tab_to_print.remove("x")
            tab_to_print.remove("y")
            tab_to_print.remove("z")
            tab_to_print.append(str(char))
            tab_to_print.sort()           
            perm(tab_to_print, length)            
            del tab_to_print[:]
                    
def perm(tab_to_print, length):
    for i in combinations(tab_to_print, length):
        if (tab_to_print[0] in i[0]):
            print(str(i))

def justify(x,width):
    x.lstrip()
    string = list(x.split(' '))
    fillchar = ' '
    words_in_line = '"'
    width_count = 0 
    for word in string:
        if (word != '') and (word != ' '):
            if (width_count + len(word)) <= width: 
                width_count += len(word) 
                width_count += 1 
                word.rjust((width -width_count) , fillchar)
                words_in_line += word 
                words_in_line += ' ' 

            else:
                words_in_line += '"\n' 
                words_in_line += '"'
                word.ljust((width -width_count) , fillchar)
                words_in_line += word
                words_in_line += ' '
                width_count = 1 
                width_count += len(word) 
    words_in_line += '"\n'
    print(words_in_line.rstrip().rjust(width, fillchar))                
    
def Menu():

    while True:
        print("""\
        Menu: (Type a number and press enter):
        (1) First task;
        (2) Second task;
        (3) Third task;
        (4) Exit;
        """)
        try:
            a=int(input("enter number : "))                        
        except:
            print("Type a number and press enter")

        if a == 1:
                x=int(input("load data into the function : "))
                reverse(x)
        elif a == 2:
                x=int(input("load data into the function : "))
                phone(x) 
        elif a == 3:
                x=str(input("words = "))
                y=int(input("maximum_width = "))
                justify(x,y)
        elif a == 4:
                break       

Menu()

