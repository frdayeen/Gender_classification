from sklearn import tree

X = [[181,80,44],[177,79,43],[160,60,38],[155,65,40],[190,90,47],[187,64,39]]
Y = ['male','female','female','male','male','female']

clf = tree.DecisionTreeClassifier()

clf =clf.fit(X,Y)

prediction = clf.predict([[145,49,32]])

print(prediction)