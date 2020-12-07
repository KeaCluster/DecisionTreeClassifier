# DecisionTreeClassifier
Decision Tree Classifier using python - regression &amp; standard clasification 
##### The main.py file will output different .txt files depending on your choice

## Use
Just run ```main.py``` as any other .py file. 
```tree.py``` just holds the algorithm as functions

**NOTE:**  It's using ```python 3.8.6``` due to complications with scikitlearn on ```3.9 ver```

**You'll need a .csv file to input your dataset** Use ``` stores.csv ``` if you want to get an idea of the syntax

```
dataset = pd.read_csv("your.csv")
```
Drop any columns using strings, they'll cause error when evaluating
```
X = dataset.drop(["name", "another_name"], axis=1)
```
Your decision/choice should be one column. Set as a boolean ```0 OR 1 ``` and this goes in the ```y``` axis, drop in the the prev line
```
y = dataset["choice"]
```

There is a loop to read your ``` .csv ``` file on the  ```main.py``` script. It'll print out your ** whole ** file, so keep that in mind.


## Python modules
- tkinter
- pandas
- numpy
- matplotlib
- scikitlearn / sklearn

## MIT Licence or whatever
##### Do whatever fancy artsy stuff you want to do with it with the admision that I blatantly got parts and pieces from different places inside the world *whack* web
