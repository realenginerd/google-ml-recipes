from sklearn import tree
features = [[140, 0], [130, 0], [150, 1], [170, 1]] # [weight, type] 0 is bumpy
labels = [0, 0, 1, 1] # 0 is apple, 1 is orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[130, 1], [160, 1], [160, 0], [170, 0]])

