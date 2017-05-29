# machine learning sample code. predict gender based on height weight and show size

from sklearn import tree
#[height, weight, shoe size]
X = [[181,80,44],[177,70,43],[160,50,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
Y = ['male','female','female','female','male','male','male','female','male','female','male']

#initialize decision tree object
clf = tree.DecisionTreeClassifier()

#fir method trains our classifier over training data set
clf= clf.fit(X,Y)

#predict for a new data

print('height,weight,shoe size')
print('190,70,43')
prediction = clf.predict([[190,70,43]])
print(prediction)
