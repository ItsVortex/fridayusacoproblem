"""
ID: alex.go2
LANG: PYTHON3
TASK: friday
"""
f = open('friday.in', 'r')
g = open('friday.out', 'w')
integern = f.readlines()
n = int(integern[0])
year = 1900
date = 0
month = 1
day = 0
thday = [0,0,0,0,0,0,0]

for x in range (0 , n):
    whichyear = year + x
    if whichyear % 4 == 0:
        if whichyear != 1900 and whichyear != 2100 and whichyear != 2200 and whichyear != 2300:
            
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day % 7] = thday[day % 7] + 1
                if x == 30:
                    month = month + 1
                    date = 0
            for x in range (0, 29):      
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day % 7] = thday[day % 7] + 1
                if x == 28:
                    month = month + 1
                    date = 0
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    month = month + 1
                    date = 0
            for x in range (0, 30):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 29:
                    month = month + 1
                    date = 0
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    date = 0
                    month = month + 1
            for x in range (0, 30):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 29:
                    date = 0
                    month = month + 1
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    date = 0
                    month = month + 1
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    date = 0
                    month = month + 1
            for x in range (0, 30):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 29:
                    date = 0
                    month = month + 1
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    date = 0
                    month = month + 1
            for x in range (0, 30):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 29:
                    date = 0
                    month = month + 1
            for x in range (0, 31):
                day = day + 1
                date = date + 1
                if date == 14:
                    thday[day% 7] = thday[day% 7] + 1
                if x == 30:
                    date = 0
                    month = month + 1
    if whichyear == 1900 or whichyear == 2100 or whichyear == 2200 or whichyear == 2300 or whichyear % 4 != 0:
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day%7] = thday[day%7] + 1
            if x == 30:
                month = month + 1
                date = 0
        for x in range (0, 28):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day % 7] = thday[day % 7] + 1
            if x == 27:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1
        for x in range (0, 30):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 29:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1
        for x in range (0, 30):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 29:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1
        for x in range (0, 30):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 29:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1
        for x in range (0, 30):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 29:
                date = 0
                month = month + 1
        for x in range (0, 31):
            day = day + 1
            date = date + 1
            if date == 14:
                thday[day% 7] = thday[day% 7] + 1
            if x == 30:
                date = 0
                month = month + 1

g.write(str(thday[0]))
g.write(" ")
g.write(str(thday[1]))
g.write(" ")
g.write(str(thday[2]))
g.write(" ")
g.write(str(thday[3]))
g.write(" ")
g.write(str(thday[4]))
g.write(" ")
g.write(str(thday[5]))
g.write(" ")
g.write(str(thday[6]))
g.write("\n")


g.close()
          
                        
                    
                
        
