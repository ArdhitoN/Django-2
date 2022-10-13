## Perbedaan antara asynchronous programming dengan synchronous programming.

- Synchronous programming bersifat single-thread dan dijalankan secara sekuensial, sedangkan asynchronous bersifat multi-thread dan tidak bergantung pada urutan (dapat berjalan secara paralel).
- Terdapat sistem blocking di dalam synchronous programming, dimana request akan dikirim ke server sekali dan kemudian hasilnya akan ditunggu. Sementara itu, asynchronous programming bekerja tanpa adanya blocking, dimana banyak request ke server dapat dilakukan di satu waktu yang sama.
- Karena kedua hal di atas, hasil kerja yang dihasilkan asynchronous programming akan lebih besar dan cepat dibandingkan synchronous programming.

## Paradigma Event-Driven Programming dan Contoh Penerapannya
Event-driven programming merupakan suatu paradigma pemrograman dimana suatu prosedur suatu algoritma pemrograman dijalankan jika terdapat suatu event/kejadian tertentu. Terdapat beragam event-triggerer, seperti mouseclick, keyboard-press, dan lain sebagainya. Setiap event dapat kita korelasikan dengan sebuah handler. Contoh penerapannya ialah saat user ingin menambahkan task, dimana jika mereka menekan tombol create-task, maka suatu modal tempat mereka mengisi data to-do baru akan muncul.

## Penerapan asynchronous programming pada AJAX.
Agar data yang ingin ditampilkan dapat muncul secara langsung tanpa mereload halaman, asynchronous programming dapat diterapkan, salah satunya dengan menggunakan AJAX (Asynchronous JavaScript and XML). Di saat terdapat suatu event tertentu, XMLHHttpRequest akan dibuat oleh JavaScript. Kemudian, XMLHttpRequest akan mengirimkan HTTPrequest ke server, dimana server akan memrposes HTTPrequest tersebut dan hasilnya akan diserahkan kembali ke browser untuk diproses dengan JavaScript.

## Langkah Implementasi
- Menerapkan AJAX GET
1. Membuat views yang mengembalikan data dalam bentuk json, dan views untuk menambah data dengan memanfaatkan forms. Lalu membuat pemetaannya di urls.py
2. Melakukan konfigurasi pada file HTML dengan mengaplikasikan asynchronous javaScript programming dengan memanfaatkan keyword fetch, await, dan async.