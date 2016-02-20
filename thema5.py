import os

def dow(year,month,day):
    # day of week, Sunday = 1, Saturday = 7
     #http://en.wikipedia.org/wiki/Zeller%27s_congruence
    m, q = month, day
	
			  
    if m == 1:
        m = 13
        year -= 1
    elif m == 2:
        m = 14
        year -= 1
    K = year % 100    
    J = year // 100
    f = (q + int(13*(m + 1)/5.0) + K + int(K/4.0))
    fg = f + int(J/4.0) - 2 * J
    fj = f + 5 - J
    if year > 1582:
        h = fg % 7
    else:
        h = fj % 7
    if h == 0:
        h = 7
    return h-1
	
	
week   = ['Sunday', 
           'Monday', 
           'Tuesday', 
           'Wednesday', 
           'Thursday',  
           'Friday', 
           'Saturday']	

mera=int(input("Please type day:"))
minas=int(input("Please type month:"))
etos=int(input("Please type year:"))

print(week[dow(etos, minas, mera)])

os.system("pause")