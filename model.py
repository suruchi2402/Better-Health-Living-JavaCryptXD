import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("iris.csv")
dfparent = pd.read_csv("parents.csv")
dfteacher = pd.read_csv("teachers.csv")

print(df.head())

# Select independent and dependent variable
X = df[["Q.1", "Q.2", "Q.3", "Q.4", "Q.5","Q.6", "Q.7","Q.8","Q.9","Q.10", "Q.11", "Q.12", "Q.13" , "Q.14" , "Q.15"]]
y = df["Verdict"]

# Select independent and dependent variable
XParent = dfparent[["Q.1", "Q.2", "Q.3", "Q.4", "Q.5","Q.6", "Q.7","Q.8","Q.9","Q.10"]]
yParent = dfparent["Verdict"]

# Select independent and dependent variable
XTeacher = dfteacher[["Q.1", "Q.2", "Q.3", "Q.4", "Q.5","Q.6", "Q.7","Q.8","Q.9","Q.10"]]
yTeacher = dfteacher["Verdict"]

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# Split the dataset into train and test
XParent_train, XParent_test, yParent_train, yParent_test = train_test_split(XParent, yParent, test_size=0.8, random_state=42)

# Split the dataset into train and test
XTeacher_train, XTeacher_test, yTeacher_train, yTeacher_test = train_test_split(XTeacher, yTeacher, test_size=0.8, random_state=42)


# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)
XParent_train = sc.fit_transform(XParent_train)
XParent_test= sc.transform(XParent_test)
XTeacher_train = sc.fit_transform(XTeacher_train)
XTeacher_test= sc.transform(XTeacher_test)

# Instantiate the model
classifier = RandomForestClassifier()
classifierparent = RandomForestClassifier()
classifierteacher = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)
classifierparent.fit(XParent_train, yParent_train)
classifierteacher.fit(XTeacher_train, yTeacher_train)

# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))
pickle.dump(classifierparent, open("modelparent.pkl", "wb"))
pickle.dump(classifierteacher, open("modelteacher.pkl", "wb"))