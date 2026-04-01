import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabities_model = pickle.load(open('diabities_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinson_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu(
        'Health predixAI',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        default_index=0
    )

# ========================= DIABETES =========================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    Pregnancies = st.number_input('Number of Pregnancies')
    Glucose = st.number_input('Glucose Level')
    BloodPressure = st.number_input('Blood Pressure value')
    SkinThickness = st.number_input('Skin Thickness value')
    Insulin = st.number_input('Insulin Level')
    BMI = st.number_input('BMI value')
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    Age = st.number_input('Age')

    if st.button('Diabetes Test Result'):
        input_data = [
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]

        diab_prediction = diabities_model.predict([input_data])

        if diab_prediction[0] == 1:
            st.error('This person is diabetic')
        else:
            st.success('This person is not diabetic')


# ========================= HEART =========================
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    age = st.number_input('Age')
    sex = st.number_input('Sex (0 = Female, 1 = Male)')
    cp = st.number_input('Chest Pain types (0–3)')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholesterol (mg/dl)')
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)')
    restecg = st.number_input('Resting ECG results (0–2)')
    thalach = st.number_input('Max Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina (1 = yes, 0 = no)')
    oldpeak = st.number_input('ST depression')
    slope = st.number_input('Slope (0–2)')
    ca = st.number_input('Major vessels (0–3)')
    thal = st.number_input('Thal (0 = normal, 1 = fixed, 2 = reversible)')

    if st.button('Heart Disease Test Result'):
        input_data = [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak,
            slope, ca, thal
        ]

        heart_prediction = heart_model.predict([input_data])

        if heart_prediction[0] == 1:
            st.error('This person has heart disease')
        else:
            st.success('This person does not have heart disease')


# ========================= PARKINSON =========================
elif selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')

    fo = st.number_input('MDVP:Fo(Hz)')
    fhi = st.number_input('MDVP:Fhi(Hz)')
    flo = st.number_input('MDVP:Flo(Hz)')
    Jitter_percent = st.number_input('MDVP:Jitter(%)')
    Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
    RAP = st.number_input('MDVP:RAP')
    PPQ = st.number_input('MDVP:PPQ')
    DDP = st.number_input('Jitter:DDP')
    Shimmer = st.number_input('MDVP:Shimmer')
    Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
    APQ3 = st.number_input('Shimmer:APQ3')
    APQ5 = st.number_input('Shimmer:APQ5')
    APQ = st.number_input('MDVP:APQ')
    DDA = st.number_input('Shimmer:DDA')
    NHR = st.number_input('NHR')
    HNR = st.number_input('HNR')
    RPDE = st.number_input('RPDE')
    DFA = st.number_input('DFA')
    spread1 = st.number_input('spread1')
    spread2 = st.number_input('spread2')
    D2 = st.number_input('D2')
    PPE = st.number_input('PPE')

    if st.button('Parkinson Test Result'):
        input_data = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP,
            PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
            APQ, DDA, NHR, HNR, RPDE, DFA,
            spread1, spread2, D2, PPE
        ]

        parkinson_prediction = parkinson_model.predict([input_data])

        if parkinson_prediction[0] == 1:
            st.error('This person has Parkinson’s disease')
        else:
            st.success('This person does not have Parkinson’s disease')
