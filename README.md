# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan telah menghasilkan banyak lulusan berkualitas. Reputasi baik institusi ini dibangun atas dasar kualitas pendidikan, tenaga pengajar yang kompeten, serta lulusan yang mampu bersaing di dunia kerja. Namun demikian, institusi ini menghadapi tantangan besar berupa tingginya angka siswa yang tidak menyelesaikan pendidikannya atau mengalami *dropout*.

Tingginya angka *dropout* menjadi ancaman terhadap reputasi dan kredibilitas Jaya Jaya Institut. Hal ini juga berdampak pada efisiensi operasional, target kelulusan, serta kepercayaan masyarakat terhadap institusi. Untuk itu, diperlukan langkah strategis guna meminimalkan angka *dropout* dengan cara mendeteksi siswa yang berisiko secepat mungkin, sehingga institusi dapat memberikan intervensi atau bimbingan lebih awal.

Dalam rangka mendukung pengambilan keputusan yang lebih baik dan berbasis data, pihak institusi ingin memanfaatkan teknologi data science dan visualisasi data dalam bentuk **dashboard pemantauan performa siswa**. Dengan adanya dashboard ini, pihak manajemen dan tenaga pengajar dapat lebih mudah memantau perkembangan siswa, mengenali pola-pola *dropout*, dan melakukan tindakan preventif.

### Permasalahan Bisnis

Berikut adalah permasalahan bisnis yang ingin diselesaikan:

1. **Tingginya tingkat *dropout* siswa**  
   Banyak siswa yang tidak menyelesaikan pendidikan mereka, sehingga memengaruhi reputasi dan target akademik institusi.

2. **Tidak adanya sistem deteksi dini siswa berisiko *dropout***  
   Institusi belum memiliki alat analisis berbasis data untuk mengidentifikasi siswa yang berisiko mengalami *dropout* secara lebih cepat dan akurat.

3. **Keterbatasan dalam memantau performa siswa secara menyeluruh**  
   Informasi performa siswa belum tersaji dalam bentuk dashboard yang mudah dipantau dan dianalisis oleh pihak manajemen dan pengajar.

4. **Kurangnya intervensi berbasis data**  
   Tanpa adanya prediksi atau segmentasi siswa berdasarkan performa dan risiko *dropout*, tindakan intervensi menjadi tidak terarah atau bahkan terlambat.

5. **Kebutuhan akan sistem monitoring yang interaktif dan informatif**  
   Institusi membutuhkan sistem dashboard yang dapat menampilkan kondisi performa siswa secara real-time dan dapat membantu proses pengambilan keputusan yang lebih cepat dan tepat.


### Cakupan Proyek

Proyek ini bertujuan untuk membantu **Jaya Jaya Institut** dalam menurunkan tingkat *dropout* siswa melalui pendekatan berbasis data dan visualisasi interaktif. Cakupan proyek difokuskan pada pemanfaatan data performa siswa, analisis prediktif, serta pengembangan dashboard pemantauan performa yang informatif dan mudah digunakan. Berikut adalah ruang lingkup yang dikerjakan dalam proyek ini:

1. **Pengumpulan dan Pembersihan Data**
   - Mengakses dan mengimpor data siswa dari berbagai sumber seperti sistem akademik atau data kehadiran.
   - Melakukan pembersihan data dengan mengatasi nilai duplikat, data kosong (*missing values*), dan memastikan format data konsisten.

2. **Eksplorasi dan Analisis Data (EDA)**
   - Melakukan analisis statistik awal untuk memahami karakteristik siswa dan pola-pola yang mengarah pada *dropout*.
   - Mengidentifikasi fitur-fitur penting seperti IPK, kehadiran, keterlambatan, latar belakang ekonomi, dan prestasi akademik.

3. **Pemodelan Prediktif**
   - Membangun model klasifikasi untuk memprediksi kemungkinan siswa mengalami *dropout*.
   - Menggunakan algoritma machine learning seperti:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - K-Nearest Neighbors (KNN)
     - Support Vector Machine (SVM)
   - Melakukan evaluasi model menggunakan metrik akurasi, precision, recall, dan F1-score.

4. **Pembuatan Dashboard Pemantauan**
   - Mengembangkan dashboard interaktif menggunakan **Looker Studio**.
   - Dashboard menampilkan visualisasi seperti:
     - Distribusi siswa berdasarkan status (aktif/dropout).
     - Performa akademik berdasarkan jurusan, semester, dan gender.
     - Tren *dropout* per periode waktu.
     - Indikator risiko siswa terhadap *dropout* yang dapat difilter berdasarkan variabel tertentu.

5. **Integrasi dan Uji Coba Dashboard**
   - Mengintegrasikan data terbaru ke dalam dashboard secara berkala atau real-time.
   - Melakukan uji coba fungsionalitas untuk memastikan dashboard mudah digunakan oleh pengguna non-teknis.

6. **Pemberian Rekomendasi Strategis**
   - Menyusun saran berbasis hasil analisis untuk mendukung intervensi dini terhadap siswa berisiko tinggi.
   - Rekomendasi diarahkan pada kebijakan pembinaan, bimbingan akademik, dan dukungan psikososial.

7. **Dokumentasi dan Pelatihan**
   - Menyediakan dokumentasi teknis dan panduan penggunaan dashboard.
   - Memberikan pelatihan kepada tenaga pengajar dan staf akademik untuk memaksimalkan pemanfaatan dashboard dalam pengambilan keputusan.

Dengan cakupan proyek ini, diharapkan Jaya Jaya Institut dapat:
- Mendeteksi lebih awal siswa yang berisiko *dropout*.
- Mengambil langkah intervensi yang lebih tepat sasaran.
- Menurunkan angka *dropout* dan meningkatkan tingkat kelulusan secara berkelanjutan.


### Persiapan

**Sumber Data:**  
Dataset yang digunakan dalam proyek ini dapat diakses melalui tautan berikut:  
[Students Performance Data - Dicoding Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup Environment untuk Google Colab:**

Berikut adalah langkah-langkah untuk memulai di **Google Colab**:

1. **Buka Google Colab:**
   - Akses [Google Colab](https://colab.research.google.com/).
   - Buat notebook baru dengan memilih **New Notebook**.

2. **Mengimpor Library yang digunakan**

Untuk memulai proyek ini di **Google Colab**, kita perlu mengimpor beberapa library yang akan digunakan dalam proses data manipulation, visualisasi, preprocessing, pemodelan, dan evaluasi. Berikut adalah daftar library yang akan digunakan:

```python
# 1. Import semua library yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import xgboost as xgb
from sklearn.metrics import accuracy_score
import joblib
```
3. **Menyiapkan Dataset yang Digunakan**

Pada langkah ini, kita akan memulai dengan membaca dataset yang telah disediakan dan melakukan pemeriksaan awal terhadap data yang ada. Dataset ini akan digunakan untuk analisis lebih lanjut.

```python
# Membaca dataset
df = pd.read_csv("/content/drive/MyDrive/Laskar Ai/Data/data_pendidikan/data.csv", sep=';')
```

Setelah membaca dataset, kita akan menampilkan beberapa informasi awal, seperti 5 data teratas, tipe data dari setiap kolom, jumlah nilai unik untuk setiap kolom kategorikal, serta analisis deskriptifnya.

```python
# Menampilkan 5 data teratas
df.head()
```

```python
# Menampilkan informasi tipe data dan missing values
df.info()
```
```python
# Menampilkan jumlah nilai unik tiap kolom kategorikal
print("\nNilai unik untuk kolom kategorikal:")
for col in df.select_dtypes(include='object').columns:
    print(f"{col}: {df[col].nunique()} nilai unik")
```
```python
# Mengecek jumlah nilai NULL
df.isnull().sum()
```
```python
# Menampilkan statistik deskriptif
df.describe()
```

Langkah-langkah ini penting untuk memahami struktur dataset yang kita gunakan serta mengecek adanya data yang hilang (missing values), yang perlu ditangani sebelum melakukan analisis lebih lanjut.

### 4. **Data Preparation / Preprocessing**

Pada tahap ini, dilakukan beberapa langkah persiapan data agar dapat digunakan secara optimal untuk proses analisis dan pemodelan machine learning. Karena dataset yang digunakan tidak memiliki nilai kosong (*missing values*), maka proses pembersihan data lebih difokuskan pada eksplorasi dan transformasi data numerik dan kategorikal.

Langkah pertama adalah mengidentifikasi dan memvisualisasikan distribusi data numerik. Hal ini bertujuan untuk melihat pola penyebaran dan mendeteksi potensi *outlier* pada setiap fitur numerik.

```python
# Kolom numerik
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

# Plot distribusi
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols[:6]):
    plt.subplot(2, 3, i+1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribusi {col}')
plt.tight_layout()
plt.show()
```
Selanjutnya, dilakukan visualisasi data kategorikal untuk mengetahui frekuensi kemunculan tiap kategori dalam kolom yang bersifat kategorikal.

```python
# Kolom kategorikal
categorical_cols = df.select_dtypes(include='object').columns

# Plot frekuensi
plt.figure(figsize=(15, 10))
for i, col in enumerate(categorical_cols[:6]):
    plt.subplot(2, 3, i+1)
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Frekuensi {col}')
    plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```
Kemudian, dilakukan analisis korelasi antar fitur numerik untuk mengetahui hubungan antar variabel menggunakan matriks korelasi.

```python
# Matriks korelasi
plt.figure(figsize=(12, 8))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Matriks Korelasi")
plt.show()
```
Kolom target Status yang semula berupa label kategorikal (Dropout dan Graduate) kemudian dikonversi menjadi nilai numerik menggunakan LabelEncoder.

```python
# Encode target label (Status)
le_status = LabelEncoder()
df['Status'] = le_status.fit_transform(df['Status'])  # Graduate=0, Dropout=1
```
Data kemudian dipisahkan menjadi fitur numerik dan fitur kategorikal. Fitur numerik akan dinormalisasi, dan fitur kategorikal akan diencode agar dapat diterima oleh algoritma machine learning.

```python
# Pisahkan fitur numerik dan kategorikal
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
numerical_cols.remove('Status')  # Jangan encode target

# Encode kolom kategorikal (jika ada)
for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])
```
Terakhir, data dipisahkan menjadi fitur (X) dan target (y), lalu dilakukan standarisasi terhadap fitur numerik menggunakan StandardScaler.

```python
# Fitur dan target
X = df.drop('Status', axis=1)
y = df['Status']

# Standarisasi fitur numerik
scaler = StandardScaler()
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])
```
Dengan preprocessing ini, data sudah siap untuk digunakan dalam proses pelatihan model prediksi status kelulusan siswa. 


5. **Model Training**

Pada tahap ini, kita akan membagi dataset menjadi data pelatihan dan data pengujian. Kemudian, kita akan melatih beberapa model machine learning untuk memprediksi nilai 'Status Siawa' (Apakah Siswa tersebut akan di Dropout/Graduate/Enrolled).

Kita akan membagi dataset menjadi dua bagian: data pelatihan (80%) dan data pengujian (20%).

```python
# Split data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("Jumlah data latih:", X_train.shape)
print("Jumlah data uji:", X_test.shape)
```

Beberapa model machine learning yang akan digunakan untuk melatih data antara lain: Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), dan XGBoost.

```python
# Melatih model
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(),
    'XGBoost': xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
}

# Pelatihan semua model
for name, model in models.items():
    model.fit(X_train, y_train)
```

6. **Menyimpan Hasil Evaluasi Model**

Setelah melatih model, langkah selanjutnya adalah mengevaluasi kinerja masing-masing model menggunakan data pengujian (test data). Evaluasi dilakukan menggunakan metrik-metrik seperti akurasi, precision, recall, dan F1-Score.

**Evaluasi Model Menggunakan Data Pengujian**  
Berikut adalah kode untuk melakukan prediksi menggunakan model yang telah dilatih dan menghitung metrik evaluasi untuk masing-masing model.

```python
# Menyimpan hasil evaluasi
results = []

for name, model in models.items():
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)

    results.append({
        "Model": name,
        "Akurasi": acc,
        "Precision": report['weighted avg']['precision'],
        "Recall": report['weighted avg']['recall'],
        "F1-Score": report['weighted avg']['f1-score']
    })

# Konversi ke DataFrame untuk tampilan tabel
results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by="Akurasi", ascending=False).reset_index(drop=True)

# Tampilkan hasil evaluasi model dalam bentuk tabel
print("📊 Hasil Evaluasi Model:\n")
print(results_df.to_string(index=False))

# Menampilkan model dengan akurasi tertinggi
best_model = results_df.iloc[0]
print(f"\n✅ Model terbaik adalah: {best_model['Model']} dengan akurasi: {best_model['Akurasi']:.4f}")
```

Didapatkan hasil evaluasinya seperti ini :
## 📊 Hasil Evaluasi Model

| Model               | Akurasi | Precision | Recall  | F1-Score |
|---------------------|---------|-----------|---------|----------|
| Random Forest       | 0.7887  | 0.7806    | 0.7887  | 0.7780   |
| Logistic Regression | 0.7684  | 0.7500    | 0.7684  | 0.7531   |
| XGBoost             | 0.7672  | 0.7603    | 0.7672  | 0.7622   |
| SVM                 | 0.7593  | 0.7478    | 0.7593  | 0.7466   |
| Decision Tree       | 0.6870  | 0.6914    | 0.6870  | 0.6891   |
| KNN                 | 0.6667  | 0.6497    | 0.6667  | 0.6557   |

✅ **Model terbaik adalah:** Random Forest dengan akurasi **0.7887**


## Business Dashboard

Dashboard ini merupakan **Dashboard Analitik Mahasiswa** yang bertujuan untuk memvisualisasikan data terkait **status akademik mahasiswa** berdasarkan berbagai faktor seperti status pendaftaran, kelompok usia, jurusan, serta rata-rata nilai semester. Dashboard ini membantu institusi pendidikan dalam memantau performa mahasiswa dan mengidentifikasi potensi masalah seperti dropout.

### Fitur-Fitur Dashboard

1. **Distribusi Mahasiswa Berdasarkan Status**
   - Menampilkan persentase mahasiswa dengan status:
     - **Enrolled**: 49.6%
     - **Dropout**: 32.1%
     - **Graduate**: 17.9%
   - Ditampilkan dalam bentuk diagram lingkaran.

2. **Jumlah Total Mahasiswa**
   - Tercatat sebanyak **4.424 mahasiswa** yang dianalisis dalam dashboard ini.

3. **Nilai Rata-Rata Semester**
   - **Grade Semester 1**: 9,12  
   - **Grade Semester 2**: 11

4. **Status Mahasiswa Berdasarkan Kelompok Usia**
   - Visualisasi menunjukkan distribusi status (Dropout, Graduate, Enrolled) berdasarkan kelompok umur: 17–20, 21–24, 25–29, 30–35, dan >35 tahun.

5. **Rata-Rata Nilai Semester Berdasarkan Status**
   - Menampilkan rata-rata nilai semester 1 dan semester 2 untuk setiap kategori status mahasiswa:
     - Graduate memiliki nilai tertinggi.
     - Dropout memiliki rata-rata nilai terendah.

6. **Status Berdasarkan Jurusan**
   - Perbandingan jumlah mahasiswa berdasarkan status akademik di tiap jurusan, seperti:
     - Management
     - Accounting
     - Engineering
     - Computer Science
     - Others
   - Memberikan wawasan mengenai jurusan dengan tingkat dropout atau kelulusan yang tinggi.

### Akses Dashboard

[Dashboard Looker Studio](https://lookerstudio.google.com/reporting/5a22d124-d64b-4eb9-ab12-281641d97d08)

---

Dashboard ini sangat bermanfaat bagi pihak kampus atau akademik untuk melakukan evaluasi kinerja pendidikan, meningkatkan tingkat kelulusan, dan mengurangi angka putus studi.


## 🚀 Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe sistem machine learning yang telah dibuat, pengguna dapat mengakses aplikasi melalui browser dengan mengunjungi tautan berikut:

🔗 **[Aplikasi Auliya Sabrina](https://submissionakhir-datascience-auliyasbrn.streamlit.app/)**

Aplikasi ini dibuat menggunakan **Streamlit** dan telah di-*deploy* secara online agar dapat diakses oleh siapa saja tanpa perlu menginstal aplikasi secara lokal.

### 🧭 Langkah Penggunaan:

1. Buka tautan aplikasi di atas menggunakan browser.
2. Isi setiap bagian dari form input sesuai dengan penjelasan pada tabel berikut:

---

### 🧾 Langkah-langkah Input Data

| **Field**                      | **Deskripsi**                                                                 |
|-------------------------------|------------------------------------------------------------------------------|
| **Status Pernikahan**          | Pilih status pernikahan mahasiswa *(Single, Married, dsb)*.                  |
| **Application Mode**           | Jalur pendaftaran yang diambil oleh mahasiswa.                              |
| **Application Order**          | Urutan pilihan program studi *(0 = pilihan pertama)*.                        |
| **Course**                     | Jurusan/program studi mahasiswa.                                             |
| **Daytime/Evening Attendance** | Pilih apakah mahasiswa hadir di siang hari atau malam.                      |
| **Previous Qualification**     | Tingkat pendidikan terakhir mahasiswa.                                       |
| **Previous Qualification Grade** | Nilai akhir dari pendidikan sebelumnya *(0 - 200)*.                          |
| **Nationality**                | Kewarganegaraan mahasiswa.                                                  |
| **Mother's Qualification**     | Kualifikasi pendidikan ibu mahasiswa.                                       |
| **Father's Qualification**     | Kualifikasi pendidikan ayah mahasiswa.                                      |
| **Dan seterusnya...**          |

> Setelah semua data diisi, akan muncul tombol untuk mendapatkan hasil **prediksi status mahasiswa**.

---

## 🧠 Output yang Akan Ditampilkan

Setelah seluruh input diberikan:

1. Model akan memproses data yang telah dimasukkan.
2. Status mahasiswa akan ditampilkan sebagai hasil prediksi, berupa:
   - `Graduated`
   - `Dropout`
   - `Enrolled`

---

Sistem ini secara otomatis menjalankan model machine learning yang telah dilatih sebelumnya dan menampilkan hasil analisis secara **interaktif** langsung di browser.



## Conclusion

Proyek ini bertujuan untuk menganalisis data mahasiswa berdasarkan status akademik, kelompok usia, jurusan, dan nilai rata-rata semester. Berdasarkan visualisasi dalam **Student Dashboard Analytic**, ditemukan beberapa temuan penting:

- Mayoritas mahasiswa berada pada status **Enrolled** (49,6%), diikuti oleh **Dropout** (32,1%), dan **Graduate** (17,9%).
- Jumlah mahasiswa tertinggi berada pada kelompok usia **17–20 tahun**, yang didominasi oleh status Dropout dan Enrolled.
- Jurusan tertentu memiliki tingkat Dropout dan Graduate yang signifikan, menunjukkan variasi performa akademik antar program studi.
- Mahasiswa dengan status **Graduate** memiliki **rata-rata nilai semester tertinggi**, sedangkan mahasiswa **Dropout** cenderung memiliki nilai terendah.
- Terdapat peningkatan nilai rata-rata dari Semester 1 (9,12) ke Semester 2 (11), menunjukkan adanya perkembangan akademik.

Secara keseluruhan, dashboard ini memberikan gambaran komprehensif yang dapat digunakan oleh institusi untuk mengevaluasi kualitas pembelajaran, mengidentifikasi potensi masalah akademik, dan merancang strategi peningkatan mutu pendidikan.

---

### Rekomendasi Action Items

- **Program Intervensi Dini untuk Mahasiswa Rentan Dropout**  
  Identifikasi mahasiswa dengan performa rendah dan lakukan pendekatan akademik atau konseling untuk meningkatkan keterlibatan belajar.

- **Analisis Lanjutan Berdasarkan Jurusan**  
  Evaluasi jurusan dengan tingkat Dropout tinggi untuk mengetahui penyebabnya, apakah dari kurikulum, metode pengajaran, atau faktor eksternal lainnya.

- **Optimalisasi Bimbingan Akademik**  
  Tingkatkan peran dosen pembimbing untuk memantau perkembangan mahasiswa dan memberikan dukungan yang tepat waktu.

- **Penyesuaian Strategi Pengajaran Berdasarkan Usia**  
  Sesuaikan pendekatan pembelajaran dengan karakteristik kelompok usia tertentu agar lebih efektif dalam mendorong kelulusan.

- **Pemanfaatan Data Secara Berkelanjutan**  
  Gunakan dashboard ini sebagai alat monitoring berkala untuk pengambilan keputusan berbasis data dalam meningkatkan performa akademik secara menyeluruh.

Dengan implementasi strategi berbasis data ini, diharapkan institusi pendidikan dapat meningkatkan tingkat kelulusan, mengurangi angka dropout, serta menciptakan sistem pendidikan yang lebih adaptif dan responsif.
