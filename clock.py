
"""
clock.py
"""

from datetime import datetime
from time import sleep
from os import system, name

ascii = ['''
 000000 
 00  00 
 00  00 
 00  00 
 000000 
''',
'''
   11   
   11   
   11   
   11   
   11   
''',
'''
 222222 
    222 
 222222 
 222    
 222222 
''',
'''
 333333 
    333 
 333333 
    333 
 333333 
''',
'''
 44  44 
 44  44 
 444444 
     44 
     44 
''',
'''
 555555 
 555    
 555555 
    555 
 555555 
''',
'''
 666666 
 66     
 666666 
 66  66 
 666666 
''',
'''
 777777 
 77  77 
     77 
     77 
     77 
''',
'''
 888888 
 88  88 
 888888 
 88  88 
 888888 
''',
'''
 999999 
 99  99 
 999999 
     99 
 999999 
''',
'''
    
 :: 
    
 :: 
    
'''
]

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

clear()

while True:
    clock = str(datetime.now())[11:19] # splice to remove date

    clockList = [] # save current time in array format, to call ascii[i]
    for i in range(len(clock)):
        if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7 or i == 8: # do not print ':'
            clockList.append(int(clock[i]))
        else:
            clockList.append(10)

    splittedAscii = [ascii[j].splitlines() for j in clockList]
    for k in zip(*splittedAscii):
        print(*k, sep='')

    sleep(1)
    clear()
