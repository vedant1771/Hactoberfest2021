import pandas as pd
import numpy as np
from sklearn import metrics
import streamlit as st
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv("data.csv")
df = df.drop(['ID','Experience'], axis = 1)
X=df[['Age','Income','CCAvg','Education','Mortgage','Securities Account','Online',"CreditCard"]].values
y=df['Personal Loan'].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

from sklearn import preprocessing
X = preprocessing.normalize(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

def results(model):
    res = model.predict([ipt])
    if res == 1:
        st.success("The Customer will avail the loan")
    else:
        st.success("The Customer will not avail the loan")
     
html_temp = '''
    <div style = "background-color: rgba(25,25,112,0.06); padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
    <center><h1>Bank Loan Modelling</h1></center>
    
    </div>
    '''
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.subheader("Input Features")
st.sidebar.text("Specify your inputs here")
ipt = []
ipt.append(st.sidebar.slider('Age',1,100,20))
ipt.append(st.sidebar.number_input('Income'))
ipt.append(st.sidebar.number_input('CCAvg'))
ipt.append(st.sidebar.radio('Education',[1,2,3]))
ipt.append(st.sidebar.number_input('Mortgage'))
ipt.append(st.sidebar.radio('Securities Account',[0,1]))
ipt.append(st.sidebar.radio('Online',[0,1]))
ipt.append(st.sidebar.radio('CreditCard',[0,1]))

html_temp_2 = '''
    <div style = "padding-bottom: 20px; padding-top: 20px; padding-left: 20px; padding-right: 20px">      
    <center><h2>Model Selection</h2></center>
    </div>
    '''
st.markdown(html_temp_2, unsafe_allow_html=True)

select = st.selectbox("Please Select your model from the following options",("Please Select","Logistic Regression","Support Vector Machine","KNeighbours Classifier","Naive-Bayes Classifier"))
try:
    if select == "Logistic Regression":
        model = LogisticRegression()
        model.fit(X_train,y_train)

    if select == "Support Vector Machine":
        model = SVC(kernel = 'linear')
        model.fit(X_train,y_train)

    if select == "KNeighbours Classifier":
        model = KNeighborsClassifier(n_neighbors = 7)
        model.fit(X_train,y_train)

    if select == "Naive-Bayes Classifier":
        model = GaussianNB()
        model.fit(X_train,y_train)

    if st.button("Predict"):
        results(model)
        
expect:
    pass

    
