# Laporan Proyek Machine Learning
### Nama : Muhamad Zidan Husaini
### Nim : 211351092
### Kelas : PAGI B

## Domain Proyek

Project ini dibuat untuk meningkatkan kewaspadaan masyarakat terhadap penyakit jantung sehingga bisa melakukan tindakan pencegahan dengan melakukan diagnosa awal pada aplikasi ini.

## Business Understanding

Project ini memudahkan diagnosa dini tanpa harus mengantri ataupun konsultasi dengan dokter untuk menghemat biaya dan waktu.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Kurangnya kesadaran masyarakat terhadap penyakit jantung

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Menyadarkan masyarakat akan pentingnya kesehatan jantung dengan mendiagnosanya sejak dini sebelum terkena penyakit jantung 

    ### Solution statements
    - Memberikan solusi untuk masyarakat berdasarkan datasets yang terjadi pada studi kasus penyakit jantung

## Data Understanding
Data ini diambil dari kaggle dengan indeks perhitungan kolesterol dan rata-rata detak jantung
dan diklasifikasikan dengan algoritma svm linear.

[Cholesterol](https://www.kaggle.com/datasets/aaronfinley/cholesterol).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:
- Age : usia pasien(integer)
- Sex : jenis kelamin(integer)
- ChestPainType : jenis rasa sakit pada dada yang ada pada istilah kedokteran(integer)
- RestingBP : tekanan darah pasien dengan satuan mmHg(integer)
- Cholesterol : kadar kolesterol pasien dengan satuan mg/dL(integer)
- FastingBS : kadar gula pada pasien dengan satuan mg/dL(integer)
- RestingECG : hasil pemeriksaan ekg dalam kondisi istirahat(integer)
- MaxHR : parameter denyut jantung maksimal saat melakukan aktivitas fisik(integer)
- ExerciseAngina : parameter apakah mempunyai riwayat penyakit angin duduk(integer)
- Oldpeak : parameter untuk mengetahui kadar depresi pasien(integer)
- ST_Slope : kecenderungan rata-rata detak jantung(integer)
- HeartDisease : parameter untuk mengetahui resiko terkena penyakit jantung(integer)

## Data Preparation

Pertama import dulu library yang dibutuhkan dengan memasukkan perintah:

```bash
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```

Kemudian agar dataset di dalam kaggle langsung bisa terhubung ke kaggle maka harus membuat token terlebih dahulu di akun kaggle dengan memasukan perintah : 
```bash
from google.colab import files
files.upload()
```
Setelah itu lalu masukan file token.

Berikutnya yaitu membuat direktori dengan memasukan perintah :
```bash
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle
!chmod 600 ~/.kaggle/kaggle.json
!ls ~/.kaggle
```

Setelah itu kita panggil url dataset yang ada di website kaggle untuk didownload langsung ke google colab.
```bash
!kaggle datasets download -d aaronfinley/cholesterol
```

Jika berhasil, selanjutnya kita ekstrak dataset yang sudah didownload dengan perintah :
```bash
!mkdir cholesterol
!unzip cholesterol.zip -d cholesterol
!ls cholesterol
```

Jika berhasil diekstrak, maka kita langsung dapat membuka dataset tersebut dengan perintah :
```bash
df = pd.read_csv('cholesterol/heart.csv')
```

jika sudah membaca data csv lalu kita membuka isi data pada kolomnya dengan perintah :
```bash
df.info()
```

jika berhasil kemudian kita mengganti tipe data yang bukan integer menjadi integer dengan perintah :
```bash
df=df.replace({'Sex':{'M': 0, 'F': 1}})
```

##Visualisasi Data

Jika ingin mengecek heatmap dari data kita ada yang kosong atau tidak, masukan perintah :
```bash
plt.figure(figsize = (18,9))
sns.heatmap(df.corr(), cmap='GnBu', annot=True)
plt.show()
```
Jika ingin mengecek heatmap dengan mengurutkan nilainya masukkan perintah :
```bash
sns.heatmap(df.corr()[['HeartDisease']].sort_values(by='HeartDisease', ascending=False), vmin=-1, vmax=1, annot=True, cmap='GnBu')
```

## Modeling
Untuk melakukan modeling saya memakai algoritma regresi linear, dimana kita harus memisahkan mana saja atribut yang akan dijadikan sebagai fitur(x) dan atribut mana yang dijadikan label(y).
```bash
X = df.drop (columns='HeartDisease', axis=1)
Y = df['HeartDisease']
```

selanjutnya saya scaling data untuk menghilangkan perbedaan skala
```bash
scaler = StandardScaler()
scaler.fit(X)
standarized_data = scaler.transform(X)
```

selanjutnya mendeklarasikan kembali atribut dan label yang sudah discaling
```bash
X = standarized_data
Y = df['HeartDisease']
```

selanjutnya menentukan data training dan testing
```bash
 X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, stratify=Y, random_state=2)
```

selanjutnya membuat model klasifikasi dengan algoritma svm 
```bash
classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)
```
## Evaluation
Untuk melakukan tahap evaluasi, matriks evaluasi yang digunakan adalah matriks akurasi
```bash
x_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(x_train_prediction, Y_train)
```
```
print('Tingkat akurasi data training = ', training_data_accuracy)
```
Tingkat akurasi data training =  0.8524904214559387
```bash
x_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(x_test_prediction, Y_test)
```
```bash
print('Tingkat akurasi data test = ', test_data_accuracy)
```
Tingkat akurasi data test =  0.8392857142857143

Berdasarkan proses yang sudah di lakukan didapakatkan akurasi data training sebesar 85% dan akurasi data testing 83% yang berarti model tersebut dapat digunakan.

## Deployment
Link Aplikasi: [Diagnosa Penyakit Jantung]()

