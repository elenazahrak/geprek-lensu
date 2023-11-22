Nama   : Elena Zahra Kurniawan

NPM    : 2206824060

Kelas  : PBP F

[Link Web Geprek Lensu](http://elena-zahra-tugas.pbp.cs.ui.ac.id)

<details>
<summary>Tugas 2</summary>
<br>
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

</details>

<details>
<summary>Tugas 3</summary>
<br>

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
</details>

<details>
<summary>Tugas 4</summary>
<br>

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

Untuk mengimplementasikan fungsi login, pertama-tama saya membuka berkas `views.py` pada subdirektori `main` untuk membuat sebuah fungsi baru bernama `login_user`. Sebelumnya, saya mengimport beberapa modul untuk mengautentikasi pengguna dan menjalankan proses login ketika autentikasi berhasil. Setelah itu, saya menambahkan potongan kode pada fungsi `login_user` untuk mengautentikasi pengguna yang berusaha untuk masuk ke dalam sistem. Saya juga membuat berkas baru bernama `login.html` pada direktori `main/templates` sebagai tampilan pada halaman login. Terakhir, saya mengimpor dan menghubungkan fungsi `login_user` ke dalam berkas `urls.py` di subdirektori main dengan menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi yang telah diimpor sebelumnya.

Untuk mengimplementasikan fungsi logout, pertama-tama saya membuka berkas `views.py` pada subdirektori `main` dan mengimpor modul logout untuk mengakses fungsionalitas logout. Saya juga membuat fungsi bernama `logout_user` dan mengisi fungsi tersebut dengan perintah `logout(request)` dan `return redirect(‘main:login’)`. Perintah `logout(request)` digunakan untuk menghapus sesi pengguna setelah melakukan login dan `return redirect(‘main:login’)` berperan untuk mengarahkan pengguna kembali ke halaman login setelah logout. Setelah itu, saya memodifikasi berkas `main.html` pada folder `main/templates` dengan menambahkan tombol Logout setelah hyperlink untuk “Add New Product” pada halaman utama. Terakhir, saya mengimpor dan menghubungkan fungsi `logout_user` ke dalam berkas `urls.py` di subdirektori main dengan menambahkan path URL ke dalam `urlpatterns` untuk dapat mengakses fungsi yang telah diimpor sebelumnya.

Untuk membatasi akses ke halaman utama, saya menambahkan beberapa potongan kode pada berkas `views.py` dengan menambahkan impor modul `login_required` untuk mewajibkan pengguna melakukan login dan menambahkan decorator `@login_required(login_url='/login')` di atas fungsi `show_main` supaya pengguna yang dapat mengakses halaman utama hanyalah pengguna yang sudah login. Terakhir, saya menjalankan perintah `python manage.py runserver` dan membuka situs http://localhost:8000/  untuk memastikan bahwa pengguna terarahkan ke tampilan login.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Pada bagian ini, saya membuat akun baru dengan memasukkan username, password, dan melakukan konfirmasi password sesuai ketentuan yang tertulis pada halaman login. Setelah memenuhi kriteria tersebut, saya berhasil masuk ke laman produk dan dapat menambahkan produk pada akun saya.
<img width="520" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/bc3ff5bf-a015-437f-bd26-da63667ccd93">
<img width="398" alt="image" src="https://github.com/elenazahrak/geprek-lensu/assets/125001077/2076527f-bed3-4a47-ab14-2dcfe3fb2abb">

- [x] Menghubungkan model Item dengan User.

Pertama-tama, saya mengimport model yang dibutuhkan pada berkas `models.py` yang terletak di dalam subdirektori `main`. Kemudian, saya menambahkan potongan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model Product saya.  Potongan kode ini akan menghubungkan setiap produk dengan pengguna melalui hubungan ForeignKey. ForeignKey menunjukkan bahwa setiap produk memiliki hubungan dengan satu pengguna tertentu, yang berarti pemilik produk tersebut. Pada `views.py`, saya memodifikasi potongan kode yang terdapat pada fungsi `create_product` sehingga saya dapat membuat produk baru menggunakan akun pengguna yang sedang login. Saya juga melakukan modifikasi pada fungsi `show_main` untuk memastikan bahwa hanya produk yang dimiliki oleh pengguna yang sedang login yang akan ditampilkan. Setelah menyimpan semua perubahan, saya melakukan migrasi model dengan perintah `python manage.py makemigrations`. Saat muncul error, pilih 1 sebanyak dua kali, di mana yang pertama untuk menetapkan default value pada field user dan yang kedua untuk menetapkan user dengan ID 1 pada model yang sudah ada. Setelah semuanya selesai dilakukan, jalankan perintah `python manage.py migrate` untuk mengaplikasikan migrasi yang telah dilakukan sebelumnya. Terakhir, saya menjalankan proyek Django dengan perintah `python manage.py runserver` dan membuka situs http://localhost:8000/.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Pada bagian ini, pertama-tama, saya akan mengimpor modul-modul yang diperlukan pada berkas `views.py`. Selanjutnya, saya memodifikasi fungsi `login_user` dengan menambahkan cookie `last_login` untuk mencatat waktu pengguna terakhir kali melakukan login. Saya juga menambahkan potongan kode pada fungsi `show_main` dengan menambahkan `'last_login': request.COOKIES['last_login'],` ke dalam variabel `context`. Setelah itu, saya melakukan modifikasi pada fungsi `logout_user` sehingga cookie `last_login` terhapus saat pengguna melakukan logout dan data `last_login` akan terhapus dari sesi saat logout dilakukan. Untuk menampilkan data `last login`, saya menambahkan potongan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada berkas `main.html`. Terakhir, saya memastikan data last login yang saya buat muncul pada halaman main dengan perintah `python manage.py runserver`.

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

Setelah menyelesaikan semua langkah di atas, saya menjawab beberapa pertanyaan pada berkas `README.md`.

- [x] Melakukan add-commit-push ke GitHub.

Terakhir, saya melakukan add, commit, dan push ke GitHub dengan perintah:
```
git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```
</details>

<details>
<summary>Tugas 5</summary>
<br>
 
**1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**

- Element Selector

Element selector merupakan jenis selector yang akan memilih HTML element berdasarkan nama elemennya. Kita dapat menggunakannya ketika kita ingin mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. 

Contoh:

```
p {
  text-align: center;
  color: pink;
}
```
Semua elemen `<p>` akan menjadi rata tengah dengan teks yang berwarna biru.

- Id Selector
  
Id selector merupakan jenis selector yang menyeleksi “id” menggunakan atribut “id” dari HTML element untuk memilih elemen tertentu. Id dari suatu elemen harus unik. Kita dapat menggunakannya ketika kita ingin mengaplikasikan gaya atau manipulasi tertentu ke elemen yang memiliki ID tertentu. Cara penulisannya adalah dengan menuliskan karakter hash  (#), lalu diikuti oleh Id elemen. 

Contoh
```
#paragraf {
  text-align: center;
  color: pink;
}
```

- Class Selector
  
Class selector merupakan jenis selector yang menyeleksi “class” dengan atribut “class” tertentu. Kita dapat menggunakannya ketika kita ingin mengaplikasikan gaya tertentu ke beberapa elemen yang memiliki class yang sama. Cara penulisannya adalah dengan menuliskan karakter titik (.) dan diikuti dengan nama class-nya.

Contoh:

```
.center {
  text-align: center;
  color: pink;
}
```


- Universal Selector
  
Universal selector adalah jenis selector yang menyeleksi Cascading Style Sheets yang memilih semua HTML element pada sebuah halaman web. Kita dapat menggunakannya ketika kita ingin mereset gaya dasar (CSS reset) atau ingin memilih semua elemen dalam dokumen ketika diperlukan.

Contoh:
```
* {
  text-align: center;
  color: pink;
}
```

**2. Jelaskan HTML5 Tag yang kamu ketahui.**

HTML merupakan sebuah bahasa markup yang digunakan untuk membuat dan merancang halaman web. HTML5 merupakan versi terbaru yang hadir dengan berbagai fitur yang memungkinkan developer dapat membuat situs web dengan pengalaman yang lebih baik. Berikut ini merupakan beberapa tags yang terdapat pada HTML5:

`<html>`: Tag untuk mendefinisikan awal dan akhir dari sebuah dokumen HTML dan semua elemen HTML yang akan berada di dalamnya

`<head>`: Wadah untuk meta-informasi tentang dokumen, seperti judul, karakter set, dan tautan ke file CSS atau JavaScript

`<title>`: Tag yang digunakan dalam elemen `<head>` untuk mendefinisikan judul halaman yang akan ditampilkan di tab peramban

`<link>`: Tag yang digunakan dalam elemen `<head>` untuk menghubungkan dokumen HTML dengan file eksternal, misalnya file CSS

`<style>`: Tag untuk menambahkan CSS langsung ke dalam halaman HTML

`<body>`: Wadah untuk konten yang akan ditampilkan di halaman web, misalnya teks, gambar, formulir, dan elemen lainnya

`<p>`: Tag untuk menampilkan paragraf teks

`<h1>, <h2>, …, <h6>`: Tag untuk membuat judul

`<img>`: Tag untuk menampilkan gambar pada halaman web

`<form>`: Tag untuk membuat formulir interaktif yang akan digunakan oleh pengguna untuk mengirim data

**3. Jelaskan perbedaan antara margin dan padding**.

Margin merupakan ruang yang berada di sekitar elemen HTML. Menggunakan margin, kita dapat mengendalikan jarak antara elemen tersebut dengan elemen-elemen lain yang ada di luar batas elemen. Margin biasanya digunakan untuk mengatur tata letak halaman dan tidak memiliki latar belakang atau warna. Lain halnya dengan padding, di mana padding merupakan ruang yang berada di sekitar konten dalam elemen HTML. Menggunakan padding, kita dapat mengendalikan jarak antara konten elemen dengan batas elemen itu sendiri. Padding dapat memiliki latar belakang dan warna sehingga memengaruhi tampilan elemen.

**4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**

CSS Tailwind merupakan kerangka kerja (framework) yang dapat digunakan untuk membuat UI atau tampilan dari aplikasi web dengan mudah dan cepat. Berbeda dengan Tailwind, Bootstrap merupakan sebuah framework yang dapat digunakan untuk membuat desain yang responsif dan mobile-friendly. Dari segi ukuran, tailwind menghasilkan ukuran file CSS yang lebih sedikit dibandingkan bootstrap. Bootstrap cenderung memiliki file CSS yang besar karena mengandung gaya yang lebih banyak. Dari segi pendekatan dan desain, tailwind lebih berfokus pada pendekatan “utility-first”, yaitu menggabungkan banyak kelas kecil untuk merancang elemen dan komponen. Dengan begitu, tailwind membutuhkan penulisan kode HTML yang lebih banyak. Lain halnya dengan bootstrap yang berfokus pada pendekatan komponen yang lebih besar dengan gaya bawaan yang lebih kuat. Dalam penggunaannya, tailwind sangat mudah disesuaikan dengan desain karena kita dapat mengubah kelas-kelas utilitasnya sesuai kebutuhan, sedangkan bootstrap memiliki gaya bawaan yang lebih kaku, sehingga penyesuaian dengan desain memerlukan lebih banyak kode tambahan.

Kita dapat menggunakan tailwind jika kita memerlukan tingkat kontrol yang tinggi terhadap desain yang tampilannya sangat kustom. Framework ini cocok dengan orang-orang yang lebih nyaman dengan pendekatan “utility-first” dan ingin mengurangi ukuran file CSS yang dihasilkan. Di sisi lain, kita dapat menggunakan bootstrap apabila kita ingin membuat tampilan website dengan cepat melalui komponen-komponen yang sudah disiapkan dan dirancang untuk digunakan secara umum. Framework ini cocok digunakan untuk orang-orang yang membutuhkan dukungan browser yang luas.


**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

- [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
Dalam melakukan kustomisasi halaman `login.html`, `register.html`, dan `create_product.html`, saya melakukan beberapa perubahan, misalnya dengan memasukkan form input login dan register ke dalam suatu card dan mengubah background. Untuk mempermudah dalam pembuatan desain, saya menggunakan framework Bootstrap. Dalam pembuatannya, saya menggunakan 2 cara penulisan CSS yaitu inline styles dan internal style sheet.

Berikut ini merupakan contoh penulisan inline styles yang saya gunakan:

```
<a class="navbar-brand" href="#" style="line-height: 2; color: #FFFFFF;">Geprek Lensu</a>
```

Berikut ini merupakan contoh penulisan internal style sheet yang saya gunakan:

```
<style>
        .navbar {
            background-color: #382B3D;
            padding: 0;
            font-family: 'Inter', sans-serif;
            font-weight: bold;
        }

        .body {
            max-width: 1440px;
            padding-right: 20px;
            padding-left: 20px;
            background-image: url('https://wallpapercave.com/wp/wp8855577.jpg');
        }

        .text {
            color: #ffffff;
            padding-top: 40px;
            padding-left: 50px;
            font-family: 'Inter', sans-serif;
        }
        .row {
            padding: 40px;
            padding-left: 40px;
            padding-right: 40px;
        }
        .cardbox {
            width: 380px;
            height: 200px;
        }
        .card-body {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
        }

        .cookie {
            color: #ffffff;
            padding-top: 40px;
            padding-left: 50px;
            font-family: 'Inter', sans-serif;
        }
    </style>
```

Selain itu, jenis selector yang saya gunakan adalah Class Selector.

Berikut ini merupakan contoh penulisan Class Selector yang saya gunakan:

```
.navbar {
            background-color: #382B3D;
            padding: 0;
            font-family: 'Inter', sans-serif;
            font-weight: bold;
        }
```

- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

Dalam melakukan kustomisasi halaman `main.html`, saya buat lebih berwarna dengan melakukan beberapa perubahan, misalnya dengan menambahkan navigation bar dan menampilkan daftar produk ke dalam card. Agar tampilan menjadi lebih berwarna, saya mengatur gaya tampilan dengan menggunakan internal styles. Berikut ini merupakan kode yang saya buat untuk menambahkan navigation bar dan menampilkan daftar produk ke dalam card:

```
<nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="#" style="line-height: 2; color: #FFFFFF;">Geprek Lensu</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:create_product' %}" style="color: #FFFFFF;">Tambah Item</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'main:logout' %}" style="color: #FFFFFF;">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
```

```
<div class="row">
            {% for product in products %}
                <div class="cardbox">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.menu }}</h5>
                        <p class="card-text">Harga: {{ product.price }}</p>
                        <p class="card-text">Jumlah Stok: <span id="stock{{ product.id }}">{{ product.stock }}</span></p>
                        <p class="card-text">{{ product.description }}</p>
                        <div class="text-center">
                            <a href="{% url 'main:add_stock' product.id %}" class="btn btn-primary btn-sm">Tambah</a>
                            <a href="{% url 'main:reduce_stock' product.id %}" class="btn btn-warning btn-sm">Kurang</a>
                            <a href="{% url 'main:delete_product' product.id %}" class="btn btn-danger btn-sm">Hapus</a>
                            <a href="{% url 'main:edit_product' product.id %}" class="btn btn-info btn-sm">Edit</a>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
```

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

Setelah menyelesaikan semua langkah di atas, saya menjawab beberapa pertanyaan pada berkas `README.md`.

- [x] Melakukan add-commit-push ke GitHub.

Terakhir, saya melakukan add, commit, dan push ke GitHub dengan perintah:

```
git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```

</details>

<details>
<summary>Tugas 6</summary>
<br>
 
**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
 
Asynchronous programming dan synchronous programming merupakan dua paradigma atau teknik pemrograman yang berbeda dalam cara mereka mengelola dan mengeksekusi tugas atau operasi yang memerlukan waktu. Synchronous programming mengeksekusi tugas atau operasi secara berurutan, satu persatu. Tugas yang sudah dimulai akan ditunggu hingga tugas tersebut selesai sebelum lanjut ke tugas berikutnya. Walaupun lebih mudah untuk diterapkan, tetapi pendekatan ini memerlukan waktu yang lama dan mampu mengakibatkan aplikasi menjadi melambat hingga tidak responsif. Berbeda dengan synchronous, asynchronous programming menjalankan tugas atau operasi secara bersamaan tanpa menunggu operasi sebelumnya selesai. Pendekatan ini menggunakan konsep seperti callback, promise, async/wait, dan konsep-konsep lainnya untuk mengelola alur eksekusi. Asynchronous programming biasanya digunakan dalam hal-hal yang memerlukan jenis pendekatan yang tetap responsif saat mengeksekusi tugas yang memerlukan waktu lama, misalnya operasi I/O atau komputasi intensif.

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Paradigma event-driven programming merupakan sebuah pendekatan di mana program merespons peristiwa atau kejadian yang terjadi, misalnya tindakan pengguna, dengan menjalankan tindakan tertentu. Pada JavaScript dan AJAX, paradigma ini sangat relevan karena banyak terdapat interaksi pengguna dan perubahan dinamis yang terjadi pada halaman web. Dalam tugas ini, penerapan kodenya seperti kode di bawah ini

```
function addProduct() {
    fetch("{% url 'main:create_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    })
    .then(function (response) {
        if (response.status === 200) {
            var myModal = new bootstrap.Modal(document.getElementById("addProductModal"));
            myModal.hide();

            document.getElementById("form").reset();
        }
    })
    .then(refreshProducts);

    return false;
}

document.getElementById("button_add").onclick = addProduct;
```

Saya menggunakan kode `document.getElementById("button_add").onclick` untuk menentukan event listener yang akan merespons klik pengguna pada tombol dengan ID "button_add". Ini adalah implementasi dari paradigma event-driven, di mana kita mendengarkan tindakan pengguna (klik) pada elemen tertentu. Ketika tombol "Add Product by AJAX" diklik, fungsi `addProduct` akan menjalankan sebuah AJAX request menggunakan fetch. Ini adalah contoh lain dari event-driven programming, di mana tindakan pengguna (klik tombol) mengarah pada permintaan AJAX yang dilakukan ke server. Setelah mendapatkan respons dari server (dalam kasus ini, jika respons memiliki status 200), saya mengubah tampilan dengan cara menutup modal yang memiliki ID "addProductModal" dan mereset form dengan ID "form". Ini adalah contoh lain dari event-driven programming di mana respons server menghasilkan tindakan lanjutan pada tampilan (manipulasi DOM). Jadi, paradigma event-driven programming pada contoh ini adalah bahwa tindakan atau kejadian (klik tombol "Add Product by AJAX") merespons dengan menjalankan serangkaian tindakan lain yang terjadi pada elemen-elemen halaman web.

**3. Jelaskan penerapan asynchronous programming pada AJAX.**

Asynchronous programming pada AJAX memungkinkan aplikasi web untuk responsif dan menghindari blocking sehingga pengguna bisa terus berinteraksi dengan halaman web tanpa harus menunggu permintaan ke server selesai. Hal ini mampu meningkatkan responsivitas dan pengalaman pengguna saat menggunakan aplikasi web. Beberapa aspek penerapan asynchronous programming dalam AJAX di antaranya callback functions, promises, dan event listeners. Callback functions didefinisikan untuk menangani respons dari server setelah permintaan selesai. Konsep ini dapat mengirimkan permintaan HTTP asinkron ke server menggunakan objek XMLHttpRequest atau fetch API. Dengan begitu, kita dapat menjalankan kode tertentu hanya ketika data telah diterima dan eksekusi kode lainnya tidak berhenti. Selanjutnya adalah promises yang dapat digunakan untuk menulis kode asynchronous sehingga lebih mudah untuk dipahami. Konsep ini dapat digunakan untuk mengatasi AJAX request dengan cara yang lebih elegan. Konsep selanjutnya ialah event listeners yang dapat menangani AJAX events, misalnya ‘load’, ‘eror’, dan ‘abort’. Dengan ini, kita dapat merespons berbagai kejadian yang terkait dengan permintaan asinkron. 

**4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**

Dari segi ukuran, Fetch API lebih ringan dan menghemat ruang serta waktu dalam proses pengunduhannya karena aplikasi kita tidak memuat library tambahan, sedangkan jQuery yang merupakan library yang lebih besar sehingga cenderung memiliki ukuran yang lebih besar. Akan tetapi, jQuery ini membantu kita dalam menghindari penulisan kode JavaScript yang berlebihan sehingga dari segi fungsionalitas menjadi lebih lengkap. Selain itu, fetch API memiliki sintaks yang lebih sederhana sehingga lebih mudah dipahami untuk pengembang yang terbiasa dengan JavaScript, walaupun pemula mungkin akan sedikit kebingungan dalam menangani konsep Promise. JQuery juga memiliki sintaks yang sederhana karena banyak fungsi yang sudah tersedia sehingga mempermudah pengembang dalam melakukan pekerjaannya. Selanjutnya, fetch API belum didukung oleh beberapa versi lama dari Internet Explorer. Akan tetapi, tidak perlu khawatir juga karena masalah ini dapat diselesaikan dengan transpiler. Lain halnya dengan jQuery yang telah dirancang untuk kompatibilitas lintas browser, termasuk browser lama. Dari berbagai pertimbangan di atas, sebenarnya kita dapat memilih sesuai dengan kebutuhan aplikasi masing-masing. Fetch API akan menjadi solusi yang tepat jika kita membutuhkan kinerja yang maksimal, ukurang yang lebih kecil, dan teknologi yang lebih modern. Akan tetapi, jQuery menjadi pilihan yang tepat jika kita membutuhkan dukungan kompatibilitas lintas browser yang kuat.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
- [x] Ubahlah kode cards data item agar dapat mendukung AJAX GET & Lakukan pengambilan task menggunakan AJAX GET.

Pada bagian ini, saya telah menentukan dua fungsi `getProducts` dan `refreshProducts` pada blok JavaScripts. Fungsi `getProducts` digunakan untuk melakukan pengambilan data produk dengan menggunakan AJAX GET. Fungsi ini mengambil data dari URL yang dihasilkan oleh templatetag Django `{% url 'main:get_product_json' %}` dan kemudian mengubah respons tersebut menjadi data JSON. Kemudian, fungsi `refreshProducts` mengambil data produk menggunakan `getProducts` dan menampilkan produk-produk tersebut dalam bentuk kartu di halaman website. Saya juga memanggil refreshProducts setelah halaman dimuat untuk pertama kali agar produk dapat ditampilkan pada awalnya. Dengan begitu, pengambilan task menggunakan AJAX GET dilakukan melalui fungsi getProducts yang diaktifkan saat halaman dimuat dan menghasilkan produk-produk yang ditampilkan pada halaman melalui fungsi `refreshProducts`.

- [x] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.

Pada bagian ini, saya membuat tombol yang dapat membuka sebuah modal yang berisi form  sehingga pengguna dapat menambahkan item. Untuk mengimplementasikannya, saya membuat kerangka modal yang memuat elemen-elemen yang diperlukan misalnya judul modal, input form, dan tombol untuk menutup modal dan menambahkan produk. Setelah itu, saya membuat tombol pada halaman utama yang akan memicu modal. Kemudian, saya membuat fungsi `addProduct()` untuk menambahkan data produk ke basis data yang menggunakan AJAX untuk mengirim data formulir ke server dengan metode POST serta mengosongkan formulir setelah berhasil menambahkan data. Fungsi ini juga mengeksekusi fungsi `refreshProducts()`. Terakhir, saya menambahkan event handler untuk tombol “Add Product” pada modal sehingga dapat menjalankan fungsi `addProduct()` saat tombol ini ditekan.

- [x] Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.

Pada bagian ini, saya membuat sebuah fungsi di views yang bertugas untuk menambahkan produk baru ke dalam basis data menggunakan teknik AJAX. Pertama, saya membuat fungsi baru di `views.py` dengan nama `add_product_ajax` yang menerima parameter `request`. Untuk mengintegrasikan AJAX dengan Django, saya mengimpor modul `csrf_exempt` dari `django.views.decorators.csrf` ke dalam berkas `views.py`. Kemudian, kita perlu menambahkan dekorator `@csrf_exempt` di atas fungsi `add_product_ajax` yang telah dibuat sebelumnya. Selanjutnya, dalam fungsi `add_product_ajax`, saya memiliki kode yang mengambil data dari permintaan POST. Misalnya, saya mengambil nilai `menu`, `price`, `stock`, `description`, dan `user` dari permintaan tersebut. Selanjutnya, saya mengidentifikasi pengguna yang sedang masuk (user) dengan `request.user.`.

Setelah itu, saya membuat objek baru yang sesuai dengan model `Product` dengan data yang telah diambil dari permintaan. Objek "new_product" ini kemudian disimpan ke dalam basis data menggunakan metode "save()". Terakhir, saya memberikan respons HTTP dengan status 201 (CREATED) untuk menandakan bahwa produk baru telah berhasil ditambahkan ke basis data. Jika ada kesalahan dalam permintaan atau produk tidak dapat ditambahkan, saya memberikan respons "HttpResponseNotFound()" untuk menandakan bahwa halaman yang diminta tidak ditemukan.

- [x] Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

Pada bagian ini, saya menambahkan pengaturan rute untuk fungsi `create_ajax`. Pertama, saya membuka berkas `urls.py` pada direktori `main` dan melakukan impor fungsi `create_ajax`. Setelah itu, saya menambahkan rute URL dengan kode `path('create-ajax/', create_ajax, name='create_ajax'),` ke dalam pengaturan `urlpatterns`. Dengan begitu, URL ini akan mengarahkan permintaan pengguna ke fungsi yang sesuai untuk menambahkan produk baru menggunakan AJAX yaitu `create_ajax`.

- [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

Pada bagian `<button type="button" class="btn" id="button_add" data-bs-dismiss="modal" style="background-color: #E03930; color:#EAD9A3; font-weight: 600;">Add Product</button>`, kode saya telah mengaitkannya dengan AJAX untuk mengirim data ke path `"/create-ajax":`. Elemen ini merupakan sebuah tombol dengan ID `button_add`. Ketika tombol ini ditekan, fungsi `addProduct` yang menggunakan Fetch API akan dijalankan untuk mengirimkan data formulir ke path `"/create-ajax"` dan kemudian akan melakukan pembaruan dengan memanggil fungsi `refreshProducts`.

- [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

Pada bagian ini saya memodifikasi kode JavaScript dan bagian ini menggunakan sebuah fungsi bernama `refreshProducts` yang digunakan untuk memperbarui tampilan produk di halaman web dengan data produk yang diperoleh dari server. Pertama, fungsi ini menggunakan `await getProducts()` untuk mengambil data produk dari server secara asynchronous. Fungsi `getProducts` adalah sebuah permintaan (request) ke server yang mengembalikan data produk. Setelah mendapatkan data produk, fungsi membersihkan (menghapus) isi dari elemen dengan ID `product_cards` pada halaman web dengan mengatur `.innerHTML`-nya menjadi string kosong. Hal ini dilakukan untuk membersihkan tampilan produk sebelum memperbarui dengan data yang baru. Selanjutnya, kode JavaScript mempersiapkan variabel `htmlString` yang akan digunakan untuk menyusun elemen-elemen HTML yang akan menampilkan produk. Variabel ini dimulai dengan string kosong. Kemudian, fungsi melakukan perulangan `items.forEach` melalui data produk yang diperoleh dari server. Untuk setiap produk, ia menambahkan elemen HTML yang akan menampilkannya dalam format yang diinginkan. Ini termasuk judul produk `menu`, deskripsi produk `description`, harga produk `price`, dan stok produk `stock`. Kemudian, ada bagian yang menambahkan tombol-tombol edit, delete, add stock, dan reduce stock. Tombol-tombol ini memiliki atribut `href` yang merujuk ke URL yang sesuai untuk masing-masing tindakan. Atribut `href` ini akan menyebabkan tindakan tertentu terjadi saat tombol ditekan. Setelah perulangan selesai, variabel `htmlString` yang berisi elemen-elemen HTML produk diberikan kepada elemen dengan ID `product_cards` menggunakan `.innerHTML`. Ini akan menyebabkan tampilan produk di halaman web diperbarui dengan data produk yang baru. Terakhir, saya memanggil `refreshProducts()` untuk menjalankan fungsi ini saat halaman dimuat. Fungsi ini akan memperbarui tampilan produk di halaman saya berdasarkan data yang diterima dari server.

- [x] Melakukan perintah collectstatic.

Pada bagian ini, saya melakukan pengaturan untuk static files yang terdapat pada file `settings.py`. Static files ini mencakup berbagai jenis file seperti CSS, JavaScript, dan gambar. Terdapat dua kode yang saya tambahkan yaitu `STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')` yang akan menentukan absolute path ke direktori tempat static files akan disimpan ketika perintah `collectstatic` dijalankan dalam proyek. Dengan begitu, kita dapat mengumpulkan semua static files dari berbagai aplikasi dalam proyek ke satu direktori. Baris kode kedua yang saya tambahkan adalah `STATIC_URL = 'static'` yang merupakan URL yang dapat diakses secara publik untuk mengambil static files. Ini merupakan alamat yang digunakan untuk mengakses static files dari luar situs web. Sedangkan perintah `collectstatic` itu sendiri bertugas untuk mengumpulkan semua static files dari berbagai aplikasi dalam proyek Django sehingga mempermudah akses dan penggunaan static files tersebut dalam situs web.

- [x] Melakukan add-commit-push ke GitHub.

Saya melakukan add, commit, dan push ke GitHub dengan perintah:

```
git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```

- [x] Melakukan deployment ke PaaS PBP Fasilkom UI dan sertakan tautan aplikasi pada file README.md.

Terakhir, saya melakukan deployment terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses secara luas oleh teman-temanmu melalui Internet.

</details>
