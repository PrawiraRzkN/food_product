# Aplikasi pengatur penjualan produk-produk makanan nusantara.
Tautan menuju aplikasi Adaptable: https://foodproduct-management.adaptable.app

## **Step by step deploy proyek baru**
1. Membangun proyek Django baru, yaitu membuat terlebih dahulu direktori baru bernama 'food_product'. Lalu menjalankan virtual environment untuk direktori tersebut untuk mengisolasi dependencies yang akan diinstall, termasuk Django itu sendiri. Setelah dependencies terinstall, dilakukan konfigurasi dan dijalankan server dari proyek ini. Jika berhasil, maka direktori baru ini di unggah ke repository github baru dengan nama yang sama.
2. Pada direktori 'food_product' dibuat aplikasi baru bernama 'main' dengan memanfaatkan virtual environtment dan membuat munculnya folder baru bernama main pada direktori 'food_product'. Tidak lupa, aplikasi main ditambahkan ke INSTALLED_APPS pada settings.py sehingga proyek mengetahui penambahan aplikasi tersebut.
3. Model dibuat pada tahap ini dengan nama Item dan berisi atribut wajib, yaitu name, amount, dan description dengan tipe data masing-masing sesuai arahan pada soal. Lalu saya menambahkan atribut date_added, price, category, dan origin sesuai dengan keperluan aplikasi. Setelah model tersebut dibuat, model harus dimigrasi agar penambahan atau perubahannya dapat terefleksi oleh Django.
4. Aplikasi main yang sudah dibuat tersebut harus dibuatkan routingnya pada proyek, yaitu dengan cara menghubungkan urls.py yang ada pada direktori 'food_product' dengan urls.py baru yang ada dalam direktori 'main'. Dengan begitu, fungsi yang ada di views.py, berisi data dari model, terpetakan.
5. Dilakukan unit testing terlebih dahulu agar kode yang dibuat pada direktori berjalan sesuai dengan yang diharapkan.
6. Repository pada github diupdate sesuai dengan perubahan pada direktori 'food_product'.
7. Aplikasi siap untuk dilakukan deployment ke Adaptable dengan cara membuat terlebih dahulu aplikasi Adaptable yang terintegrasi pada repository 'food_product' pada github.

## **Proses request client ke web aplikasi berbasis Django**
![Alt text](img-properties/bagan-client-request.jpg)
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
| **MVC** | **MVT** | **Controller** |
| --- | --- | --- |
|Pola desainnya diatur agar dapat digunakan dalam pengembangan berbagai jenis aplikasi seperti aplikasi dekstop, web, dan mobile. Dalam model ini, Model dan View dipisahkan Controller sehingga developer harus mengelola Controller secara manual apabila terdapat perubahan pada Model maupun View. | MVT adalah desain yang dibuat untuk pengembangan aplikasi basis website. Terdapat Template yang akan mengatur tampilan halaman web dan akan mengurus pembaruan tampilan secara otomatis ketika data berubah. | Desain MVVM sering digunakan dalam aplikasi berbasi User Interface seperti aplikasi mobile atau dekstop. Desain ini memiliki ViewModel yang akan memisahkan Model dan View seutuhnya sehingga keduanya tidak saling bergantung. MVVM ini mengandalkan sistem data binding, yaitu sistem yang akan secara otomatis melakukan pembaruan ketika terjadi perubahan data yang dibaca oleh ViewModel. |


