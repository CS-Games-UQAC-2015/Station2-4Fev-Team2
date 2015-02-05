filename = "A-small-practice.in"

def resolve(lines):
    # Sort lines by length order (smallest first)
    lines.sort(key=len)
    
    shortest = 99999999
    
    # Get unique characters in all strings
    for i in range(len(lines)):
        line = lines[i]
        
        if i == 0:
            continue;
            
        # If the unique characters of this line aren't the same as the last line, it's impossibru
        if (set(lines[i-1]) != set(line)):
            return "Fegla Won"
    
    return shortest

def main():
    with open(filename) as txt:
        casesAmount = int(txt.readline())
    
        for i in range(casesAmount):
            inputAmount = int(txt.readline())
            lines = []
            
            # Get all lines
            for j in range(inputAmount):
                line = txt.readline().rstrip('\n')
                lines.append(line)
                
            # Solve
            print("Case #" + str(i) + ": " + str(resolve(lines)))
            
if __name__ == "__main__":
    main()