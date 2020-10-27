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
    # for i in range(0,len(participantsPreferences)):
    #     # print(bankersPreferences[participantsPreferences[i][0]-1][0])
    #     # print(participantsPreferences[i][0])
    #     if (participantsPreferences[i][0]==bankersPreferences[participantsPreferences[i][0]-1][0]):
    #         # participantsPreferences[i].remove(participantsPreferences[i][0])
    #         # participantsPreferences[i].pop(0)
    #         participantsPreferences[i][0]=0

    #     if (bankersPreferences[i][0]==participantsPreferences[bankersPreferences[i][0]-1][0]):
    #         # participantsPreferences[i].remove(participantsPreferences[i][0])
    #         # participantsPreferences[i].pop(0)
    #         bankersPreferences[i][0]=0

    #     print('b',bankersPreferences)

    #     print('p',participantsPreferences)


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
    # numOfBankers=2
    # numOfParticipants=3
    # bankersPreferencesListOfList = [[1], [2,3]]
    # participantsPreferencesListOfList = [[1], [2], [2]]
    
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