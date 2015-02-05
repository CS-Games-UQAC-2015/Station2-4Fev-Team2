filename = "A-small-practice.in"
with open(filename) as txt:
    casesAmount = txt.readline()

    for i in range(casesAmount):
        inputAmount = txt.readline()

        for j in range(inputAmount):
            line = txt.readline()
            for k in range(len(line))


