from datetime import datetime

def Numbersbetween (start, end, interval):
# This function counts and prints to console the numbers between two selected numbers using the interval provided.
    global numberslist, startno, endno, interval1, lenlist
    startno = int(input(start))
    endno = int(input(end))
    interval1 = int(input(interval))
    numberslist = []

    for i in range(startno + 1, endno, interval1):
        numberslist.append(str(i))
    print (numberslist)
    lenlist = len(numberslist)
    print (len(numberslist), "is the total numbers between ", startno, "and ", endno, "with an interval of ",interval1)
    prnt = input(str("Would you like to print the results? Y / N: "))
    printresults(prnt)


def printresults (answer):
# This function creates a new file, or appends existing one with latest run of program. It also asks if you want to repeat either way.
    if answer == "y" or answer == "Y":
        # Checking if there is a previous entry, and if so the run number. 
        try:
            s = open("c:/users/user/Desktop/Numbers.txt", "r")
            linelist = s.readlines()
            s.close()
            if linelist == "\n":
                runnumber = 1
            else:
                runline = linelist[len(linelist)-5]
                runnumber = (int(runline.lstrip("Run Number:")) + 1)
        except FileNotFoundError:
            runnumber = 1


        # Writing the new entry using the correct run number from above.
        s = open("c:/users/Ralf/Desktop/Numbers.txt", "a")
        if runnumber > 1:
            s.write("\n\n")
        s.write(f"Run Number: {runnumber}\nDate: {datetime.now()}\n")
        s.write(f"Start number: {startno}  End number: {endno}  Interval: {interval1}\n")
        s.write(str(numberslist))
        s.write("\n")
        s.write(f"Total number of values between start and end: {lenlist}")
        s.close()  
        
        again = input(str("Would you like to run the program again? "))
        runagain(again)
              
    else:
        again = input(str("Would you like to run the program again? "))
        runagain(again)
        
def runagain (answer):
# This function runs the counting function again if requested, or quits if not. 
    if answer == "y" or answer == "Y":
        Numbersbetween("Enter start Value: ", "Enter end value: ", "Enter interval: ")
    else: 
        print ("Thank you for using this program")
      
print ("""This function lists and counts the numbers 
between a selected starting and end value 
along with a chosen interval
""")
Numbersbetween("Enter start Value: ", "Enter end value: ", "Enter interval: ")
