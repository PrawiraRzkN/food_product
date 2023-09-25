# Tugas 2: Aplikasi pengatur penjualan produk-produk makanan nusantara.
Tautan menuju aplikasi Adaptable: https://foodproduct-management.adaptable.app

## **Step by step deploy proyek baru**
1. Membangun proyek Django baru, yaitu membuat terlebih dahulu direktori baru bernama 'food_product'. Lalu menjalankan virtual environment untuk direktori tersebut untuk mengisolasi dependencies yang akan diinstall, termasuk Django itu sendiri. Setelah dependencies terinstall, dilakukan konfigurasi dan dijalankan server dari proyek ini. Jika berhasil, maka direktori baru ini di unggah ke repository github baru dengan nama yang sama.
2. Pada direktori 'food_product' dibuat aplikasi baru bernama 'main' dengan memanfaatkan virtual environtment dan membuat munculnya folder baru bernama main pada direktori 'food_product'. Tidak lupa, aplikasi main ditambahkan ke INSTALLED_APPS pada settings.py sehingga proyek mengetahui penambahan aplikasi tersebut.
3. Model dibuat pada tahap ini dengan nama Item dan berisi atribut wajib, yaitu name, amount, dan description dengan tipe data masing-masing sesuai arahan pada soal. Lalu saya menambahkan atribut date_added, price, category, dan origin sesuai dengan keperluan aplikasi. Setelah model tersebut dibuat, model harus dimigrasi agar penambahan atau perubahannya dapat terefleksi oleh Django.
4. Aplikasi main yang sudah dibuat tersebut harus dibuatkan routingnya pada proyek, yaitu dengan cara menghubungkan urls.py yang ada pada direktori 'food_product' dengan urls.py baru yang ada dalam direktori 'main'. Dengan begitu, fungsi yang ada di views.py, berisi data dari model, terpetakan.
5. Dilakukan unit testing terlebih dahulu agar kode yang dibuat pada direktori berjalan sesuai dengan yang diharapkan. (Pada proyek saya, diberikan test tambahan, yaitu test pembuatan instance dari model dan test menyimpan dan mengambil instance model)
6. Repository pada github diupdate sesuai dengan perubahan pada direktori 'food_product'.
7. Aplikasi siap untuk dilakukan deployment ke Adaptable dengan cara membuat terlebih dahulu aplikasi Adaptable yang terintegrasi pada repository 'food_product' pada github.

## **Proses request client ke web aplikasi berbasis Django**
![Bagan request client ke web aplikasi Django](img-properties/bagan-client-request.jpg)
Dalam aplikasi web Django, ketika klien mengirim permintaan HTTP, Django menggunakan berkas urls.py untuk menentukan tampilan yang sesuai. Tampilan yang ada dalam berkas views.py mengendalikan logika aplikasi, termasuk berinteraksi dengan model dalam berkas models.py untuk mengakses dan mengubah data dalam basis data. Data yang diperlukan untuk menghasilkan tampilan dikumpulkan dalam tampilan, dan hasilnya dirender dengan menggunakan berkas HTML. Berkas HTML berisi kode HTML dan tag-template Django yang digunakan untuk menyisipkan data dari tampilan. Setelah proses rendering selesai, tampilan tersebut dikirim sebagai respons kepada klien, membentuk alur pengembangan yang terstruktur dalam Django: urls.py mengatur rute, views.py mengendalikan logika, models.py mengelola data, dan berkas HTML mengontrol tampilan, sehingga menciptakan aplikasi web yang berfungsi dengan baik.

## **Mengapa kita menggunakan virtual environment? Apakah dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Aplikasi web berbasis Django dibuat dengan virtual environment untuk mengisolasi dependencies dari system milik komputer. Sehingga perubahan sistem yang terjadi pada komputer atau proyek lainnya tidak akan mempengaruhi stabilitas proyek yang sedang dikembangkan. Selain itu, virtual environment digunakan juga agar sistem dapat menjalankan lebih dari satu proyek Django pada satu komputer saja. Aplikasi web berbasis Django juga dapat dibuat tanpa virtual environment, namun hal tersebut tidak disarankan karena bisa jadi adanya konflik antar sistem yang berjalan di komputer atau proyek lainnya dengan proyek yang sedang dibuat.

## **Apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
Dalam pengembangan aplikasi, terdapat beberapa pola arsitektur perangkat lunak yang lazim digunakan para developer, yaitu MVC (Model-View-Controller), MVT (Model-View-Template) dan MVVM (Model-View-ViewModel). Pola arsitektur ini berguna untuk memisahkan komponen yang dimiliki suatu aplikasi dengan komponen aplikasi lainnya sehingga tidak terjadi konflik antar komponen tersebut. 

Pada MVC, MVT, dan MVVM ketiganya memiliki kesamaan dalam struktur, yaitu terdapat model dan view:
1. Model --> Bagian yang mengelola data dari aplikasi. Mulai dari mengakses, memanipulasi, validasi, hingga perhitungan dari data yang dimiliki aplikasi maupun dari sumber lain.
2. View --> Bagian yang mengelola tampilan untuk diberikan kepada pengguna ketika menggunakan aplikasi. View akan mengakses data-data melalui model lalu data tersebut ditampilkan ke layar pengguna.

### MVC (Model-View-Controller)
Pada MVC terdapat bagian yang akan mengelola alur informasi dalam berjalannya aplikasi, yaitu sebagai perantara antara Model dan View. Bagian ini disebut dengan Controller. Ketika pengguna melakukan permintaan pada aplikasi, Controller berperan dalam memproses permintaa tersebut dan mengirim sinyal kepada Model agar data diperbaharui sesuai permintaan pengguna atau mengirimkan data yang dibutuhkan ke View untuk ditampilkan.

### MVT (Model-View-Template)
Pada MVT terdapat bagian yang bernama Template. Fungsi bagian ini adalah menjadi tampilan yang akan diberikan pengguna. Sehingga Template seringkali digunakan oleh developer untuk merancang tampilan halaman web atau aplikasi. Template bisa muncul pada layar pengguna akibat sinyal dari View yang menjadi pengatur tampilan sekaligus kurir bagi Model untuk memberikan data-data ke Template.

### MVVM (Model-View-ViewModel)
Pada MVVM ada jembatan antara Model dan View yang disebut dengan ViewModel. Bagian ini selain menjadi perantara, juga menjadi pengatur format yang diberikan Model agar dapat ditampilkan oleh View sehingga dapat ditampilkan pada layar.

### Perbedaan MVC, MVT, dan MVVM:
| **MVC** | **MVT** | **MVVM** |
| --- | --- | --- |
|Pola desainnya diatur agar dapat digunakan dalam pengembangan berbagai jenis aplikasi seperti aplikasi dekstop, web, dan mobile. Dalam model ini, Model dan View dipisahkan Controller sehingga developer harus mengelola Controller secara manual apabila terdapat perubahan pada Model maupun View. | MVT adalah desain yang dibuat untuk pengembangan aplikasi basis website. Terdapat Template yang akan mengatur tampilan halaman web dan akan mengurus pembaruan tampilan secara otomatis ketika data berubah. | Desain MVVM sering digunakan dalam aplikasi berbasi User Interface seperti aplikasi mobile atau dekstop. Desain ini memiliki ViewModel yang akan memisahkan Model dan View seutuhnya sehingga keduanya tidak saling bergantung. MVVM ini mengandalkan sistem data binding, yaitu sistem yang akan secara otomatis melakukan pembaruan ketika terjadi perubahan data yang dibaca oleh ViewModel. |

# Tugas 3: Implementasi Form dan _Data Delivery_ pada Django
Hasil menambahkan objek melalui form dalam format HTML, XML, JSON, XML by ID, dan JSON by ID:
### Format HTML
![Postman result HTML](img-properties/Postman-Result%20(1).jpg)
### Format XML
![Postman result XML](img-properties/Postman-Result%20(5).jpg)
### Format JSON
![Postman result JSON](img-properties/Postman-Result%20(4).jpg)
### Format XML by ID dengan ID=3
![Postman result XML by ID](img-properties/Postman-Result%20(3).jpg)
### Format JSON by ID dengan ID=4
![Postman result JSON by ID](img-properties/Postman-Result%20(2).jpg)

## Perbedaan form POST dan form GET dalam Django
Terdapat dua jenis method form yang dapat digunakan dalam Django, yaitu POST dan GET. Keduanya memiliki fungsi yang sama, yaitu mengambil data yang diisi user pada form lalu menyimpan data tersebut pada database. Akan tetapi, keduanya memiliki karakteristik masing-masing, yaitu sebagai berikut:
| **POST** | **GET** |
| --- | --- |
| Data pada _form_ akan dibaca dan dilakukan _encode_ kepada data tersebut untuk keperluan transmisi, lalu dikirim secara internal kepada server tanpa menampilkan parameter dari URL. Sehingga data lebih aman karena tidak sembarang orang dapat melakukan akses ke data tersebut. | Data pada form akan dibaca dan dikirim ke server sebagai _string_ yang merupakan parameter URL. Sehingga seluruh data yang dibaca menggunakan method GET bisa terlihat oleh siapapun melalui URL |
| Sebuah _request_ yang memberikan dampak kepada database dan system harus menggunakan POST | GET digunakan untuk _request_ yang tidak punya pengaruh kepada system. |
| Cocok digunakan untuk memperoleh _Login Data_ seperti _password_, data yang sangat besar, dan _binary data_ seperti gambar | Cocok digunakan untuk keperluan yang hanya mengakses sesuatu yang sudah ada di website seperti _web search form_. |

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
HTML (HyperTest Markup Language) adalah komponen utama dalam hal mengatur struktur sebuah website, yaitu menginterpretasi dan mengkomposisikan tulisan, gambar, dan material lainnya sehingga dapat ditampilkan pada website. HTML hanya mengurus apa yang ditampilkan pada website dan merespon apa yang dilakukan user pada website, termasuk input data melalui _form_. Akan tetapi, data tersebut oleh HTML hanya dapat dikirim dari user ke server dan server ke user. Untuk melakukan pengiriman data antar server melalui _network_, dibutuhkan XML dan JSON. 

XML (Extensible Markup Language) adalah sebuah _markup language_ dan format _file_ yang didesain untuk menyimpan, mentransimisikan, dan mengkonstruksi berbagai macam data. Data-data yang disimpan melalui XML bersifat _self-describing_ yang membuat data-data tersebut menjadi lebih fleksibel dalam penggunaanya di berbagai website maupun aplikasi. Adapun karakteristik dari XML dalam pengiriman data sebagai berikut:
1. Data disimpan dalam bentuk _tree structure_ dengan _namespace_ untuk setiap kategori data.
2. Memiliki ukuran file yang relatif tinggi.
3. Dapat mendeteksi error pada data yang kompleks dengan baik karena berfokus pada _machine-readablity_.
4. Cocok digunakan dalam dokumen struktur data kompleks yang membutuhkan pertukaran data.

JSON (JavaScript Object Notation) adalah format _file_ yang menggunakan _human-readable text_ untuk menyimpan dan mentransmisikan objek data dengan format pasangan _attribute_:_value_. JSON umumnya digunakan untuk mengirimkan data melalui koneksi jaringan seperti internet, yaitu digunakan dalam mengirimkan data antara server dan aplikasi web. Misalnya, saat browser membuka aplikasi cuaca, browser membuat API _request_ ke server web aplikasi cuaca tersebut. Server web mengirimkan kembali sebuah respon yaitu berupa data JSON. Browser kemudian mengubah data JSON ini menjadi halaman web yang mudah dibaca oleh manusia. Browser menggunakan HTML untuk menentukan bagaimana data yang dikirimkan menggunakan JSON ditampilkan di halaman web. Adapun karakteristik dari JSON dalam pengiriman data sebagai berikut:
1. Data disimpan seperti sebuah _map_ dengan pasangan _key-value_
2. Memiliki ukuran file yang sangat kecil dan transmisi yang cepat
3. Memiliki keamanan penyimpanan data yang baik
4. Cocok digunakan untuk pengembangan _mobile apps_, API, dan media penyimpanan data.

## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern
JSON menjadi pilihan utama kebanyakan _developer_ website sebagai media pertukaran data karena aplikasi web modern sangat dituntut untuk bisa melakukan segalanya dengan kecepatan yang tinggi dan keamanan yang maksimal. Hal tersebut dapat dipenuhi dengan menggunakan JSON. Format bahasa yang _human-readable_ membuat data JSON berukuran ringan sehingga transmisi pengiriman data tersebut bisa dilaksanakan dengan cepat dan lebih mudah dalam melakukan _maintenance_. Selain itu, keamanan yang ditawarkan dari JSON ini lebih baik dibandingkan media pertukaran data lainnya seperti XML.

## _Step by step_ implementasi form dan _data delivery_ pada Django
1. Langkah awal dalam membuat form adalah membuat suatu kerangka views dari situs web yang dibuat agar desain web akan selalu konsisten dan tanpa ada redundansi kode. Dilakukan dengan cara membuat folder template pada root folder dan diisi dengan base.html yang berisi kerangka umum pada halaman web. Lalu isi settings.py pada subdirektori aplikasi dan isi DIRS pada variabel TEMPLATES dengan BASE_DIR / 'templates'. Setelah itu, main.html yang sebelumnya sudah dibuat ditambahkan {% extends 'base.html' %} diawal lalu diberi {% block content %} dan {% endblock content %} sebelum dan sesudah kode program.
2. Form dibuat denngan cara membuat berkas baru pada direktori main dengan nama forms.py yang berisi struktur form untuk menerima data baru. Lalu, pada views.py dibuat fungsi baru yang menerima parameter request dan berisi form = ProductForm(request.POST or None) yang digunakan untuk membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST dan form tersebut harus divalidasi lalu disimpan ke server sebelum dilakukan return pada fungsi yang berisi perintah _redirect_ setelah data form berhasil disimpan.
3. Untuk mengetahui hasil pengambilan data di form, perlu ditambahkan key and value data yang telah diambil ke fungsi main programnya di views.py.
4. Setelah itu tambahkan _path url_ baru yang akan menavigasikan program menuju halaman pengisian form.
5. Pada direktori main/templates dibuatlah file html yang merupakan tampilan dari permintaan pengisian form pada website menggunakan syntax:
```
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>
```
6. Lalu tambahkan hasil pengisian form tersebut pada file html halaman utama degan cara mengakses data melalui object data yang telah mtersimpan di database melalui form.
7. Untuk pengembalian data dalam bentuk XML dan JSON, buat terlebih dahulu fungsi yang menerima parameter request yang menyimpan hasil query dari seluruh data yang ada pada product menggunakan data = Product.objects.all(). Lalu tambahkan _return function_ berupa HttpResponse yang diserialisasi menjadi XML ataupun JSON. Setelah itu tambahkan path pengambilan data tersebut pada urls.py dengan _path url_ menyesuaikan nama fungsi yang sudah dibuat di views.py.
8. Untuk pengembalian data berdasarkan ID dalam bentuk XML dan JSON. Step sama seperti nomor 7 hanya saja data = Product.objects.all() diganti menjadi data = Product.objects.filter(pk=id).

## Referensi:
1. https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=As%20you%20will%20see%20from,how%20that%20data%20is%20displayed.
2. https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST&text=Django's%20login%20form%20is%20returned,this%20to%20compose%20a%20URL.

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
## Django `UserCreationForm`
Pada framework Django, terdapat `UserCreationForm` yang dapat digunakan untuk membuat sebuah formulir yang dirancang untuk dapat mengumpulkan informasi yang dibutuhkan dalam pembuatan akun _user_ baru, seperti _username_ dan _password_, serta informasi tambahan lainnya seperti email.
### Kelebihan:
1. Mudah Digunakan: `UserCreationForm` menyediakan fungsi-fungsi yang sudah terdefinisi dengan baik, sehingga memudahkan pengembang web dalam mengimplementasikan fitur pendaftaran _user_ baru dengan cepat.
2. Validasi Bawaan: Form ini sudah dilengkapi dengan validasi bawaan, termasuk validasi untuk memastikan bahwa kata sandi yang dimasukkan cukup kuat dan tidak ada _user_ dengan _username_ yang sama.
3. Fungsionalitas yang Dapat Disesuaikan: Meskipun sudah memiliki fitur pendaftaran bawaan, `UserCreationForm` dapat dengan mudah disesuaikan sesuai kebutuhan aplikasi. _developer_ dapat menambahkan atau menghapus bidang-bidang tambahan yang diperlukan atau mengubah validasi sesuai dengan kebijakan keamanan aplikasi yang dibuat.
### Kekurangan:
1. Tidak Sesuai untuk Kasus Khusus: Jika aplikasi memiliki kebutuhan pendaftaran yang khusus, `UserCreationForm` mungkin tidak cukup fleksibel contohnya jika ingin mengaitkan informasi pendaftaran dengan aplikasi pihak ketiga. Oleh karena itu, `UserCreationForm` tidak akan bisa dipakai disemua aplikasi.
2. Tidak Mengatasi Semua Aspek Keamanan: Meskipun UserCreationForm menyediakan beberapa validasi bawaan, itu tidak mengatasi semua aspek keamanan. _Developer_ masih perlu memastikan bahwa aplikasinya memiliki keamanan yang kuat, seperti perlindungan terhadap serangan pencurian _session_ atau _SQL injection_.
3. Terbatas pada Fitur Bawaan Django: Formulir ini hanya mencakup fitur yang sudah ada dalam Django. Jika diperlukan fitur-fitur pendaftaran yang lebih canggih atau integrasi dengan alat otentikasi luar, _developer_ harus membuat formulir sendiri atau memodifikasi fitur yang ada pada `UserCreationForm`.

## Perbedaan antara autentikasi dan otorisasi dalam konteks Django
| **Autentikasi** | **Otorisasi** |
| --- | --- |
| Autentikasi adalah proses program dalam melakukan verifikasi kebenaran informasi pengguna yang memasukkan informasi kredensial dalam melakukan login, seperti _username_ dan _password_ sehingga hanya _user_ yang terdaftar pada sistem yang dapat mengakses website | Otorisasi adalah proses program menentukan hak akses atau izin apa saja yang dapat dilakukan dan tidak dapat dilakukan oleh _user_ setelah proses autentikasi dilakukan. |
| Berfungsi untuk memastikan bahwa hanya _user_ yang sah dan berwenang sesuai dengan yang sudah terdaftar pada sistem yang dapat mengakses akun atau sumber daya tertentu dalam website. | Berfungsi untuk melindungi informasi berupa data atau fitur tertentu dalam aplikasi dari akses yang tidak sah atau tidak seharusnya diberikan kepada sembarang _user_. |
| Contohnya, saat seorang pengguna mencoba masuk ke akunnya, sistem akan memeriksa apakah nama pengguna dan kata sandi yang dimasukkan cocok dengan data yang ada di database. Jika cocok, pengguna dianggap telah berhasil diautentikasi. | Contohnya, otorisasi menentukan apakah pengguna tersebut memiliki izin untuk melakukan tindakan tertentu, seperti mengedit profil mereka sendiri, menghapus postingan, atau mengakses halaman tertentu. |

Autentikasi dan otorisasi merupakan hal yang penting pada pengembangan aplikasi Django karena keduanya berperan secara integral dalam hal keamanan dari aplikasi tersebut. Dengan adanya autentikasi dan otorisasi, kontrol akses dan perlindungan data pada aplikasi menjadi lebih mudah dilakukan karena tidak sembarang orang dapat mengakses aplikasi dan tidak sembarang _user_ dapat mengakses data dan fitur dari aplikasi.

## Cookies dalam konteks aplikasi web dan penggunakan cookies untuk mengelola data sesi pengguna di aplikasi Django
Cookies adalah mekanisme dalam pengembangan aplikasi web yang digunakan untuk mempertahankan informasi _state_ atau _session_ antara klien (browser pengguna) dan server. Cookies digunakan untuk menyimpan data di sisi klien yang dapat digunakan oleh server untuk mengidentifikasi atau "mengingat" _user_ selama _user_ tersebut mengakses situs web. Cookies memungkinkan aplikasi web untuk mengatasi keterbatasan protokol HTTP yang _stateless_ dengan menyimpan informasi pada sisi klien dan mengirimkannya kembali ke server dalam setiap _request_.

Dalam aplikasi Django, _user_ yang berhasil login ke web aplikasi Django akan menerima _cookie session_ dari server. Cookie ini akan mengandung identifikasi unik yang digunakan oleh server untuk mengenali _user_ tertentu. Ketika _user_ pindah ke halaman lain atau melakukan _request_ lain di dalam web yang sama, cookie ini akan disertakan dalam setiap _request_ HTTP yang dikirimkan ke server. Ini memungkinkan server untuk "mengingat" pengguna yang telah login sebelumnya dan memberi mereka akses ke halaman atau sumber daya tertentu tanpa harus meminta login ulang setiap kali melakukan _request_.

Dengan demikian, cookies adalah mekanisme utama untuk mengimplementasikan "holding state" atau menyimpan informasi _session_ antara klien dan server dalam aplikasi Django. Adanya cookies memungkinkan aplikasi Django untuk mengelola status _user_ di antara _request_ HTTP yang berbeda, termasuk mempertahankan informasi otentikasi dan _session_ untuk pengguna yang sudah login.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat menjadi aman jika diimplementasikan dengan benar dan jika pengembangan mengikuti praktik keamanan yang tepat. Namun, ada risiko potensial yang harus diwaspadai agar cookies tidak digunakan dengan cara yang dapat mengancam keamanan dan privasi _user_. Untuk meminimalisir risiko tersebut sangat penting untuk memperhatikan tiga aspek dari penggunaan cookies, yaitu sebagai berikut:

1. Privasi _user_: _User_ sering kali merasa prihatin tentang privasi online mereka. Penggunaan cookies, terutama yang digunakan untuk pelacakan perilaku _user_, dapat memunculkan kekhawatiran privasi. _User_ mungkin merasa tidak nyaman jika mereka merasa aktivitas online mereka terlacak atau informasi pribadi mereka terpapar tanpa izin.
2. Penggunaan Data dan Pelacakan: Cookies dapat digunakan oleh perusahaan dan pihak ketiga untuk mengumpulkan data tentang perilaku _user_ dan preferensi mereka. Ini dapat digunakan untuk mengarahkan iklan dan menyesuaikan pengalaman online. Akan tetapi, beberapa _user_ mungkin merasa bahwa ini adalah pelacakan yang tidak seusai dengan prinsip privasi mereka.
3. Regulasi Privasi: Di berbagai yurisdiksi, ada regulasi yang ketat terkait penggunaan cookies, seperti GDPR di Uni Eropa dan CCPA di California. Penggunaan cookies harus mematuhi persyaratan regulasi ini, termasuk memberikan informasi yang jelas tentang penggunaan cookies dan memberikan opsi kepada pengguna untuk menolaknya.

Dalam semua aspek ini, penting bagi pengembang web dan pemilik situs web untuk mempertimbangkan dampak penggunaan cookies pada privasi dan hak pengguna serta untuk mematuhi regulasi yang berlaku. Ini dapat melibatkan pemberian informasi yang transparan tentang penggunaan cookies, memberikan pengguna opsi untuk mengelola cookies, dan mengikuti praktik-praktik keamanan dan privasi sesuai dengan hukum yang berlaku.

## Step by step implementasi autentikasi, session, dan cookies pada Django
### Membuat Fungsi dan Form Registrasi:
1. Membuka `views.py` dalam subdirektori "main" dan mengimpor modul yang diperlukan seperti `redirect`, `UserCreationForm`, dan `messages`.
2. Membuat fungsi `register(request)` yang akan meng-handle proses registrasi pengguna. Fungsi ini akan menggunakan `UserCreationForm` untuk membuat formulir registrasi.
3. Dalam fungsi `register`, jika metode HTTP adalah POST (pengguna telah mengirimkan formulir), maka formulir akan divalidasi dan jika valid, akun pengguna akan dibuat, dan pesan berhasil ditampilkan.
4. Membuat berkas HTML `register.html` untuk tampilan halaman registrasi. Formulir registrasi disediakan menggunakan `{{ form.as_table }}`.
5. Menambahkan URL path untuk fungsi registrasi ke dalam `urls.py`.

### Membuat Fungsi Login:
1. Membuka `views.py` dalam subdirektori "main" dan mengimpor modul yang diperlukan seperti `authenticate` dan `login`.
2. Membuat fungsi `login_user(request)` yang akan meng-handle proses login pengguna. Fungsi ini menggunakan `authenticate` untuk melakukan autentikasi berdasarkan _username_ dan _password_ yang diberikan.
3. Dalam fungsi `login_user`, jika autentikasi berhasil, pengguna akan di-redirect ke halaman utama, jika gagal, pesan error ditampilkan.
4. Membuat berkas HTML `login.html` untuk tampilan halaman login. Formulir login disediakan dengan input _username_ dan _password_.
5. Menambahkan URL path untuk fungsi login ke dalam `urls.py`.

### Membuat Fungsi Logout:
1. Membuka `views.py` dalam subdirektori "main" dan mengimpor modul `logout`.
2. Membuat fungsi `logout_user(request)` yang akan meng-handle proses logout pengguna. Fungsi ini akan melakukan logout, menghapus cookie, dan mengarahkan pengguna ke halaman login.
3. Menambahkan URL path untuk fungsi logout ke dalam `urls.py`.

### Merestriksi Akses Halaman Main:
1. Membuka `views.py` dalam subdirektori "main" dan mengimpor modul `login_required`.
2. Menambahkan decorator `@login_required(login_url='/login')` di atas fungsi `show_main` untuk membatasi akses halaman utama hanya untuk pengguna yang sudah login.
3. Menambahkan tombol "Logout" pada halaman utama (`main.html`).

### Menggunakan Data Dari Cookies:
1. Impor Modul `HttpResponseRedirect`, `reverse`, dan `datetime`
2. Dalam fungsi `login_user` gunakan `login(request, user)` untuk login pengguna, buat objek response dengan `HttpResponseRedirect`, set cookie `last_login` dengan waktu login terakhir, dan kembalikan objek `response`.
3. Menampilkan Data Cookie di Halaman Utama, yaitu dalam fungsi `show_main`, tambahkan `'last_login': request.COOKIES['last_login']`, ke dalam `context` untuk mengambil nilai cookie `last_login`.
3. Ubah `logout_user` untuk menghapus cookie `last_login` saat logout dengan menggunakan `response.delete_cookie('last_login')` untuk menghapus cookie tersebut.

### Menghubungkan Model Product dengan User:
1. Mengimpor modul `User` dari `django.contrib.auth.models` ke dalam `models.py`.
2. Menambahkan field `user` dengan tipe data `ForeignKey` pada model `Item` untuk menghubungkan produk dengan pengguna yang membuatnya.
3. Mengubah fungsi `create_item` untuk mengisi field user dengan pengguna yang sedang login sebelum menyimpan item.
4. Mengubah fungsi `show_main` untuk menampilkan item yang terasosiasi dengan pengguna yang sedang login.
5. Melakukan migrasi model untuk mengaplikasikan perubahan pada basis data.

## Referensi:
1. https://www.javatpoint.com/django-usercreationform 
2. https://vegibit.com/understanding-djangos-authentication-and-authorization-system/
3. https://www.blackhawkbank.com/blog/should-i-accept-cookies-on-every-website