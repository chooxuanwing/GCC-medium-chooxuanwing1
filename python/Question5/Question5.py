# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
    
     
    # print(numOfParticipants)
    # print(numOfBankers)
    # print('b',bankersPreferences)
    # print('p',participantsPreferences)
    # print('********************')
    temp=0
    count=0
    temp1=0
    count1=0

    for i in participantsPreferences:
        # print(i)
        temp = participantsPreferences.count(i)
        if (temp>count):
            count = temp
    # print(count)

    for j in bankersPreferences:
        # print(j)
        temp1=bankersPreferences.count(j)
        if(temp1>count1):
            count1=temp1
    # print(count1)

    if (count1>count):
        return count1
    return count
   

    
    


def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()