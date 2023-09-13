Nama    : Elena Zahra Kurniawan

NPM     : 2206824060

Kelas   : PBP F

>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 Membuat sebuah proyek Django baru.
 Saya membuat sebuah direktori baru dengan nama geprek_lensu dan membuat repositori GitHub baru dengan nama geprek-lensu. Lalu, saya menginisiasi direktori geprek_lensu sebagai repositori Git. Untuk mengisolasi package dan dependencies dari aplikasi, saya membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan perintah `env\Scripts\activate.bat`. Kemudian, saya membuat berkas requirements.txt dengan beberapa dependencies untuk kemudian memasangkannya dengan perintah `pip install -r requirements.txt`. Lalu proyek Django saya dapat dibuat dengan perintah `django-admin startproject geprek_lensu .`. Agar semua host dapat mengakses aplikasi web dan aplikasi web dapat diakses secara luas, saya menetapkan nilai `["*]` pada `ALLOWED_HOST` yang terdapat di `settings.py`. Kemudian, saya menjalankan server Django dan membuka situs http://localhost:8000 guna memastikan bahwa aplikasi Django saya telah berhasil dibuat.

 Membuat aplikasi dengan nama main pada proyek tersebut.
>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Berdasarkan pengertian, virtual environment merupakan sebuah alat yang membantu pengembang perangkat lunak untuk membuat lingkungan yang terisolasi dan terpisah untuk setiap proyek python. Melalui alat ini, pengembang dapat mengunduh kumpulan library yang dibutuhkan untuk proyek aplikasi tertentu tanpa mengganggu proyek aplikasi lainnya. Kita menggunakan dan membutuhkan virtual environment untuk mencegah terjadinya masalah atau konflik yang terjadi saat terdapat library atau package yang berbeda. Dengan memisahkan package yang digunakan pada satu proyek dengan proyek lainnya, virtual environment dapat menjaga keteraturan proyek sehingga kode lebih mudah untuk dikelola.

Kita bisa saja membuat suatu aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, pengembang akan cenderung merasa kesulitan untuk menghadapi dependensi yang berkonflik dan kesulitan dalam mengelola paket Python yang beragam untuk proyek yang berbeda-beda.
>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang menangani tampilan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini akan mengirim input pengguna kepada controller hingga nantinya dapat menciptakan tampilan aplikasi yang dinamis. Komponen ini juga menyajikan data yang sesuai kepada pengguna.
-- Controller: Sebuah komponen yang menjadi penghubung antara Model dan View. Komponen ini akan menerima input dari pengguna melalui View dan memproses permintaan “Get Data” dari model dan meneruskan hasil perbaharuannya untuk ditunjukkan kepada pengguna.

MVT (Model View Template)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang akan menampilkan data kepada pengguna. Komponen ini berisi logika yang menentukan bagaimana suatu data dipresentasikan.
- Template: Sebuah komponen yang menghasilkan tampilan HTML dalam aplikasi web berbasis Django. Komponen ini digunakan untuk memisahkan kode HTML dari logika Python ke dalam aplikasi.

MVVM (Model View ViewModel)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang digunakan sebagai tampilan antarmuka. Komponen ini akan menampilkan data yang telah diproses sebelumnya serta mengirimkan input pengguna ke ViewModel.
- ViewModel: Sebuah komponen yang menjadi perantara antara View dan Model. Komponen ini mengambil data dari Model dan mengubahnya menjadi tampilan yang diinginkan oleh View. Komponen ini juga berisikan perintah yang dapat digunakan oleh View untuk memengaruhi Model.

Perbedaan pada MVC, MVT, dan MVVM di antaranya MVC lebih umum digunakan dalam pengembangan aplikasi berbasis web dan desktop dengan tingkat kompleksitas yang beragam, sementara MVT merupakan varian dari MVC yang ditemukan pada kerangka kerja Django, terutama untuk pengembangan aplikasi web dengan fokus manajemen konten, dan MVVM umum digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang kompleks. Selain itu, MVC mengatur aliran data dari Model ke View Melalui Controller, sementara MVT mengaturnya dari Model ke Template untuk ditampilkan, dan MVVM mengaturnya dari Model ke ViewModel serta mengikat data ke View.
