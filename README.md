Nama    : Elena Zahra Kurniawan

NPM     : 2206824060

Kelas   : PBP F

>Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat sebuah proyek Django baru.
 Saya membuat sebuah direktori baru dengan nama geprek_lensu dan membuat repositori GitHub baru dengan nama geprek-lensu. Lalu, saya menginisiasi direktori geprek_lensu sebagai repositori Git. Untuk mengisolasi package dan dependencies dari aplikasi, saya membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan perintah `env\Scripts\activate.bat`. Kemudian, saya membuat berkas requirements.txt dengan beberapa dependencies untuk kemudian memasangkannya dengan perintah `pip install -r requirements.txt`. Lalu proyek Django saya dapat dibuat dengan perintah `django-admin startproject geprek_lensu .`. Agar semua host dapat mengakses aplikasi web dan aplikasi web dapat diakses secara luas, saya menetapkan nilai `["*]` pada `ALLOWED_HOST` yang terdapat di `settings.py`. Kemudian, saya menjalankan server Django dan membuka situs http://localhost:8000 guna memastikan bahwa aplikasi Django saya telah berhasil dibuat.

- Membuat aplikasi dengan nama main pada proyek tersebut.
Saya menjalankan perintah `python manage.py startapp main` untuk membentuk sebuah direktori baru bernama `main`. Selanjutnya, saya menambahkan `main` ke dalam sebuah variabel bernama `INSTALLED_APPS` yang terdapat pada `settings.py` untuk mendaftarkan aplikasi `main` ke dalam proyek geprek lensu.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main
 Saya mengimport fungsi `include` pada berkas `urls.py`  yang terdapat pada direktori `geprek_lensu`. Untuk mengarahkan path `main/` ke rute yang diimpor dari aplikasi, saya menambahkan rute URL `path('main/', include('main.urls'))`. Berkas `urls.py` pada proyek memungkinkan aplikasi pada proyek Django bersifat modular.

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
 Pada berkas `models.py`, saya menambahkan atribut dengan tipe data yang sesuai dengan kebutuhan aplikasi saya, misalnya menu dengan tipe data CharField, price dan stock dengan tipe data IntegerField, dan description dengan tipe data TextField. Saya juga menambahkan fungsi untuk menambahkan stock dengan nama fungsi `add_stock` dan mengurangi stock dengan cara memesan dengan fungsi `order`. Untuk memigrasi model yang saya telah buat, saya menjalankan perintah `python manage.py makemigrations` dan menerapkan migrasi ke basis data lokal dengan perintah `python manage.py migrate`

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya memodifikasi berkas `views.py` dengan menambahkan `from django.shortcuts import render` untuk tampilan HTML. Saya juga menambahkan fungsi `show main` dengan perintah di bawah ini untuk mengambil data dari model Item dan akan dirender ke template HTML.
`from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Geprek Lensu',
        'name': 'Elena Zahra Kurniawan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)`

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Pada bagian ini, saya melakukan sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py` dengan perintah:

`from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]`
Kode ini bertujuan untuk mendefinisikan sebuah pola URL di aplikasi dengan namespace 'main`. Ketika URL akar diakses, fungsi `show_main` dalam modul `views` akan dipanggil dan URL yag bernama `show_main` ini dapat digunakan untuk mengacu pada URL tersebut dalam aplikasi.

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Selanjutnya, saya membuat akun Adaptable yang terhubung dengan akun GitHub dan melakukan proses deployment sehingga aplikasi saya dapat diakses secara luas.

- Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
Setelah menyelesaikan semua langkah di atas, saya menjawab beberapa pertanyaan pada file README.md dan melakukan add, commit, dan push ke repositori GitHub.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](https://github.com/elenazahrak/geprek-lensu/assets/125001077/57fd8514-74ae-474e-98b6-bf7ea4613171)
Pertama, client akan melakukan permintaan (request) dengan mengakses URL tertentu pada aplikasi web kita. URL yang diminta akan dicocokkan dengan pola yang didefinisikan pada `urls.py`. Setelah itu, `urls.py` akan mencocokkan URL yang diminta dengan pola yang didefinisikan. Bila sudah cocok, `views.py` akan dipanggil dan menjalankan logika berdasarkan permintaan yang diterima. Hal ini bisa dengan mengambil atau memanipulasi data menggunakan `models.py` serta melakukan render template HTML dengan data tersebut. `Models.py` akan digunakan untuk berinteraksi dengan basis data jika diperlukan.  Kemudian, template HTML akan digunakan untuk melakukan proses render halaman web yang akan dikirimkan sebagai sebuah tanggapan ke client.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Berdasarkan pengertian, virtual environment merupakan sebuah alat yang membantu pengembang perangkat lunak untuk membuat lingkungan yang terisolasi dan terpisah untuk setiap proyek python. Melalui alat ini, pengembang dapat mengunduh kumpulan library yang dibutuhkan untuk proyek aplikasi tertentu tanpa mengganggu proyek aplikasi lainnya. Kita menggunakan dan membutuhkan virtual environment untuk mencegah terjadinya masalah atau konflik yang terjadi saat terdapat library atau package yang berbeda. Dengan memisahkan package yang digunakan pada satu proyek dengan proyek lainnya, virtual environment dapat menjaga keteraturan proyek sehingga kode lebih mudah untuk dikelola.

Kita bisa saja membuat suatu aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, pengembang akan cenderung merasa kesulitan untuk menghadapi dependensi yang berkonflik dan kesulitan dalam mengelola paket Python yang beragam untuk proyek yang berbeda-beda.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang menangani tampilan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini akan mengirim input pengguna kepada controller hingga nantinya dapat menciptakan tampilan aplikasi yang dinamis. Komponen ini juga menyajikan data yang sesuai kepada pengguna.
- Controller: Sebuah komponen yang menjadi penghubung antara Model dan View. Komponen ini akan menerima input dari pengguna melalui View dan memproses permintaan “Get Data” dari model dan meneruskan hasil perbaharuannya untuk ditunjukkan kepada pengguna.

MVT (Model View Template)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang akan menampilkan data kepada pengguna. Komponen ini berisi logika yang menentukan bagaimana suatu data dipresentasikan.
- Template: Sebuah komponen yang menghasilkan tampilan HTML dalam aplikasi web berbasis Django. Komponen ini digunakan untuk memisahkan kode HTML dari logika Python ke dalam aplikasi.

MVVM (Model View ViewModel)
- Model: Sebuah komponen yang menggambarkan logika bisnis dan status data yang ada di dalam aplikasi. Komponen ini akan mengelola dan memanipulasi data, berinteraksi dengan database, hingga memperbarui tampilan pada aplikasi yang dikembangkan.
- View: Sebuah komponen yang digunakan sebagai tampilan antarmuka. Komponen ini akan menampilkan data yang telah diproses sebelumnya serta mengirimkan input pengguna ke ViewModel.
- ViewModel: Sebuah komponen yang menjadi perantara antara View dan Model. Komponen ini mengambil data dari Model dan mengubahnya menjadi tampilan yang diinginkan oleh View. Komponen ini juga berisikan perintah yang dapat digunakan oleh View untuk memengaruhi Model.

Perbedaan pada MVC, MVT, dan MVVM di antaranya MVC lebih umum digunakan dalam pengembangan aplikasi berbasis web dan desktop dengan tingkat kompleksitas yang beragam, sementara MVT merupakan varian dari MVC yang ditemukan pada kerangka kerja Django, terutama untuk pengembangan aplikasi web dengan fokus manajemen konten, dan MVVM umum digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna yang kompleks. Selain itu, MVC mengatur aliran data dari Model ke View Melalui Controller, sementara MVT mengaturnya dari Model ke Template untuk ditampilkan, dan MVVM mengaturnya dari Model ke ViewModel serta mengikat data ke View.

>Tugas 3

**1. Apa perbedaan antara form POST dan form GET dalam Django?**
   
Dalam Django, form POST dan form GET merupakan dua metode yang berbeda yang dapat digunakan untuk mengirimkan data dari browser pengguna ke server Django. Form POST biasanya digunakan untuk mengirimkan data yang akan dimasukkan atau diubah pada server, sedangkan Form GET biasanya digunakan untuk mengambil data dari server. Form POST tidak memiliki batasan panjang data yang dapat dikirim dan cocok untuk mengirimkan jumlah data yang lebih besar, lain halnya dengan form GET yang panjang URL dan data yang dapat dikirimkannya dibatasi oleh batasan server web dan browser dan lebih cocok untuk mengirimkan jumlah data yang lebih sedikit. Dari segi keamanan, form POST lebih aman untuk mengirimkan data-data sensitif karena data disertakan dalam tubuh permintaan HTTP dan tidak terlihat dalam URL, tidak seperti form GET yang datanya terlihat di URL serta dapat dengan mudah dilihat dan dicuri siapapun sehingga kurang aman untung data-data sensitif.

**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah dalam tujuan dan struktur datanya. XML dirancang untuk menyimpan dan mengirim data yang terstruktur. Tidak adanya aturan khusus dalam representasi data membuat XML dianggap tidak efisien dalam kecepatan pengiriman data. Lain halnya dengan JSON yang digunakan untuk pertukaran data antara aplikasi dengan format teks yang ringkas dan mudah dibaca. JSON sering digunakan dalam pengembangan aplikasi web, misalnya untuk pertukaran data dalam API web serta komunikasi antara browser dan server. JSON merepresentasikan data dalam bentuk key-value pairs dengan menggunakan sintaks objek JavaScript. JSON dinilai lebih efisien dalam parsing data dibandingkan dengan XML. Lain halnya lagi dengan HTML yang membuat dan menyajikan tampilan serta konten pada halaman web. Konten yang dimaksud dapat berupa teks, gambar, tautan, dan lain sebagainya. Berbeda dengan XML dan JSON yang menyimpan atau melakukan pertukaran data, fokus HTML lebih mengarah pada representasi tampilan.

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
   
JSON dinilai lebih cepat dan efisien dalam mengolah data karena format JSON memiliki hirarki data yang lebih jelas dan jumlah baris kode yang jauh lebih sedikit. Penulisan kodenya yang tidak memerlukan terlalu banyak karakter membuat data lebih cepat tiba di server. Selain itu, hampir semua browser modern yang ada saat ini dapat memproses data JSON dan mengakses website dengan baik dan lancar.

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
   
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

Pada tahap ini, saya membuat sebuah form input data yang memungkinkan saya untuk memasukkan objek data baru yang akan ditampilkan pada halaman utama aplikasi. Saya membuat file baru bernama `forms.py` dan menambahkan beberapa kode, serta mengisi bagian fields dengan model yang saya gunakan, yaitu ["menu", "price", "stock", "description"].

- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Pada bagian ini, saya menambahkan beberapa import pada berkas `views.py` yang terdapat pada folder main. Untuk mengelola proses pengisian formulir dan penyimpanan data produk, saya membuat fungsi baru bernama `create_product`. Saya juga melakukan perubahan pada fungsi `show_main` guna menampilkan data produk yang telah disimpan pada database dan nambahkan import fungsi `create_product` pada `urls.py`. Kemudian, saya membuat berkas `create_product.html` untuk menambahkan elemen-elemen yang dibutuhkan saat menampilkan form input data. Saya juga melakukan modifikasi pada main.html supaya data produk dapat ditampilkan dalam bentuk tabel dan juga menambahkan tombol “Klik untuk Menambahkan Menu” yang akan terhubung ke page form.

Selanjutnya, saya menambahkan lagi beberapa import pada berkas `views.py` yang terdapat pada folder main. Kemudian, saya menambahkan beberapa fungsi seperti `show_xml` dan `show_json` untuk mengambil data dari model “Product" dan menyimpannya dalam sebuah variabel dan menambahkan beberapa import untuk fungsi yang telah saya buat sebelumnya pada file `urls.py`.

Untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON, saya membuat dua fungsi baru bernama `show_xml_by_id` dan `show_json_by_id` dengan parameter “request” dan “id” pada file `views.py`. Kemudian, di dalam fungsi-fungsi tersebut, saya membuat variabel yang akan digunakan untuk menyimpan hasil dari permintaan query data berdasarkan ID tertentu yang ada dalam model “Product”. Saya juga menambahkan “return” untuk mengembalikan HttpResponse yang berisi parameter “data” yang sudah di-serialize menjadi format XML atau JSON. Selanjutnya, pada file `urls.py`, saya menambahkan beberapa import untuk fungsi yang telah saya buat sebelumnya.

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Dalam pembuatan routing URL untuk views pada HTML, saya menambahkan path url ke dalam `urlpatterns` untuk dapat mengakses fungsi. Untuk menguji form input data produk yang telah dibuat sebelumnya, saya menjalankan proyek Django dengan perintah `python manage.py runserver` dan membuka http://localhost:8000 pada browser.
Dalam pembuatan routing URL untuk views pada XML dan JSON,  saya menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi-fungsi tersebut. Terakhir, saya menjalankan proyek Django menggunakan perintah `python manage.py runserver `dan membuka http://localhost:8000/xml atau http://localhost:8000/json pada browser untuk melihat hasilnya.
Mengulang hal yang sama,  saya menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi-fungsi tersebut. Terakhir, saya menjalankan proyek Django menggunakan perintah  `python manage.py runserver` dan membuka  http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] pada browser untuk melihat hasilnya. [id] diisi dengan ID yang ingin kita akses.

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

Setelah menyelesaikan semua langkah di atas, saya menjawab beberapa pertanyaan pada file README.md.

- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

<img width="960" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/7abc1be8-5425-4cd1-a897-ef62ffc2e5db">
<img width="960" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/139b0cd1-1cf3-49f3-be82-3be69d91d627">
<img width="958" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/faa4cfc8-eef5-4eb6-aa7c-f76af751295a">
<img width="960" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/84678b6e-965d-4d67-82c1-577bbac2c64c">
<img width="959" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/c71533db-1fcb-4501-a277-bf15a631be50">

- [x] Melakukan add-commit-push ke GitHub.

Terakhir, saya melakukan add, commit, dan push ke GitHub dengan perintah:
```git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```

>Tugas 4

**1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
   
Django UserCreationForm merupakan built-in forms yang disediakan oleh Django yang dapat digunakan untuk membuat formulir pendaftaran pengguna pada aplikasi web yang menggunakan framework Django. Secara khusus, UserCreationForm digunakan untuk mengumpulkan informasi-informasi yang diperlukan ketika kita ingin membuat akun untuk pengguna baru. UserCreationForm memiliki tiga fields, di antaranya username (nama pengguna), password1 (kata sandi), dan password2 (konfirmasi kata sandi).

Keberadaan UserCreationForm ini memudahkan pengguna untuk dapat menggunakan formulir yang telah disediakan oleh Django secara default tanpa perlu membuat dan menulis formulir dari awal. UserCreationForm juga dapat memastikan bahwa data yang dimasukkan oleh pengguna telah sesuai dengan data yang diminta, misalnya validasi tingkat keamanan password yang dimasukkan. Formulir ini juga telah terhubung dengan User atau model pengguna bawaan Django sehingga data pengguna dapat tersimpan pada database dengan lebih mudah tanpa harus menggunakan kode tambahan. Meskipun demikian, Django UserCreationForm juga memiliki beberapa kelemahan. UserCreationForm tidak cocok digunakan untuk kebutuhan khusus yang memerlukan aliran pendaftaran pengguna yang rumit karena formulir ini dirancang untuk penggunaan umum. Jika kita memiliki kebutuhan khusus, kita perlu menyesuaikannya atau membuat formulir pendaftaran khusus sesuai dengan kebutuhan kita. Di samping itu, tampilan default pada UserCreationForm mungkin tidak cocok dengan desain antarmuka aplikasi web kita sehingga perlu disesuaikan agar sesuai dengan gaya desain yang kita inginkan. Kemudian, beberapa hal terkait keamanannya masih perlu diperhatikan, misalnya perlindungan terhadap serangan brute-force atau serangan injeksi.

**2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

Berdasarkan pengertiannya, autentikasi merupakan proses verifikasi identitas pengguna guna memastikan bahwa pengguna yang mengakses aplikasi adalah identitas yang mereka klaim, sedangkan otorisasi merupakan proses untuk mengatur hak akses pengguna terhadap tindakan tertentu yang terdapat dalam aplikasi. Pada Django, autentikasi biasanya dilakukan dengan memeriksa kredensial pengguna, misalnya username dan password melalui UserAuthentication atau autentikasi yang serupa. Melalui proses autentikasi, pengguna dapat login ke aplikasi, verifikasi identitas, dan identifikasi sesi mereka. Lain halnya dengan otorisasi yang pada Django sering kali dilakukan dengan menggunakan decorator, misalnya @login_required untuk membatasi akses ke tampilan atau dengan menerapkan aturan izin pada objek-model Django. Proses otorisasi ini memastikan bahwa pengguna hanya dapat melihat serta menyunting data sesuai dengan peran atau izin yang mereka miliki.

Proses autentikasi dan otorisasi dalam Django menjadi sangat penting untuk menjaga keamanan aplikasi website. Kedua proses ini memastikan bahwa hanya pengguna yang diizinkan yang dapat mengakses data atau fitur tertentu yang terdapat pada website. Tidak hanya itu, melalui proses otorisasi, kita dapat mengontrol pengguna-pengguna tertentu yang memiliki hak akses ke data krusial dalam aplikasi kita.

**3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

Cookies merupakan kumpulan informasi yang disimpan pada komputer pengguna yang berisi rekam jejak dan aktivitas mereka ketika mengunjungi sebuah situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan data pada perangkat pengguna agar data tersebut dapat diakses dan digunakan oleh server web saat pengguna mengunjungi situs di lain waktu. Cookies sering kali digunakan untuk tujuan seperti menyimpan informasi autentikasi, melacak perilaku pengguna, menyimpan referensi atau pengaturan pengguna, dan mengumpulkan data analitik tentang penggunaan situs web. Dalam framework Django, Django menggunakan cookies untuk mengatur data sesi pengguna melalui sebuah fitur bernama “Django session Framework”. Pertama-tama, sistem akan membuat sesi unik untuk seorang pengguna yang sedang mengunjungi situs web Django. Setelah itu, data sesi pengguna akan tersimpan dalam objek session yang terkait dengan pengguna. Nantinya, yang akan tersimpan pada server Django adalah data sesinya, dan yang tersimpan pada sisi klien adalah ID sesi yang unik. Dengan begitu, ketika pengguna mengunjungi situs web kembali, cookie sesi akan dikirimkan ke server dan ID SESI akan digunakan oleh Django untuk mengambil data sesi pengguna yang sesuai dari server.

**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

Tentu terdapat beberapa risiko potensial yang patut diwaspadai saat kita menggunakan cookies dalam pengembangan web. Jika cookies tidak dikelola dengan baik, cookies dapat disalahgunakan oleh pihak-pihak yang tidak memiliki hak akses yang sah untuk melacak perilaku pengguna. Informasi yang terkandung dalam cookies juga sering kali merupakan data krusial dan sensitif, misalnya ID sesi atau token otentikasi. Jika cookies ini tidak dilindungi dengan baik, maka data-data ini rawan diserang dan dicuri oleh pihak yang tidak berwenang. Selain itu, terdapat beberapa serangan yang sudah cukup umum dalam konteks serangan cookies, di antaranya serangan XSS dan serangan CSRF. Serangan XSS (Cross Site Scripting) merupakan serangan keamanan yang melibatkan penempatan kode berbahaya di sisi klien ke halaman web. Di sisi lain, serangan CSRF (Cross Site Request Forgery) merupakan tipe serangan eksploitasi web yang memaksa pengguna untuk secara tidak sadar mengirimkan permintaan ke situs web tertentu melalui situs web yang mereka akses saat itu sehingga aplikasi web akan menjalankan permintaan tersebut, meskipun itu bukan keinginan pengguna. 

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Untuk mengimplementasikan fungsi registrasi, pertama-tama saya menjalankan virtual Environment saya terlebih dahulu dan membuka berkas `views.py` yang terdapat pada subdirektori `main`. Kemudian, saya menambahkan beberapa import modul seperti `redirect`, `UserCreationForm`, dan `messages`. UserCreationForm akan memudahkan saya dalam membuat formulir pendaftaran pengguna pada aplikasi web saya. Lalu, membuat sebuah fungsi bernama `register` untuk membuat formulir registrasi dan membuat akun pengguna ketika data pada formulir tersebut di-submit. Selanjutnya, saya membuat berkas baru bernama `register.html` pada folder `main/templates` dan mengisinya dengan beberapa kode. Saya juga mengimpor dan menghubungkan fungsi `register` ke dalam berkas `urls.py` di subdirektori `main` dengan menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi yang telah diimpor sebelumnya.

Untuk mengimplementasikan fungsi login, pertama-tama saya membuka berkas `views.py` pada subdirektori `main` untuk membuat sebuah fungsi baru bernama `login_user`. Sebelumnya, saya mengimport beberapa modul untuk mengautentikasi pengguna dan menjalankan proses login ketika autentikasi berhasil. Setelah itu, saya menambahkan potongan kode pada fungsi `login_user` untuk mengautentikasi pengguna yang berusaha untuk masuk ke dalam sistem. Saya juga membuat berkas baru bernama `login.html` pada direktori `main/templates sebagai tampilan pada halaman login. Terakhir, saya mengimpor dan menghubungkan fungsi `login_user` ke dalam berkas `urls.py` di subdirektori main dengan menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi yang telah diimpor sebelumnya.

Untuk mengimplementasikan fungsi logout, pertama-tama saya membuka berkas `views.py` pada subdirektori `main` dan mengimpor modul logout untuk mengakses fungsionalitas logout. Saya juga membuat fungsi bernama `logout_user` dan mengisi fungsi tersebut dengan perintah `logout(request)` dan `return redirect(‘main:login’)`. Perintah `logout(request)` digunakan untuk menghapus sesi pengguna setelah melakukan login dan `return redirect(‘main:login’)` berperan untuk mengarahkan pengguna kembali ke halaman login setelah logout. Setelah itu, saya memodifikasi berkas `main.html` pada folder `main/templates` dengan menambahkan tombol Logout setelah hyperlink untuk “Add New Product” pada halaman utama. Terakhir, saya mengimpor dan menghubungkan fungsi `logout_user` ke dalam berkas `urls.py` di subdirektori main dengan menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi yang telah diimpor sebelumnya.

Untuk membatasi akses ke halaman utama, saya menambahkan beberapa potongan kode pada berkas `views.py` dengan menambahkan impor modul `login_required` untuk mewajibkan pengguna melakukan login dan menambahkan decorator `@login_required(login_url='/login')` di atas fungsi `show_main` supaya pengguna yang dapat mengakses halaman utama hanyalah pengguna yang sudah login. Terakhir, saya menjalankan perintah `python manage.py runserver` dan membuka situs http://localhost:8000/  untuk memastikan bahwa pengguna terarahkan ke tampilan login.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Pada bagian ini, saya membuat akun baru dengan memasukkan username, password, dan melakukan konfirmasi password sesuai ketentuan yang tertulis pada halaman login. Setelah memenuhi kriteria tersebut, saya berhasil masuk ke laman produk dan dapat menambahkan produk pada akun saya.
![Untitled design (2)](https://github.com/elenazahrak/geprek-lensu/assets/125001077/6442ba3f-bb9c-42ee-b07c-20d93b912ce3)

- [x] Menghubungkan model Item dengan User.

Pertama-tama, saya mengimport model yang dibutuhkan pada berkas `models.py` yang terletak di dalam subdirektori `main`. Kemudian, saya menambahkan potongan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model Product saya.  Potongan kode ini akan menghubungkan setiap produk dengan pengguna melalui hubungan ForeignKey. ForeignKey menunjukkan bahwa setiap produk memiliki hubungan dengan satu pengguna tertentu, yang berarti pemilik produk tersebut. Pada `views.py`, saya memodifikasi potongan kode yang terdapat pada fungsi `create_product` sehingga saya dapat membuat produk baru menggunakan akun pengguna yang sedang login. Saya juga melakukan modifikasi pada fungsi `show_main` untuk memastikan bahwa hanya produk yang dimiliki oleh pengguna yang sedang login yang akan ditampilkan. Setelah menyimpan semua perubahan, saya melakukan migrasi model dengan perintah `python manage.py makemigrations`. Saat muncul error, pilih 1 sebanyak dua kali, di mana yang pertama untuk menetapkan default value pada field user dan yang kedua untuk menetapkan user dengan ID 1 pada model yang sudah ada. Setelah semuanya selesai dilakukan, jalankan perintah `python manage.py migrate` untuk mengaplikasikan migrasi yang telah dilakukan sebelumnya. Terakhir, saya menjalankan proyek Django dengan perintah `python manage.py runserver` dan membuka situs http://localhost:8000/.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Pada bagian ini, pertama-tama, saya akan mengimpor modul-modul yang diperlukan pada berkas `views.py`. Selanjutnya, saya memodifikasi fungsi `login_user` dengan menambahkan cookie `last_login` untuk mencatat waktu pengguna terakhir kali melakukan login. Saya juga menambahkan potongan kode pada fungsi `show_main` dengan menambahkan `'last_login': request.COOKIES['last_login'],` ke dalam variabel `context`. Setelah itu, saya melakukan modifikasi pada fungsi `logout_user` sehingga cookie `last_login` terhapus saat pengguna melakukan logout dan data `last_login` akan terhapus dari sesi saat logout dilakukan. Untuk menampilkan data `last login`, saya menambahkan potongan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada berkas `main.html`. Terakhir, saya memastikan data last login yang saya buat muncul pada halaman main dengan perintah `python manage.py runserver`.

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

Setelah menyelesaikan semua langkah di atas, saya menjawab beberapa pertanyaan pada berkas `README.md`.

- [x] Melakukan add-commit-push ke GitHub.

Terakhir, saya melakukan add, commit, dan push ke GitHub dengan perintah:
```git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```
