import math
import numpy as np

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2   +  (P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier(k=3):
    border = "-"*60

    Data = [
        {'point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'point' : 'D', 'X' : 5, 'Y' : 6, 'Label' : 'Blue'},
        {'point' : 'E', 'X' : 6, 'Y' : 6, 'Label' : 'Blue'},
        {'point' : 'F', 'X' : 3, 'Y' : 4, 'Label' : 'Red'},
        {'point' : 'G', 'X' : 3, 'Y' : 2, 'Label' : 'Red'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

    new_point = {'X' : 3, 'Y' : 3}

    print("Distances of All points : ")
    print(border)
    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(Data,key=lambda item : item['distance'])
    print("sorted Data : ")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    

    nearest = sorted_data[:k]

    print(border)
    print("nearest 3 members are : ")
    print(border)

#    for d in nearest:
#       print(d)
#       
#   print(nearest)

    #voting
    votes = {}
    
    for neighbours in nearest:
        lable = neighbours['Label']
        votes[lable] = votes.get(lable,0)+1

    print(border)
    print("Voting Result is : ")
    print(border)

    for d in votes:
        print("Name : ",d,"Number of votes : ",votes[d])

    print(border)

    iMax = 0
    Name = ""

    for d in votes:
        if (votes[d]>iMax):
            iMax = votes[d]
            Name=d
    print("Final Prediction is : ",Name)


def main():
    MarvellousKNNClassifier(5)

if __name__ == "__main__":
    main()


