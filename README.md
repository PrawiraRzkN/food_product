# Aplikasi pengatur penjualan produk-produk makanan nusantara.
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

# Implementasi Form dan _Data Delivery_ pada Django
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