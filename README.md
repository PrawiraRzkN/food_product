Aplikasi pengatur penjualan produk-produk makanan nusantara.
Tautan menuju aplikasi Adaptable: https://foodproduct-management.adaptable.app

Pertanyaan-Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Jawaban:
    - Membangun proyek Django baru, yaitu membuat terlebih dahulu direktori baru bernama 'food_product'. Lalu menjalankan virtual environment untuk direktori tersebut untuk mengisolasi dependencies yang akan diinstall, termasuk Django itu sendiri. Setelah dependencies terinstall, dilakukan konfigurasi dan dijalankan server dari proyek ini. Jika berhasil, maka direktori baru ini di unggah ke repository github baru dengan nama yang sama.
    - Pada direktori 'food_product' dibikin aplikasi baru bernama 'main' dengan memanfaatkan virtual environtment dan membuat munculnya folder baru bernama main pada direktori 'food_product'. Tidak lupa, aplikasi main ditambahkan ke INSTALLED_APPS pada settings.py sehingga proyek mengetahui penambahan aplikasi tersebut.
    - 
    - Model dibuat pada tahap ini dengan nama Item dan berisi atribut wajib, yaitu name, amount, dan description dengan tipe data masing-masing sesuai arahan pada soal. Lalu saya menambahkan atribut date_added, price, category, dan origin sesuai dengan keperluan aplikasi. Setelah model tersebut dibuat, model harus dimigrasi agar penambahan atau perubahannya dapat terefleksi oleh Django.
    - Aplikasi main yang sudah dibuat tersebut harus dibuatkan routingnya pada proyek, yaitu dengan cara menghubungkan urls.py yang ada pada direktori 'food_product' dengan urls.py baru yang ada dalam direktori 'main'. Dengan begitu, fungsi yang ada di views.py, berisi data dari model, terpetakan.
    - Dilakukan unit testing terlebih dahulu agar kode yang dibuat pada direktori berjalan sesuai dengan yang diharapkan.
    - Repository pada github diupdate sesuai dengan perubahan pada direktori 'food_product'.
    - Aplikasi siap untuk dilakukan deployment ke Adaptable dengan cara membuat terlebih dahulu aplikasi Adaptable yang terintegrasi pada repository 'food_product' pada github.

2. 
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Jawaban:
    Aplikasi web berbasis Django dibuat dengan virtual environment untuk mengisolasi dependencies dari system milik komputer. Sehingga perubahan sistem yang terjadi pada komputer atau proyek lainnya tidak akan mempengaruhi stabilitas proyek yang sedang dikembangkan. Selain itu, virtual environment digunakan juga agar sistem dapat menjalankan lebih dari satu proyek Django pada satu komputer saja. Aplikasi web berbasis Django juga dapat dibuat tanpa virtual environment, namun hal tersebut tidak disarankan karena bisa jadi adanya konflik antar sistem yang berjalan di komputer atau proyek lainnya dengan proyek yang sedang dibuat.
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    Jawaban:
    


