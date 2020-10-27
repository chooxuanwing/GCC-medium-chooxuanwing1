import math
# You may change this function parameters
def encrypt(words):
    # Participants code will be here
    
    wordsFormatted = words.replace(" ","")
    print(wordsFormatted)
    stringLength = len(wordsFormatted)
    sqrt = pow(stringLength,0.5)
    lowBound = math.floor(sqrt)
    upBound = math.ceil(sqrt)
    checkBox = lowBound*upBound

    if (checkBox < stringLength):
        lowBound += 1
    remainder = stringLength%lowBound

    print(stringLength, lowBound, upBound,remainder)

    out = ''
    
    count =0
    j=0
    while (remainder!=0):
        while (j < remainder-1):
            # count += 1
            for j in range(0,remainder):
                for i in range(0,stringLength//lowBound+ 1):
                    out += wordsFormatted[(i*upBound)+j]
                    print(out)
                out += " "

        for j in range(remainder,upBound):
            for i in range(0, stringLength//lowBound):
                out += wordsFormatted[(i*upBound) +j] 
                print(out)
            out += " "
        return out

    print('NO REMAINDER')
    for j in range(0, upBound):
        for i in range(0,lowBound):
            out += wordsFormatted[i*upBound+j]
        out += " "
    return out


def main():
    words = input()

    # answer = encrypt('its harder to read code than to write itttyuy')
    answer = encrypt(words)
    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()