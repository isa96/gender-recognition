# Project 1: Face Recognition (Gender Classification)

Proyek ini menampilkan beragam percobaan arsitektur dan algoritma Convolitional Neural Network (CNN) dalam Computer Vision melalui implementasi klasifikasi gender 
menggunakan dataset CelebA. Dengan memanfaatkan teknik deep learning, model ini dilatih untuk memprediksi gender dengan akurasi berdasarkan atribut wajah.

## 🚀 Sorotan Utama:

    Teknik: Menggunakan teknik computer vision dengan library Tensorflow dan Keras.
    Model: Menggunakan arsitektur model deep learning VGG16, VGG19, GoogleNet, ResNet50 dan ResNet101.
    Kinerja: Mencapai prediksi gender terbaik dan akurat pada arsitektur ResNet50 dan ResNet101.

Jelajahi kode dan hasil untuk mendapatkan wawasan tentang dunia pengenalan wajah dan klasifikasi gender!

📝 Catatan: Proyek ini merupakan bagian dari Bootcamp Computer Vision oleh Indonesia AI.

## ★ Introduction

### Background

Identifikasi gender dari data pengguna menjadi semakin penting dalam berbagai bidng, termasuk dalam bisnis dan privasi. 
Pemodelan deep learning menawarkan pendekatan yang kuat dan adaptif untuk mengatasi tantangan ini, memungkinkan sebuah sistem untuk belajar pola yang 
kompleks dari data yang besar dan bervariasi.

### Problem Statement

Pemodelan deep learning menjanjikan solusi kuat untuk klasifikasi gender, namun terdapat tantangan dari ketidakpastian representasi gender dan 
ketidakseimbangan dataset. Terdapat variasi budaya/ras cukup sulit untuk dikenali, sementara ketidakseimbangan dataset dapat menyebabkan bias. 
Pada repositori ini, kita akan mengeksplorasi upaya untuk mencapai klasifikasi gender yang lebih akurat melalui pemodelan deep learning.
  
## ★ Getting Started

### 1. Data collection & Preparation

#### 🔍 Dataset : [CelebA (Celebrity Faces Attributes)](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

Dataset diambil dari CelebA (Celebrity Faces Attributes), Dataset merupakan kumpulan data gambar wajah selebriti yang terdiri dari 200 ribu gambar wajah dari 
kurang lebih 10 ribu selebriti yang berbeda dengan 40 list attribute menjadi dasar proyek ini. Dalam pemrosesan kami menyaring data sebanyak 5000 gambar 
dengan attribute ‘Male’ yang merepresentasikan kelas Male dan Female. Kemudian menganalisis jumlah sebaran data dan melakukan split data menjadi data training, 
validation dan testing.

### 2. Data Augmentation 

Untuk meningkatkan keragaman dataset pelatihan dan meningkatkan ketangguhan model, teknik augmentasi data berikut diterapkan selama preprocessing gambar:

    rescale=1.0 / 255 (Normalization)
    rotation_range=20
    width_shift_range=0.2
    height_shift_range=0.2
    horizontal_flip=True
    validation_split=0.2

Strategi augmentasi ini berkontribusi pada dataset pelatihan yang lebih beragam dan umum, meningkatkan kemampuan model untuk belajar dan berperforma baik pada berbagai input.

### 3. Model Development

#### * Base Model :

##### VGG19:
- Merupakan model arsitektur Convolutional Neural Network (CNN) yang dikembangkan oleh Visual Graphics Group (VGG) dari Universitas Oxford.
- Memiliki 19 layer, termasuk lapisan konvolusi dan lapisan fully connected.
- Dikenal dengan struktur yang dalam dan simetris.

##### VGG16
- Serupa dengan VGG19, VGG16 adalah model arsitektur CNN yang dikembangkan oleh Visual Graphics Group (VGG) dari Universitas Oxford.
- Memiliki 16 layer, termasuk lapisan konvolusi dan lapisan fully connected.
- Digunakan dalam banyak tugas penglihatan komputer dan pengenalan gambar.

##### ResNet50
- ResNet50 adalah bagian dari keluarga model ResNet (Residual Network) yang dikembangkan oleh Microsoft Research.
- Memiliki 50 layer dan dikenal dengan penggunaan blok residu, yang memudahkan pelatihan model yang sangat dalam.

##### ResNet101
- Mirip dengan ResNet50, ResNet101 adalah versi yang lebih besar dengan 101 layer.
- Didesain untuk mengatasi masalah degradasi kinerja yang mungkin terjadi pada model yang sangat dalam.

##### GoogleNet 
- GoogleNet, atau Inception, adalah model arsitektur CNN yang dikembangkan oleh Google.
- Terkenal dengan penggunaan modul Inception, yang menggunakan filter konvolusi dengan berbagai ukuran.

#### * Hyperparameter :

Dalam proyek ini, beberapa hyperparameter dikonfigurasi untuk mengoptimalkan kinerja model. Berikut adalah beberapa hyperparameter yang digunakan :

    Optimizer: Adam
    Learning rate: 0.0001
    Image Size: 218 x 178
    Batch Size: 32
    Epoch : 25
    Callbacks: Early Stopping, Model Checkpoint
    Loss Function : Binary Crossentropy
    Metrics : Accuracy

### 4. Training & Optimization

Pada tahap ini, dilakukan pelatihan dan optimasi model menggunakan beberapa arsitektur dan algoritma yang berbeda, 
yaitu VGG16, VGG19, ResNet50, ResNet101, dan GoogleNet. Proses ini dilakukan untuk mencari arsitektur yang memberikan hasil terbaik pada dataset CelebA 
untuk tujuan klasifikasi gender.

#### * Proses Pelatihan

    Setiap model diinisialisasi dengan Class Weight (Female : 0.833, Male : 1.25) untuk mengimbangi Imbalance Data
    3200 data gambar dengan beragam augmentasi digunakan untuk melatih model.
    Pengoptimalan dilakukan dengan fine tuning dan dan menggunakan algoritma transfer learning.

#### * Evaluasi Model

Setelah pelatihan, model dievaluasi menggunakan dataset validasi untuk mengukur akurasi hasil prediksi. Hasil evaluasi ini mencakup akurasi validasi 
dari setiap arsitektur model yang diuji.


## ★ The Results

### Perbandingan Test Results

Pada tahap ini, hasil pengujian model dari setiap algoritma pengoptimalan fine tuning dan transfer learning dibandingkan untuk mendapatkan pemahaman yang lebih baik 
tentang kinerja relatif masing-masing model. Grafik di bawah ini memvisualisasikan hasil pengujian dari setiap algoritma pada dataset CelebA. 
Data yang diukur adalah akurasi test pada setiap algoritma selama pengujian. 


Dari hasil train dan evaluation, terlihat bahwa ResNet50 dan ResNet101 mencapai akurasi validasi yang relatif sama dan merupakan yang tertinggi dari 
pengoptimalan fine tuning dengan selisih hanya 0,10%, hal ini menunjukkan bahwa arsitektur ini berkemungkinan besar menjadi pilihan terbaik 
untuk tugas klasifikasi gender pada dataset CelebA.

### Inference Time

Pada tahap ini, waktu inference dari setiap arsirtektur diperhitungkan untuk membandingkan kecepatan model dalam memproses data uji. 
Berikut data inference time pada setiap model dari pengujian fine tuning dan transfer learning :

    Fine Tuning :
    VGG19 : 12 s
    VGG16 : 12 s
    ResNet50: 13 s
    ResNet101: 12 s
    GoogleNet: 14s

    Transfer Learning  :   
    VGG19 : 17 s
    VGG16 : 15 s
    ResNet50: 14 s
    ResNet101: 13 s
    GoogleNet: 12s
