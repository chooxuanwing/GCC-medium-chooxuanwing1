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
    
    out = ''
    
    for i in range(0,stringLength//lowBound):
        out += wordsFormatted[i*upBound]
        print(out)
    return " "


def main():
    words = input()

    answer = encrypt(words)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()