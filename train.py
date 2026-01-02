from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
# Loading the dataset in the data frame.
iris_df=pd.read_csv('https://raw.githubusercontent.com/mpourhoma/CS4661/master/iris.csv')

print(iris_df)

# Get Feature names into Feature_columns and label name
Feature_columns=iris_df.columns.values.tolist()[:-1]
Label=iris_df.columns.values.tolist()[-1]
print("Feature Columns:"+str(Feature_columns))
print("Label:"+str(Label))
print('\n\n')

X=iris_df[Feature_columns]
y=iris_df[Label]

#Splitting the dataset to 60% training data and 40% testing data 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4, random_state=10)

print('Training set\n')
print('Features of size: ' + str(X_train.shape) + '\n' + str(X_train))
print('\n')
print('Label:\n'+ str(y_train.shape)+ '\n' +str(y_train))

print('\n\nTesting set\n')
print('Features of size: ' + str(X_test.shape) + '\n' + str(X_test))
print('\n')
print('Label:\n'+ str(y_test.shape)+ '\n' +str(y_test))


k=3
knn=KNeighborsClassifier(n_neighbors=k)#instantiating knn object
knn.fit(X_train,y_train)#training

joblib.dump(knn,"iris_classifier.pkl")