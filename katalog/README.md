# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Oleh: Ardhito Nurhadyansah

NPM : 2106750206

App-link: https://cata-log.herokuapp.com/katalog/

# Bagaimana Aplikasi Web Berbasis Django Bekerja

Secara umum, cara kerja aplikasi web berbasis Django dapat dilihat melalui ilustrasi di bawah ini.
<br>

![Image](https://raw.githubusercontent.com/ArdhitoN/Django-2/main/katalog/HowDjangoWorks.png)

Pada awalnya, client akan mengirimkan HTTP request ke server untuk mengakses halaman aplikasi web. Request tersebut akan diterima oleh server dan dikirim ke urls.py. Di dalam urls.py, akan dilakukan parsing(pemecahan) dan deteksi terhadap argumen-argumen yang ada dengan menggunakan regular expression. Setelahnya, setiap argumen yang terolah dikirim ke views yang sesuai, dimana views akan melakukan komunikasi dengan komponen-komponen lainnya seperti models dan sisi template. Komunikasi antara views.py dan models bertujuan untuk memperoleh data dari database dan/atau mengirimkan data ke database. Dalam hal ini, models berperan untuk memanipulasi data secara langsung (Create, Read, Update, Delete) sesuai dengan query yang dikirim views, dimana hasilnya akan dikirimkan kembali untuk dipetakan ke sisi template. Hasil akhir dari proses pemetaan tersebut akan dikirimkan sebagai HTTP response ke client. 

# Apa Itu Virtual Environment dan Mengapa Kita Menggunakannya?
Virtual environment merupakan sebuah tempat yang dapat mengisolasikan project yang sedang kita kerjakan. Penggunaan virtual environment bersifat opsional, namun sangat dianjurkan. Dengan menggunakan virtual environment, library, dependency, interpreter, dan berbagai hal lain yang dipergunakan dalam suatu project dapat terpisah dengan project lainnya. Dengan begitu, proses pengembangan project tidak mempengaruhi dan/atau bergantung pada situasi eksternal.



# Cara Pembuatan Aplikasi Web

## Langkah Pengambilan Data dari Model dan Pemetaannya ke Dalam Template

Untuk melakukan pengambilan data dari model ke views, kita perlu mengimpor Data Model yang ada pada models.py di dalam views.py. Hal tersebut dilakukan melalui perintah:
```
from katalog.models import CatalogItem
```
Setelahnya, kita dapat memperoleh seluruh data object model dari database dan menyimpannya dalam suatu variabel dengan perintah berikut:
```
catalog_items_data = CatalogItem.objects.all()
```
Untuk melengkapi data yang akan dipetakan ke sisi template, kita dapat membuat sebuah dictionary yang mengandung semua data yang diperlukan, contohnya ialah sebagai berikut:
```
context = {
    'catalog_list' : catalog_items_data,
    'name' : 'Ardhito Nurhadyansah',
    'NPM'  : "2106750206",
}
```

Lalu, kita dapat mulai melakukan proses pemetaan/rendering antara data yang kita miliki ke file template dengan memanggil fungsi render dengan 3 argumen, yaitu request yang berasal dari client, file template yang akan diisi, serta data yang akan dipetakan ke file tempalate sebagai berikut:
```
render(request, "katalog.html", context)
```
Hasil dari fungsi render tersebutlah yang akan direturn sebagai HTTP response ke client-side.

<hr>

## Langkah Pembuatan Routing Terhadap Fungsi di Views
Pertama, di dalam file urls.py yang terdapat di dalam folder aplikasi yang ingin dibuat (dalam hal ini katalog), kita perlu mengimpor fungsi path dan fungsi yang ingin kita gunakan dari views. Hal tersebut dilakukan dengan perintah:

```
from django.urls import path
from katalog.views import show_katalog
```
Setelahnya, kita dapat menambahkan routing fungsi yang ingin digunakan dari views ke dalam variabel urlpatterns dengan menggunakan fungsi path sebagai berikut:
```
urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
`path('', show_katalog, name='show_katalog')` memiliki 3 argumen, dimana argumen pertama menunjukkan route, argumen kedua menunjukkan fungsi di dalam view yang ingin dirouting, dan argumen ketiga ditujukan untuk penamaan.

Selain itu, di dalam urls.py yang ada di dalam folder project (dalam hal ini project_django), kita perlu menambahkan path katalog.url ( `path('katalog/', include('katalog.urls'))` ) sebagai elemen di dalam urlpatterns. Argumen pertama dalam fungsi path dimaksudkan untuk menunjukkan route, dan argumen kedua dimaksudkan untuk memasukkan elemen url dari aplikasi yang ingin kita buat.

## Langkah Pemetaan Data di dalam Internal Template File

Untuk melakukan pemetaan di dalam file internal template (dalam hal ini file HTML), kita dapat melakukannya dengan menggunakan konvensi sintaks dari Django. Untuk menampilkan sebuah nilai dari suatu variabel tertentu, kita dapat menggunakan sintaks seperti berikut:`{{nama_variabel}}`

Data yang dipassing sebagai argumen dalam fungsi render (yaitu context) akan dipetakan di dalam katalog.html. Untuk mengakses masing-masing data yang telah dikemas di dalam sebuah dictionary sebagai values, kita dapat mengaksesnya dengan memanggil keys dari values tersebut. 

Jika data yang dibutuhkan merupakan atribut spesifik dari object, kita dapat mengakses atribut tersebut dengan sintaks: `objek.nama_atribut`.

## Langkah Untuk Melakukan Deployment Aplikasi ke Heroku
Untuk melakukan deployment, kita dapat merujuk ke tutorial di dalam [Lab0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0). Pertama, kita perlu membuat sebuah aplikasi baru di heroku. Selanjutnya, diperlukan konfigurasi awal pada GitHub Actions dengan membuka Settings > Secrets > Actions. Di sana, kita perlu menambahkan repository secret baru dengan spesifikasi key-value pair sebagai berikut:
```
HEROKU_API_KEY: VALUE_API_KEY
HEROKU_APP_NAME: NAMA_APLIKASI_HEROKU
```
Kemudian, kita dapat melakukan push terhadap file-file yang telah kita ubah di dalam project/aplikasi Django yang kita buat dan mendeploynya ke repository GitHub.

<<<<<<< HEAD
Setelahnya, aplikasi Django akan dapat diakses secara global menggunakan internet.
=======
Setelahnya, aplikasi Django akan dapat diakses secara global menggunakan internet.
>>>>>>> edecd176b00166506f5d443558388aa8c6bc13a0
