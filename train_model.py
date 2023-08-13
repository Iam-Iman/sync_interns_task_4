### Training the Random Forest Classifier Model

# import packages
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb')) # open the saved pickle file

data = np.asarray(data_dict['data'])

labels = np.asarray(data_dict['labels'])
#print(len(data))
#print(labels)
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels) # split data

clf = RandomForestClassifier() # initialize classifier

clf.fit(x_train, y_train) # fit classifier

y_predict = clf.predict(x_test) # make predictions 
# evaluate using classification report
class_rep = classification_report(y_predict, y_test)

print(class_rep)

f = open('model.p', 'wb')
pickle.dump({'model': clf}, f)
f.close()

