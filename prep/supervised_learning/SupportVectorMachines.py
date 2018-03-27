def SVMAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn.svm import SVC
    clf = SVC(kernel="rbf", C = 10000.0)
    
    t0 = time() ### Set training timer 
    ### Uncomment to train with a data subset ###################
    ### features_train = features_train[:len(features_train)/100] 
    ### labels_train = labels_train[:len(labels_train)/100] 
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"
    
    t0 = time() ### Set prediction timer 
    pred = clf.predict(features_test)
    print "training time:", round(time()-t0, 3), "s"
    
    from sklearn.metrics import accuracy_score
    return accuracy_score(pred, labels_test)

accuracy = SVMAccuracy(features_train, labels_train, features_test, labels_test)
