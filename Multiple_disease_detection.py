'''
@author: Anurag Toshniwal
'''

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

# Sidebar navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Detection System',
                          ['Diabetes',
                          'Heart Disease',
                          'Parkinsons'],
                          icons=['activity','heart','person'],
                          menu_icon = 'cast')
    
    
# Diabetes Page

if selected == 'Diabetes':
    
    st.title('Diabetes Detection via ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.00, step=1e-2, format="%.2f")
    with col3:
        BloodPressure = st.number_input('Blood Pressure', min_value=0.00, step=1e-2, format="%.2f")
        
    with col1:
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0.00, step=1e-2, format="%.2f")
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0.00, step=1e-2, format="%.2f")
    with col3:
        BMI = st.number_input('BMI', min_value=0.00, step=1e-2, format="%.2f")
      
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.00,step=1e-3, format="%.3f")
    with col2:
        Age = st.number_input('Age of Person', min_value=0)
        
    # Prediction
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(Glucose==0 or BloodPressure==0 or SkinThickness==0 or Insulin==0 or BMI==0 or DiabetesPedigreeFunction == 0 or Age==0):
            st.error('Please enter values correctly !!')
        
        else:
            if diab_prediction[0] == 0:
                diab_diagnosis = 'The person 𝗶𝘀 𝗻𝗼𝘁 diabetic'
            else:
                diab_diagnosis = 'The person 𝗶𝘀 diabetic'
        
            st.success(diab_diagnosis)
        


# Heart Disease  Page
if (selected == 'Heart Disease'):
    
    # page title
    st.title('Heart Disease Detection via ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0)
        
    with col2:
        sex = st.selectbox('Sex', ['Male','Female'])
        
    with col3:
        cp = st.selectbox('Chest Pain types', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0)
        
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
        
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', ['Nothing to note','ST-T Wave abnormality','Possible or definite left ventricular hypertrophy'])
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0)
        
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', min_value=0.00)
        
    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping','Flatsloping','Downslopins'])
        
    with col3:
        ca = st.selectbox('Major vessels colored by flourosopy', [0,1,2,3,4])
        
    with col1:
        thal = st.selectbox('Thalium stress result',['Normal', 'Fixed defect', 'Reversable defect'])
        
        
    if sex == 'Male':
        sex = 1
    else:
        sex = 0
        
    if fbs == 'True':
        fbs = 1
    else:
        fbs = 0
        
    if exang == 'Yes':
        exang = 1
    else:
        exang = 0
        
    if thal == 'Normal':
        thal = 1
    elif thal == 'Fixed defect':
        thal = 2
    else:
        thal = 3
        
    if cp == 'Typical angina':
        cp = 0
    elif cp == 'Atypical angina':
        cp = 1
    elif cp == 'Non-anginal pain':
        cp = 2
    else:
        cp = 3
    
    if restecg == 'Nothing to note':
        restecg = 0
    elif restecg == 'ST-T Wave abnormality':
        restecg = 1
    else:
        restecg = 2
        
    if slope == 'Upsloping':
        slope = 0
    elif slope == 'Flatsloping':
        slope = 1
    else:
        slope = 2

     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        if (age==0 or trestbps==0 or chol==0 or thalach==0 or oldpeak==0):
            st.error('Please enter correct values !!')
    
        else:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
            if (heart_prediction[0] == 1):
                  heart_diagnosis = 'The person 𝗶𝘀 𝗵𝗮𝘃𝗶𝗻𝗴 heart disease'
            else:
                  heart_diagnosis = 'The person 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗵𝗮𝘃𝗲 𝗮𝗻𝘆 heart disease'
        
            st.success(heart_diagnosis)
                

                 

# Parkinson's Prediction Page
if (selected == "Parkinsons"):
    
    # page title
    st.title("Parkinsons Detection via ML")
    
    col1, col2,  col3, col4 = st.columns(4)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col1:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        RAP = st.number_input('MDVP:RAP', min_value=0.00, step=1e-5, format='%.5f')
        
    with col3:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.00, step=1e-5, format='%.5f')
        
    with col4:
        DDP = st.number_input('Jitter:DDP', min_value=0.00, step=1e-5, format='%.5f')
        
    with col1:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.00, step=1e-5, format='%.5f')
        
    with col3:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.00, step=1e-5, format='%.5f')
        
    with col4:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.00, step=1e-5, format='%.5f')
        
    with col1:
        APQ = st.number_input('MDVP:APQ', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        DDA = st.number_input('Shimmer:DDA', min_value=0.00, step=1e-5, format='%.5f')
        
    with col3:
        NHR = st.number_input('NHR', min_value=0.00, step=1e-5, format='%.5f')
        
    with col4:
        HNR = st.number_input('HNR', min_value=0.00, step=1e-5, format='%.5f')
        
    with col1:
        RPDE = st.number_input('RPDE', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        DFA = st.number_input('DFA', min_value=0.00, step=1e-5, format='%.5f')
        
    with col3:
        spread1 = st.number_input('Spread 1', max_value=0.000, step=1e-5, format='%.5f')
        
    with col4:
        spread2 = st.number_input('Spread 2', min_value=0.00, step=1e-5, format='%.5f')
        
    with col1:
        D2 = st.number_input('D2', min_value=0.00, step=1e-5, format='%.5f')
        
    with col2:
        PPE = st.number_input('PPE', min_value=0.00, step=1e-5, format='%.5f')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        
        if(fo==0 or fhi==0 or flo==0 or Jitter_percent==0 or Jitter_Abs==0 or RAP==0 or PPQ==0 or DDP==0 or Shimmer==0 or 
           Shimmer_dB==0 or APQ3==0 or APQ5==0 or APQ==0 or DDA==0 or NHR==0 or HNR==0 or RPDE==0 or DFA==0 or spread1==0 
           or spread2==0 or D2==0 or PPE==0):
            
            st.error('Please enter correct values !!')
        
        else:
            
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
            if (parkinsons_prediction[0] == 1):
                  parkinsons_diagnosis = "The person 𝗵𝗮𝘀 Parkinson's disease"
            else:
                  parkinsons_diagnosis = "The person 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗵𝗮𝘃𝗲 Parkinson's disease"
        
            st.success(parkinsons_diagnosis)

