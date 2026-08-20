# Machine Learning Assignment
# Topics: NumPy, StandardScaler, Euclidean Distance,
# Classification Metrics, TP/TN/FP/FN and Classification Report


# ============================================================
# Q1. Calculate Mean using NumPy
# ============================================================

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


Data = np.array([6, 7, 8, 9, 10, 11, 12])

Mean = np.mean(Data)

print("=" * 60)
print("Q1. MEAN")
print("=" * 60)
print("Dataset:", Data)
print("Mean =", Mean)


# ============================================================
# Q2. Calculate Variance and Standard Deviation
# ============================================================

Variance = np.var(Data)
StandardDeviation = np.std(Data)

print("\n" + "=" * 60)
print("Q2. VARIANCE AND STANDARD DEVIATION")
print("=" * 60)
print("Dataset:", Data)
print("Variance =", Variance)
print("Standard Deviation =", StandardDeviation)


# ============================================================
# Q3. Feature Scaling using StandardScaler
# ============================================================

Data2 = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

Scaler = StandardScaler()

ScaledData = Scaler.fit_transform(Data2)

print("\n" + "=" * 60)
print("Q3. FEATURE SCALING USING STANDARDSCALER")
print("=" * 60)
print("Original Dataset:")
print(Data2)

print("\nScaled Dataset:")
print(ScaledData)


# ============================================================
# Q4. Euclidean Distance Before and After Feature Scaling
# ============================================================

# Distance between first and second points before scaling
DistanceBefore = np.sqrt(
    (Data2[0][0] - Data2[1][0]) ** 2 +
    (Data2[0][1] - Data2[1][1]) ** 2
)

# Distance between first and second points after scaling
DistanceAfter = np.sqrt(
    (ScaledData[0][0] - ScaledData[1][0]) ** 2 +
    (ScaledData[0][1] - ScaledData[1][1]) ** 2
)

print("\n" + "=" * 60)
print("Q4. EUCLIDEAN DISTANCE")
print("=" * 60)
print("Distance Before Scaling =", DistanceBefore)
print("Distance After Scaling  =", DistanceAfter)

print("\nExplanation:")
print("Before scaling, the feature with larger values has a much")
print("greater effect on the Euclidean distance.")
print("After scaling, both features are brought to a comparable scale.")


# ============================================================
# Q5. Classification Report
# ============================================================

print("\n" + "=" * 60)
print("Q5. CLASSIFICATION REPORT")
print("=" * 60)

print("A classification report is used to evaluate a classification")
print("model. It provides precision, recall, F1-score and support.")
print("It is mainly used for classification problems.")


# ============================================================
# Q6. Classification Metrics
# ============================================================

print("\n" + "=" * 60)
print("Q6. CLASSIFICATION METRICS")
print("=" * 60)

print("Precision:")
print("Precision = TP / (TP + FP)")
print("It tells us how many predicted positive values were actually positive.")

print("\nRecall:")
print("Recall = TP / (TP + FN)")
print("It tells us how many actual positive values were correctly identified.")

print("\nF1 Score:")
print("F1 Score = 2 * Precision * Recall / (Precision + Recall)")
print("It gives a balance between precision and recall.")

print("\nSupport:")
print("Support is the number of actual samples belonging to each class.")

print("\nAccuracy:")
print("Accuracy = Correct Predictions / Total Predictions")
print("It tells us the percentage of total predictions that are correct.")


# ============================================================
# Q7. Determine TP, TN, FP and FN
# ============================================================

Actual = [1, 1, 1, 1, 0, 0, 0, 0]
Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for i in range(len(Actual)):

    if Actual[i] == 1 and Predicted[i] == 1:
        TP += 1

    elif Actual[i] == 0 and Predicted[i] == 0:
        TN += 1

    elif Actual[i] == 0 and Predicted[i] == 1:
        FP += 1

    elif Actual[i] == 1 and Predicted[i] == 0:
        FN += 1

print("\n" + "=" * 60)
print("Q7. TP, TN, FP AND FN")
print("=" * 60)
print("Actual Values:   ", Actual)
print("Predicted Values:", Predicted)
print("True Positive (TP)  =", TP)
print("True Negative (TN)  =", TN)
print("False Positive (FP) =", FP)
print("False Negative (FN) =", FN)


# ============================================================
# Q8. Python Program to Calculate TP, TN, FP and FN
# ============================================================

actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for i in range(len(actual)):

    if actual[i] == 1 and predicted[i] == 1:
        TP += 1

    elif actual[i] == 0 and predicted[i] == 0:
        TN += 1

    elif actual[i] == 0 and predicted[i] == 1:
        FP += 1

    elif actual[i] == 1 and predicted[i] == 0:
        FN += 1

print("\n" + "=" * 60)
print("Q8. TP, TN, FP AND FN USING PYTHON")
print("=" * 60)
print("TP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)


# ============================================================
# Q9. Classification Report using Scikit-learn
# ============================================================

actual = [1, 1, 1, 0, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

Report = classification_report(actual, predicted)

print("\n" + "=" * 60)
print("Q9. CLASSIFICATION REPORT USING SCIKIT-LEARN")
print("=" * 60)
print("Actual Values:   ", actual)
print("Predicted Values:", predicted)
print("\nComplete Classification Report:")
print(Report)