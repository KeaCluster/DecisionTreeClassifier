import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor  # regression

from sklearn.metrics import classification_report, confusion_matrix

dataset = pd.read_csv("stores.csv")
X = dataset.drop(["name", "decision"], axis=1)
y = dataset["decision"]


def classify_Tree():
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30
    )  # test with only 30% of all data

    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    print(
        "Confusion Matrix: \n\n",
        conf_matrix,
        "\n\n",
        "Values from table:\n\n ",
        df,
        "\n\n",
        "Overall report: \n\n",
        report,
        file=open("normal_tree.txt", "w"),
    )


def regress_Tree():
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=0
    )
    # regression
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(
        "Confusion Matrix: \n\n",
        conf_matrix,
        "\n\n",
        "Values from table:\n\n ",
        df,
        "\n\n",
        "Overall report: \n\n",
        report,
        file=open("regression_tree.txt", "w"),
    )
