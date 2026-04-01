import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabities_model=pickle.load(open('diabities_model.sav','rb'))
heart_model=pickle.load(open('heart_disease_model.sav','rb'))
parkinson_model=pickle.load(open('parkinsons_model.sav','rb'))



with st.sidebar:
    selected =option_menu('Health predixAI',
        ['Diabetes Prediction',
         'Heart disease prediction',
         'Parkinsons Prediction'],
         default_index =0)

#Diabetes
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    Pregnancies = st.text_input('Number of Pregnancies')

    Glucose = st.text_input('Glucose Level')

    BloodPressure = st.text_input('Blood Pressure value')

    SkinThickness = st.text_input('Skin Thickness value')

    Insulin = st.text_input('Insulin Level')

    BMI = st.text_input('BMI value')

    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    Age = st.text_input('Age of the Person')
    diab_diagnosis = ''

    if st.button('Diabetes Test result'):
        diab_Prediction = diabities_model.predict([[pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFuncton,Age]])

        if(diab_Prediction[0]==1):
            diab_diagnosis = 'this person is diabitic'
        else:
            diab_diagnosis = 'this person is not diabitic'
    st.success(diab_diagnosis)
if(selected == 'Heart disease prediction'):
    st.title('Heart disease prediction using ML')
    age = st.text_input('Age')
    sex = st.text_input('sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis=''

    if st.button('heart disease test result'):
        heart_prediction=heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if(heart_prediction[0]==1):
            heart_diagnosis='this person has heart disease'
        else:
            heart_diagnosis='this person does not has heart disease'    
    st.success(heart_diagnosis)
if(selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button('parkinson test diagnosis'):
        parkinson_prediction=parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs,RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        if(parkinson_prediction[0]==1):
            parkinsons_diagnosis='this person is diagnosed with parkinsons'
        else:
            parkinsons_diagnosis='this person is not diagnosed with parkinsons'
    st.success(parkinsons_diagnosis)


