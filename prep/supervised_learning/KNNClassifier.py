import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from time import time
from sklearn.neighbors import KNeighborsClassifier

features_train, labels_train, features_test, labels_test = makedata()

def RunKNeighborsClassifier(features_train, labels_train, features_test, labels_test):
    clf=KNeighborsClassifier(
        n_neighbors=2, 
        weights='distance', 
        algorithm='ball_tree',  
        metric = 'braycurtis')
    t0 = time()
    clf.fit(features_train,labels_train)
    print "training time:", round(time()-t0, 3), "s"
    pred = clf.predict(features_test)
    from sklearn.metrics import accuracy_score
    print accuracy_score(pred,labels_test)
    print "prediction time:", round(time()-t0, 3), "s"
     
RunKNeighborsClassifier(features_train, labels_train, features_test, labels_test)
