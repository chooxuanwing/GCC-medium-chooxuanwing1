# import sys
# Participants may update the following function parameters
def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):

    totalTrades = []
    sum=0
    for i in range(0,noOfTradesAvailable):
        totalTrades.append(p[i]*x[i]-(1-p[i])*y[i])
    totalTrades = sorted(totalTrades, reverse=True)
    print(totalTrades)

    for j in range(0,maximumTradesAllowed):
        sum+=totalTrades[j]
    print(sum)

    return sum

def main():
    # This part may require participants to fill in as well.
    noOfTradesAvailable, maximumTradesAllowed = list(map(int, input().split()))
    p = list(map(float, input().split()))
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    # noOfTradesAvailable = 4
    # maximumTradesAllowed = 2
    # p=[0.5 ,0.5 ,0.5 ,0.5]
    # x=[4.00, 1.00, 2.00, 3.00]
    # y=[4.00 ,0.50 ,1.00 ,1.00]
    
    # Participants may update the following function parameters
    answer = maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()