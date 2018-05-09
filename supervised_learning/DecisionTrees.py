def DCAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=50)

    t0 = time() ### Set training timer 
    clf = clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time() ### Set prediction timer 
    pred = clf.predict(features_test)
    print "training time:", round(time()-t0, 3), "s"

    from sklearn.metrics import accuracy_score
    return accuracy_score(pred, labels_test)

accuracy = DCAccuracy(features_train, labels_train, features_test, labels_test)
