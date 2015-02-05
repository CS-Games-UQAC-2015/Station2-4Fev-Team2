filename = "A-small-practice.in"
with open(filename) as txt:
    casesAmount = int(txt.readline())

    for i in range(casesAmount):
        inputAmount = int(txt.readline())
        str = ['']*inputAmount
        
        for j in range(inputAmount):
            line = txt.readline()
            str[j] = line
            #for k in range(len(line))
            
        print('Case #',i,': ')