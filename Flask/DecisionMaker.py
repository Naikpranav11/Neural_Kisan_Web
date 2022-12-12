class DM:
  
    def Train(self,csvPath):
        df = pd.read_csv(csvPath)

        iris = datasets.load_iris()

        import pandas as pd
        data=pd.DataFrame({
        'sepal length':iris.data[:,0],
        'sepal width':iris.data[:,1],
        'petal length':iris.data[:,2],
        'petal width':iris.data[:,3],
        'species':iris.target
            })
        data.head()


        X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
        y=data['species']  # Labels

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
        from sklearn.ensemble import RandomForestClassifier
        
        #Create a Gaussian Classifier
        clf=RandomForestClassifier(n_estimators=100)

        #Train the model using the training sets y_pred=clf.predict(X_test)
        clf.fit(X_train,y_train)

        
        print('Trained')
        # joblib.dump(clf,'model.pkl')
        # print("Model Saved")
    def Classify(self):
        # lr=joblib.load('model.pkl')
        y_pred= self.clf.predict(self.X_test)
        species_idx = self.clf.predict([[3, 5, 4, 2]])[0]
        return self.iris.target_names[species_idx]




##PRANAV ENTER CODE HERE

def classify(img,modelFile,labels):
     ##Load the model
       model = load_model(modelFile)

       camera = img

       labels = open(labels, 'r').readlines()
       ret, image = camera.read()
       image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
       image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
       image = (image / 127.5) - 1
       probabilities = model.predict(image)
       ret ={'LABEL':f'{labels[np.argmax(probabilities)]}','MAX':f'{np.max(probabilities)}','MIN':f'{np.min(probabilities)}'}
       json_dump=json.dumps(ret)
       return json_dump