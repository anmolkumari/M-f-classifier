from sklearn import tree
clf=tree.DecisionTreeClassifier()

X = [[181, 80, 44, 40], [177, 70, 43, 44], [160, 60, 38, 32], [154, 54, 37, 34], [166, 65, 40, 45],
     [190, 90, 47, 48], [175, 64, 39, 36],
     [177, 70, 40, 37], [159, 55, 37, 35], [171, 75, 42, 49], [181, 85, 43, 48]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
      'female', 'male', 'male']
clf=clf.fit(X,Y)
print("enter your height,weight and shoe size chest size")
h=input()
w=input()
shoe=input()
cs=input()

prediction=clf.predict([[h,w,shoe,cs]])
print (prediction)   