from datetime import datetime

def Numbersbetween (start, end, interval):
# This function prints and counts the numbers between two selected numbers 
# using an interval between numbers.
    nodict = {}
    try:
        startno = int(input(start))
        endno = int(input(end))
        intvl = int(input(interval))

        numberslist = list(range(startno + intvl, endno, intvl))
        print (numberslist)
        print (f"{len(numberslist)} is the total numbers between {startno} and {endno} with an interval of {intvl}")
        nodict['lst'] = numberslist
        nodict['strt'] = startno
        nodict['end'] = endno
        nodict['int'] = intvl
        return nodict
    except ValueError:
        print ("Please enter integer (whole) digits only")
        main()

def printresults (lst, start, end, intvl):
# This function either prints the results to a text file or asks if you'd like to repeat.
    prnt = input("Would you like to print the results? Y / N: ").lower()
    if prnt not in ("y", "n"):
        print ("Command not recognised")
        printresults (lst, start, end, intvl)        
    if prnt == "y":
        # Checking if there is a previous entry, and if so the run number. 
        try:
            with open("c:/users/Ralf/Desktop/Numbers.txt", "r") as s:
                linelist = s.readlines()
                if linelist == "\n":
                    runnumber = 1
                else:
                    runline = linelist[len(linelist)-5]
                    runnumber = (int(runline.lstrip("Run Number:")) + 1)
        except FileNotFoundError:
            runnumber = 1


        # Writing the new entry using the correct run number from above.
        with open("c:/users/Ralf/Desktop/Numbers.txt", "a") as s:
            if runnumber > 1:
                s.write("\n\n")
            s.write(f"Run Number: {runnumber}\nDate: {datetime.now()}\n")
            s.write(f"Start number: {start}  End number: {end}  Interval: {intvl}\n")
            s.write(f"{lst}\n")
            s.write(f"Total number of values between start and end: {len(lst)}")
            
        print ("Results successfully printed!")
        return
                 
    else:
        return
        
def runagain ():
# This function runs the counting function again if requested, or quits if not. 
    rerun = input("Would you like to run the program again? Y / N: ").lower()
    if rerun == "y":
        main()
    if rerun not in ("y", "n"):
        print ("Command not recognised")
        runagain()
    else: 
        print ("Thank you for using this program")

__counter = 0
def main ():
    global __counter
    if __counter == 0:
        print("""
+--------------------------------------------+
| This function lists and counts the numbers |
|   between a selected start and end value   |
|          along with an interval.           |
+--------------------------------------------+
""")
        __counter += 1
    else:
        pass
    nodict = Numbersbetween("Enter start Value: ", "Enter end value: ", "Enter interval: ")
    printresults(nodict['lst'], nodict['strt'], nodict['end'], nodict['int'])
    runagain()


if __name__ == "__main__":
    main()
      





