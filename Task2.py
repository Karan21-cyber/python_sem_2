try: #Try is used to check the program runs or not. If runs it executed else return except.
    print("\nSwallow Speed Analysis: Version 1.0\n")
    MPH = []
    sum = 0
    while True:
        speed = input("Enter the Next Reading: ")
        if 'U' in speed:  # It checks that "U" is in the input or not. 
            mile = float(speed[1:])
            MPH.append(mile)
            print("Reading Saved.")   

        elif 'E' in speed: # It check that "E" is in the input or not. 
            km = float(speed[1:])
            kmTomiles = km/1.61
            MPH.append(kmTomiles)
            print("Reading Saved.")
            
        elif speed == "": # If there is no input then it breaks and stop the loop.
            break
        else:  # it execute if wrong input is given
            print("Wrong Input!")
            continue
    
    if len(MPH) == 0: # It check the length of list is equal to 0 or not.
        print("No Reading entered. Nothing to do.\n")
    
    else: # It execute if the length of list is greater then 0.
        maxdata = max(MPH)
        convertmax = maxdata * 1.61
        mindata = min(MPH)
        convertmin = mindata *1.61
        
        for x in range(len(MPH)): #This loop is used for adding the value inside the list
            sum += MPH[x]
        avgmile = sum/len(MPH)
        avgkm = avgmile * 1.61

        print("\nResult Summary\n")
        if len(MPH) == 1: # It check count that is equal to 2 or not. 
            print(len(MPH), " Reading Analysed.\n")
        else:
            print(len(MPH)," Readings Analysed.\n")

        print("Max Speed: {:.1f} MPH, {:.1f} KPH.".format(maxdata,convertmax))
        print("Min Speed: {:.1f} MPH, {:.1f} KPH.".format(mindata,convertmin))
        print("Avg Speed: {:.1f} MPH, {:.1f} KPH.\n".format(avgmile,avgkm))
    
except: # If the program has error then it prints
    print("Your input is wrong! Try Again!!")
    