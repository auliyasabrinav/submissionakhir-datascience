import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('/model/best_model.joblib')

# Judul aplikasi
st.title('Aplikasi Prediksi Status Mahasiswa')

# Deskripsi aplikasi
st.write("Masukkan data berikut untuk mendapatkan prediksi status mahasiswa (Graduated, Dropout, atau Enrolled).")

# Input Marital Status
marital_status_options = {
    'Single': 1,
    'Married': 2,
    'Widower': 3,
    'Divorced': 4,
    'Facto Union': 5,
    'Legally Separated': 6
}

marital_status = st.selectbox(
    "Status Pernikahan",
    options=list(marital_status_options.keys()),
    help="1 – Single, 2 – Married, 3 – Widower, 4 – Divorced, 5 – Facto Union, 6 – Legally Separated"
)

# Ambil value numeric dari pilihan
marital_status_value = marital_status_options[marital_status]

# Input Application Mode
application_mode_options = {
    '1st phase - general contingent': 1,
    'Ordinance No. 612/93': 2,
    '1st phase - special contingent (Azores Island)': 5,
    'Holders of other higher courses': 7,
    'Ordinance No. 854-B/99': 10,
    'International student (bachelor)': 15,
    '1st phase - special contingent (Madeira Island)': 16,
    '2nd phase - general contingent': 17,
    '3rd phase - general contingent': 18,
    'Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
    'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
    'Over 23 years old': 39,
    'Transfer': 42,
    'Change of course': 43,
    'Technological specialization diploma holders': 44,
    'Change of institution/course': 51,
    'Short cycle diploma holders': 53,
    'Change of institution/course (International)': 57
}

application_mode = st.selectbox(
    "Application Mode",
    options=list(application_mode_options.keys()),
    help="Pilih salah satu jalur masuk mahasiswa"
)

application_mode_value = application_mode_options[application_mode]

# Input Application Order dengan Skala
application_order = st.slider(
    "Application Order",
    min_value=0,
    max_value=9,
    step=1,
    value=0,  # Default nilai awal
    format="%.0f",  # Memastikan angka tampil tanpa desimal
    help="Urutan pilihan program studi saat pendaftaran (0 = pilihan pertama, 9 = pilihan terakhir)"
)

# Input Course
course = st.selectbox(
    "Course",
    options=[
        33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991
    ],
    format_func=lambda x: {
        33: "Biofuel Production Technologies",
        171: "Animation and Multimedia Design",
        8014: "Social Service (evening attendance)",
        9003: "Agronomy",
        9070: "Communication Design",
        9085: "Veterinary Nursing",
        9119: "Informatics Engineering",
        9130: "Equinculture",
        9147: "Management",
        9238: "Social Service",
        9254: "Tourism",
        9500: "Nursing",
        9556: "Oral Hygiene",
        9670: "Advertising and Marketing Management",
        9773: "Journalism and Communication",
        9853: "Basic Education",
        9991: "Management (evening attendance)"
    }[x],
    help="Pilih jurusan yang dipilih oleh mahasiswa."
)

# Input Daytime/Evening Attendance menggunakan Radio Buttons
attendance_type = st.radio(
    "Daytime/Evening Attendance",
    options=[1, 0],  # 1 untuk daytime, 0 untuk evening
    format_func=lambda x: "Daytime" if x == 1 else "Evening",
    help="Pilih apakah jenis kehadiran adalah daytime (1) atau evening (0)."
)

# Input Previous Qualification (Previous Education Level)
previous_qualification = st.selectbox(
    "Previous Qualification (Education Level)",
    options=[
        1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43
    ],
    format_func=lambda x: {
        1: "Secondary education",
        2: "Higher education - bachelor's degree",
        3: "Higher education - degree",
        4: "Higher education - master's",
        5: "Higher education - doctorate",
        6: "Frequency of higher education",
        9: "12th year of schooling - not completed",
        10: "11th year of schooling - not completed",
        12: "Other - 11th year of schooling",
        14: "10th year of schooling",
        15: "10th year of schooling - not completed",
        19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
        38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
        39: "Technological specialization course",
        40: "Higher education - degree (1st cycle)",
        42: "Professional higher technical course",
        43: "Higher education - master (2nd cycle)"
    }.get(x, "Unknown"),
    help="Pilih tingkat pendidikan sebelumnya."
)

# Input Previous Qualification (Grade)
previous_qualification_grade = st.slider(
    "Previous Qualification Grade",
    min_value=0,  # Nilai minimum
    max_value=200,  # Nilai maksimum
    step=1,  # Langkah kenaikan
    help="Masukkan nilai grade dari kualifikasi sebelumnya (antara 0 dan 200)."
)

# Input Nationality
nationality = st.selectbox(
    "Nationality",
    options=[
        1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109
    ],  # Daftar pilihan Nationality (berupa integer)
    format_func=lambda x: {
        1: "Portuguese", 2: "German", 6: "Spanish", 11: "Italian", 13: "Dutch", 14: "English",
        17: "Lithuanian", 21: "Angolan", 22: "Cape Verdean", 24: "Guinean", 25: "Mozambican",
        26: "Santomean", 32: "Turkish", 41: "Brazilian", 62: "Romanian", 100: "Moldova (Republic of)",
        101: "Mexican", 103: "Ukrainian", 105: "Russian", 108: "Cuban", 109: "Colombian"
    }[x],  # Menampilkan nama negara berdasarkan pilihan integer
    help="Pilih kewarganegaraan Anda."
)

# Input Mother's Qualification
mothers_qualification = st.selectbox(
    "Mother's Qualification",
    options=[
        1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44
    ],  # Daftar pilihan qualification (berupa integer)
    format_func=lambda x: {
        1: "Secondary Education - 12th Year of Schooling or Eq.",
        2: "Higher Education - Bachelor's Degree",
        3: "Higher Education - Degree",
        4: "Higher Education - Master's",
        5: "Higher Education - Doctorate",
        6: "Frequency of Higher Education",
        9: "12th Year of Schooling - Not Completed",
        10: "11th Year of Schooling - Not Completed",
        11: "7th Year (Old)",
        12: "Other - 11th Year of Schooling",
        14: "10th Year of Schooling",
        18: "General Commerce Course",
        19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        22: "Technical-Professional Course",
        26: "7th Year of Schooling",
        27: "2nd Cycle of the General High School Course",
        29: "9th Year of Schooling - Not Completed",
        30: "8th Year of Schooling",
        34: "Unknown",
        35: "Can't read or write",
        36: "Can read without having a 4th year of schooling",
        37: "Basic Education 1st Cycle (4th/5th Year) or Equiv.",
        38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        39: "Technological Specialization Course",
        40: "Higher Education - Degree (1st Cycle)",
        41: "Specialized Higher Studies Course",
        42: "Professional Higher Technical Course",
        43: "Higher Education - Master (2nd Cycle)",
        44: "Higher Education - Doctorate (3rd Cycle)"
    }[x],  # Menampilkan deskripsi qualification berdasarkan pilihan integer
    help="Pilih kualifikasi pendidikan ibu Anda."
)

# Input Father's Qualification
fathers_qualification = st.selectbox(
    "Father's Qualification",
    options=[
        1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 22, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44
    ],  # Daftar pilihan qualification (berupa integer)
    format_func=lambda x: {
        1: "Secondary Education - 12th Year of Schooling or Eq.",
        2: "Higher Education - Bachelor's Degree",
        3: "Higher Education - Degree",
        4: "Higher Education - Master's",
        5: "Higher Education - Doctorate",
        6: "Frequency of Higher Education",
        9: "12th Year of Schooling - Not Completed",
        10: "11th Year of Schooling - Not Completed",
        11: "7th Year (Old)",
        12: "Other - 11th Year of Schooling",
        13: "2nd Year Complementary High School Course",
        14: "10th Year of Schooling",
        18: "General Commerce Course",
        19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
        20: "Complementary High School Course",
        22: "Technical-Professional Course",
        25: "Complementary High School Course - Not Concluded",
        26: "7th Year of Schooling",
        27: "2nd Cycle of the General High School Course",
        29: "9th Year of Schooling - Not Completed",
        30: "8th Year of Schooling",
        31: "General Course of Administration and Commerce",
        33: "Supplementary Accounting and Administration",
        34: "Unknown",
        35: "Can't Read or Write",
        36: "Can Read Without Having a 4th Year of Schooling",
        37: "Basic Education 1st Cycle (4th/5th Year) or Equiv.",
        38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
        39: "Technological Specialization Course",
        40: "Higher Education - Degree (1st Cycle)",
        41: "Specialized Higher Studies Course",
        42: "Professional Higher Technical Course",
        43: "Higher Education - Master (2nd Cycle)",
        44: "Higher Education - Doctorate (3rd Cycle)"
    }[x],  # Menampilkan deskripsi qualification berdasarkan pilihan integer
    help="Pilih kualifikasi pendidikan ayah Anda."
)

# Input Mother's Occupation
mothers_occupation = st.selectbox(
    "Mother's Occupation",
    options=[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194
    ],  # Daftar pilihan occupation (berupa integer)
    format_func=lambda x: {
        0: "Student",
        1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
        2: "Specialists in Intellectual and Scientific Activities",
        3: "Intermediate Level Technicians and Professions",
        4: "Administrative Staff",
        5: "Personal Services, Security and Safety Workers and Sellers",
        6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
        7: "Skilled Workers in Industry, Construction and Craftsmen",
        8: "Installation and Machine Operators and Assembly Workers",
        9: "Unskilled Workers",
        10: "Armed Forces Professions",
        90: "Other Situation",
        122: "Health Professionals",
        123: "Teachers",
        125: "Specialists in Information and Communication Technologies (ICT)",
        131: "Intermediate Level Science and Engineering Technicians and Professions",
        132: "Technicians and Professionals, of Intermediate Level of Health",
        134: "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services",
        141: "Office Workers, Secretaries in General and Data Processing Operators",
        143: "Data, Accounting, Statistical, Financial Services and Registry-related Operators",
        144: "Other Administrative Support Staff",
        151: "Personal Service Workers",
        152: "Sellers",
        153: "Personal Care Workers and the Like",
        171: "Skilled Construction Workers and the Like, Except Electricians",
        173: "Skilled Workers in Printing, Precision Instrument Manufacturing, Jewelers, Artisans and the Like",
        175: "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts",
        191: "Cleaning Workers",
        192: "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry",
        193: "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport",
        194: "Meal Preparation Assistants"
    }[x],  # Menampilkan deskripsi occupation berdasarkan pilihan integer
    help="Pilih pekerjaan ibu Anda dari daftar yang tersedia."
)

# Input Father's Occupation
fathers_occupation = st.selectbox(
    "Father's Occupation",
    options=[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 112, 114, 121, 122, 123, 124, 131, 132, 134, 135, 141, 143, 144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 181, 182, 183, 192, 193, 194, 195
    ],  # Daftar pilihan occupation (berupa integer)
    format_func=lambda x: {
        0: "Student",
        1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
        2: "Specialists in Intellectual and Scientific Activities",
        3: "Intermediate Level Technicians and Professions",
        4: "Administrative Staff",
        5: "Personal Services, Security and Safety Workers and Sellers",
        6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
        7: "Skilled Workers in Industry, Construction and Craftsmen",
        8: "Installation and Machine Operators and Assembly Workers",
        9: "Unskilled Workers",
        10: "Armed Forces Professions",
        90: "Other Situation",
        99: "(blank)",
        101: "Armed Forces Officers",
        102: "Armed Forces Sergeants",
        103: "Other Armed Forces Personnel",
        112: "Directors of Administrative and Commercial Services",
        114: "Hotel, Catering, Trade and Other Services Directors",
        121: "Specialists in the Physical Sciences, Mathematics, Engineering and Related Techniques",
        122: "Health Professionals",
        123: "Teachers",
        124: "Specialists in Finance, Accounting, Administrative Organization, Public and Commercial Relations",
        131: "Intermediate Level Science and Engineering Technicians and Professions",
        132: "Technicians and Professionals, of Intermediate Level of Health",
        134: "Intermediate Level Technicians from Legal, Social, Sports, Cultural and Similar Services",
        135: "Information and Communication Technology Technicians",
        141: "Office Workers, Secretaries in General and Data Processing Operators",
        143: "Data, Accounting, Statistical, Financial Services and Registry-related Operators",
        144: "Other Administrative Support Staff",
        151: "Personal Service Workers",
        152: "Sellers",
        153: "Personal Care Workers and the Like",
        154: "Protection and Security Services Personnel",
        161: "Market-oriented Farmers and Skilled Agricultural and Animal Production Workers",
        163: "Farmers, Livestock Keepers, Fishermen, Hunters and Gatherers, Subsistence",
        171: "Skilled Construction Workers and the Like, Except Electricians",
        172: "Skilled Workers in Metallurgy, Metalworking and Similar",
        174: "Skilled Workers in Electricity and Electronics",
        175: "Workers in Food Processing, Woodworking, Clothing and Other Industries and Crafts",
        181: "Fixed Plant and Machine Operators",
        182: "Assembly Workers",
        183: "Vehicle Drivers and Mobile Equipment Operators",
        192: "Unskilled Workers in Agriculture, Animal Production, Fisheries and Forestry",
        193: "Unskilled Workers in Extractive Industry, Construction, Manufacturing and Transport",
        194: "Meal Preparation Assistants",
        195: "Street Vendors (Except Food) and Street Service Providers"
    }[x],  # Menampilkan deskripsi occupation berdasarkan pilihan integer
    help="Pilih pekerjaan ayah Anda dari daftar yang tersedia."
)

# Input Admission Grade
admission_grade = st.number_input(
    "Admission Grade",
    min_value=0.0,
    max_value=200.0,
    step=0.1,
    format="%.1f",
    help="Masukkan nilai ujian masuk antara 0 hingga 200"
)

# Input Displaced
displaced = st.radio(
    "Displaced",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa termasuk displaced student?"
)

# Input Educational Special Needs
educational_special_needs = st.radio(
    "Educational Special Needs",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa memiliki kebutuhan pendidikan khusus?"
)

# Input Debtor
debtor = st.radio(
    "Debtor",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa memiliki tunggakan?"
)

# Input Tuition Fees Up to Date
tuition_up_to_date = st.radio(
    "Tuition Fees Up to Date",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa sudah membayar biaya kuliah tepat waktu?"
)

# Input Gender
gender = st.radio(
    "Gender",
    options=[1, 0],
    format_func=lambda x: "Male" if x == 1 else "Female",
    help="Pilih jenis kelamin mahasiswa"
)

# Input Scholarship Holder
scholarship_holder = st.radio(
    "Scholarship Holder",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa penerima beasiswa?"
)

# Input Age at Enrollment
age_at_enrollment = st.number_input(
    "Age at Enrollment",
    min_value=15,
    max_value=100,
    step=1,
    help="Usia mahasiswa saat mendaftar"
)

# Input International
international = st.radio(
    "International Student",
    options=[1, 0],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="Apakah mahasiswa merupakan mahasiswa internasional?"
)

# ---- Curricular Units - 1st Semester ----
st.subheader("Curricular Units - 1st Semester")

credited_1st = st.number_input(
    "Credited (1st Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang diakui pada semester 1"
)

enrolled_1st = st.number_input(
    "Enrolled (1st Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang diambil pada semester 1"
)

evaluations_1st = st.number_input(
    "Evaluations (1st Sem)",
    min_value=0,
    step=1,
    help="Jumlah evaluasi pada semester 1"
)

approved_1st = st.number_input(
    "Approved (1st Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang lulus pada semester 1"
)

grade_1st = st.number_input(
    "Average Grade (1st Sem)",
    min_value=0.0,
    max_value=20.0,
    step=0.1,
    help="Rata-rata nilai semester 1 (0–20)"
)

without_eval_1st = st.number_input(
    "Without Evaluations (1st Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah tanpa evaluasi di semester 1"
)

# ---- Curricular Units - 2nd Semester ----
st.subheader("Curricular Units - 2nd Semester")

credited_2nd = st.number_input(
    "Credited (2nd Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang diakui pada semester 2"
)

enrolled_2nd = st.number_input(
    "Enrolled (2nd Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang diambil pada semester 2"
)

evaluations_2nd = st.number_input(
    "Evaluations (2nd Sem)",
    min_value=0,
    step=1,
    help="Jumlah evaluasi pada semester 2"
)

approved_2nd = st.number_input(
    "Approved (2nd Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah yang lulus pada semester 2"
)

grade_2nd = st.number_input(
    "Average Grade (2nd Sem)",
    min_value=0.0,
    max_value=20.0,
    step=0.1,
    help="Rata-rata nilai semester 2 (0–20)"
)

without_eval_2nd = st.number_input(
    "Without Evaluations (2nd Sem)",
    min_value=0,
    step=1,
    help="Jumlah mata kuliah tanpa evaluasi di semester 2"
)

# ---- Economic Indicators ----
st.subheader("Economic Indicators")

unemployment_rate = st.number_input(
    "Unemployment Rate (%)",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    help="Tingkat pengangguran dalam persen"
)

inflation_rate = st.number_input(
    "Inflation Rate (%)",
    min_value=-100.0,  # Memungkinkan nilai negatif
    max_value=100.0,
    step=0.1,
    help="Tingkat inflasi dalam persen"
)

gdp = st.number_input(
    "GDP",
    min_value=-1000000.0,  # Memungkinkan nilai negatif
    step=1000.0,
    help="Produk Domestik Bruto"
)


# Tombol untuk melakukan prediksi
if st.button("Prediksi Status"):
    # Membuat DataFrame dari input user
    input_data = pd.DataFrame([[
        marital_status_value,
        application_mode_value,
        application_order,
        course,
        attendance_type,
        previous_qualification,
        previous_qualification_grade,
        nationality,
        mothers_qualification,
        fathers_qualification,
        mothers_occupation,
        fathers_occupation,
        admission_grade,
        displaced,
        educational_special_needs,
        debtor,
        tuition_up_to_date,
        gender,
        scholarship_holder,
        age_at_enrollment,
        international,
        credited_1st,
        enrolled_1st,
        evaluations_1st,
        approved_1st,
        grade_1st,
        without_eval_1st,
        credited_2nd,
        enrolled_2nd,
        evaluations_2nd,
        approved_2nd,
        grade_2nd,
        without_eval_2nd,
        unemployment_rate,
        inflation_rate,
        gdp
    ]], columns=[
        'Marital_status', 'Application_mode', 'Application_order', 'Course',
        'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
        'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
        'Mothers_occupation', 'Fathers_occupation', 'Admission_grade', 'Displaced',
        'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'Gender',
        'Scholarship_holder', 'Age_at_enrollment', 'International',
        'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
        'Unemployment_rate', 'Inflation_rate', 'GDP'
    ])

   # Melakukan prediksi
    prediction = model.predict(input_data)[0]

    # Cek output prediksi
    st.write(f"Output prediksi: {prediction}")

    # Mapping prediksi
    status_mapping = {0: "Enrolled", 1: "Dropout", 2: "Graduated"}  # ✅ perbaikan ejaan
    predicted_status = status_mapping.get(prediction, "Unknown")

    # Menampilkan hasil prediksi dengan warna sesuai
    if predicted_status == "Graduated":
        st.success(f"Status mahasiswa yang diprediksi adalah: **{predicted_status}**")  # Hijau
    elif predicted_status == "Dropout":
        st.error(f"Status mahasiswa yang diprediksi adalah: **{predicted_status}**")    # Merah
    elif predicted_status == "Enrolled":
        st.info(f"Status mahasiswa yang diprediksi adalah: **{predicted_status}**")     # Biru
    else:
        st.warning("Status tidak diketahui.")









