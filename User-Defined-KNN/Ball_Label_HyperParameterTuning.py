import math
import numpy as np


def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt(
        (P1['X'] - P2['X'])**2 +
        (P1['Y'] - P2['Y'])**2
    )

    return Ans


def MarvellousKNNClassifier(k=3):

    border = "-" * 60

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'Label': 'Blue'},
        {'point': 'E', 'X': 6, 'Y': 6, 'Label': 'Blue'},
        {'point': 'F', 'X': 3, 'Y': 4, 'Label': 'Red'},
        {'point': 'G', 'X': 3, 'Y': 2, 'Label': 'Red'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

    new_point = {'X': 3, 'Y': 3}

    print("Distances of All points : ")
    print(border)

    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(Data, key=lambda item: item['distance'])

    print("Sorted Data : ")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    nearest = sorted_data[:k]

    print("Nearest", k, "members are : ")
    print(border)

    for d in nearest:
        print(d)

    # Voting
    votes = {}

    for neighbours in nearest:

        label = neighbours['Label']

        votes[label] = votes.get(label, 0) + 1

    print(border)
    print("Voting Result is : ")
    print(border)

    for d in votes:
        print("Name : ", d, "Number of votes : ", votes[d])

    print(border)

    iMax = 0
    Name = ""

    for d in votes:

        if votes[d] > iMax:

            iMax = votes[d]
            Name = d

    print("Final Prediction is : ", Name)

    return Name


def CalculateAccuracy(Data, k):

    Correct = 0
    Total = len(Data)

    for test_point in Data:

        TrainingData = []

        for d in Data:

            if d['point'] != test_point['point']:
                TrainingData.append(d)

        for d in TrainingData:

            d['distance'] = MarvellousEucDistance(d, test_point)

        SortedData = sorted(
            TrainingData,
            key=lambda item: item['distance']
        )

        Nearest = SortedData[:k]

        Votes = {}

        for neighbour in Nearest:

            Label = neighbour['Label']

            Votes[Label] = Votes.get(Label, 0) + 1

        iMax = 0
        Prediction = ""

        for Label in Votes:

            if Votes[Label] > iMax:

                iMax = Votes[Label]
                Prediction = Label

        if Prediction == test_point['Label']:

            Correct = Correct + 1

    Accuracy = (Correct / Total) * 100

    return Accuracy


def HyperParameterTuning():

    border = "-" * 60

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'Label': 'Blue'},
        {'point': 'E', 'X': 6, 'Y': 6, 'Label': 'Blue'},
        {'point': 'F', 'X': 3, 'Y': 4, 'Label': 'Red'},
        {'point': 'G', 'X': 3, 'Y': 2, 'Label': 'Red'}
    ]

    print("\n")
    print(border)
    print("Hyper Parameter Tuning")
    print(border)

    KValues = [2, 3, 4, 5]

    BestK = 0
    BestAccuracy = 0

    for k in KValues:

        Accuracy = CalculateAccuracy(Data, k)

        print("K =", k, "Accuracy =", Accuracy, "%")

        if Accuracy > BestAccuracy:

            BestAccuracy = Accuracy
            BestK = k

    print(border)
    print("Best K Value :", BestK)
    print("Best Accuracy :", BestAccuracy, "%")
    print(border)


def main():

    MarvellousKNNClassifier(5)

    HyperParameterTuning()


if __name__ == "__main__":

    main()