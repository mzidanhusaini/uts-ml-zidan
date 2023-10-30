import pickle
import streamlit as st

model = pickle.load(open('penyakit_jantung.sav', 'rb'))

st.title('Diagnosa Resiko Anda Terkena Penyakit Jantung')

Age = st.text_input('Usia Anda')
Sex = st.selectbox('Jenis Kelamin anda ?', ['Laki laki', 'Perempuan'])

if Sex == 'Laki laki':
    Sex = 0
else:
    Sex = 1
ChestPainType = st.selectbox('Tipe nyeri dada anda ?', ['Asymptonic', 'Non-Angina Pain', 'Atypical Angina', 'Typical Angina'])

if ChestPainType == 'Asymptonic':
    ChestPainType = 1
elif ChestPainType == 'Non-Angina Pain':
      ChestPainType = 2
elif ChestPainType == 'Atypical Angina':
      ChestPainType = 3
else:
    ChestPainType = 4
RestingBP = st.text_input('Resting blood pressure [mm Hg] ?')
Cholesterol = st.text_input('Tingkat kolesterol anda ?')
FastingBS = st.selectbox('Fasting Blood Sugar ?', ['Ya', 'Tidak'])

if FastingBS == 'Ya':
    FastingBS = 1
else:
    FastingBS = 0
RestingECG = st.selectbox('Hasil test EKG ketika beristirahat ?', ['Normal', 'LVH', 'ST'])

if RestingECG == 'Normal':
    RestingECG = 1
elif RestingECG == 'LVH':
    RestingECG = 2
else:
    RestingECG = 3
MaxHR = st.text_input('Total maksimal detak jantung ?')
ExerciseAngina = st.selectbox('Apakah anda berolahraga ?', ['Ya', 'Tidak'])

if ExerciseAngina == 'Ya':
    ExerciseAngina = 1
else:
    ExerciseAngina = 0
Oldpeak = st.text_input('Indeks depresi (Oldpeak) ?')
ST_Slope = st.selectbox('Kecenderungan detak jantung', ['Meningkat', 'Stagnan', 'Menurun'])

if ST_Slope == 'Meningkat':
    ST_Slope = 0
elif ST_Slope == 'Stagnan':
    RestingECG = 1
else:
    RestingECG = 2

tingkat_resiko = ''

if st.button('Diagnosa'):
    resiko_jantung = model.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
    
    if(resiko_jantung[0] == 0):
        tingkat_resiko = 'Anda Tidak Beresiko Terkena Penyakit Jantung'
    else :
        tingkat_resiko ='Anda Beresiko Terkena Penyakit Jantung'

    st.success(tingkat_resiko)