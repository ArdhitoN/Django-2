# Assignment-3 : Data Delivery
Tampilan antarmuka mywatchlist dapat dilihat melalui tautan berikut : 
https://cata-log.herokuapp.com/mywatchlist/html/

Data aplikasi mywatchlist dalam format xml dan json dapat dilihat melalui tautan di bawah ini. Untuk dapat melihat data berdasarkan id yang dimilikinya, masukkan nomor id dari data-object (1-10) di paling belakang dari url.
https://cata-log.herokuapp.com/mywatchlist/xml/

https://cata-log.herokuapp.com/mywatchlist/json/

## Apa itu HTML, XML, JSON? Dan Apa Perbedaan Antara Ketiganya?

### HTML
HTML (Hypertext Markup Language) merupakan suatu bahasa yang dirancang untuk menstrukturisasi halaman web.


### XML
XML(eXtensible Markup Language) merupakan bahasa yang digunakan untuk menyimpan data. Di dalam XML, setiap elemen akan memiliki opening tag dan closing tag, terkecuali untuk prolog XML yang digunakan untuk mendefinisikan tipe encoding dan versi dari XML. Meskipun begitu, eksistensi dari prolog XML bersifat opsional. 

### JSON
Sama seperti XML, JSON (JavaScript Object Notation) merupakan suatu bahasa yang digunakan untuk menyimpan data yang berisi objects. Cara pendefinisian object dalam JSON sama dengan pendefinisian object di JavaScript, dimana object "dibungkus" dalam sebuah tanda kurung kurawal ({ }), dimana atribut dari object tersebut akan ditulis dengan format key: value. Value dari atribut tertentu dapat diperoleh melalui key yang sesuai.  

### Perbedaan HTML, XML, dan JSON
- Fungsi HTML berfokus untuk **menampilkan** data pada halaman web, sedangkan XML dan JSON lebih berfokus untuk **mendeskripsikan** data

- Data/elemen dalam JSON diformat dalam bentuk **object** sebagaimana dalam JavaScript. Di sisi lain, data/elemen pada HTML dan XML "dibungkus" di dalam **tag**.  

- Tags untuk XML element (kecuali prolog) selalu terdiri atas opening tag dan closing tag. Sementara itu, pada tags pada elemen HTML tidak selalu terdiri atas kedua entitas tersebut (terdapat self-closing tag).

- Karena format data di dalam JSON relatif lebih simple dan padat dibandingkan dengan format pada XML, file-size yang dihasilkan JSON akan relatif lebih kecil dibandingkan file-size XML. Oleh karenanya, data delivery dengan JSON relatif lebih cepat dibandingkan dengan data delivery menggunakan XML.


## Mengapa Kita Memerlukan Data Delivery Dalam Sebuah Platform?
Dalam sebuah platform, tentu diperlukan sebuah interaksi yang dinamis antara aplikasi dengan penggunanya. Oleh karena itu, data yang ada harus selalu bersifat valid dan up-to-date melalui pemrosesan data (baik masuk maupun keluar). 

Untuk mendukung performa dari sistem di dalam platform, dibutuhkan *data delivery* yang bersifat efektif dan efisien. Hal tersebut dapat dilakukan dengan mengoptimalisasi model saat menstrukturisasi database. Selain itu, penggunaan format data yang sesuai juga menjadi salah satu hal yang perlu dipertimbangkan. 

## Langkah Implementasi Pembuatan Aplikasi

### Inisialisasi 
Sebelumnya, kita perlu masuk ke dalam directory dimana root project berada. Setelahnya, kita dapat menyalakan virtual environment untuk mengisolasikan kegiatan yang akan kita lakukan. Setelahnya, kita dapat mengirim perintah berikut untuk menginisialisasikan aplikasi baru:

```python manage.py startapp mywatchlist```

Note : Sebelumnya, beberapa langkah untuk inisialisasi aplikasi sudah terlalui, sehingga langkah yang tercantum disini secara khusus diperuntukkan untuk aplikasi mywatchlist. 

### Menambahkan Path mywatchlist Sehingga Pengguna Dapat Mengakses http://localhost:8000/mywatchlist

Masukkan path('mywatchlist/', include('mywatchlist.urls')) sebagai salah satu elemen di dalam variabel urlpatterns yang ada di dalam file urls.py (di folder root project) sebagai berikut:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls'))
]
```

### Membuat Model Untuk Data di Dalam Aplikasi
Di dalam file models.py yang terdapat di folder mywatchlist, kita akan membuat sebuah class yang akan menjadi blueprint dari object-object data dengan langkah sebagai berikut:

#### Mengimpor modul models yang akan dipergunakan untuk membuat model dan mendefinisikan atribut dari object, serta class MaxValueValidator dan MinValueValidator yang akan dipergunakan untuk mendefinisikan batasan value yang valid dari nilai rating dengan perintah:
```
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
```


Membuat sebuah class bernama MyWatchList yang akan mengextend class Model, dengan atribut: 

- title (tipe datafield berupa karakter dengan tambahan argumen max_length untuk mendefinisikan panjang maksimum dari field)
- rating (tipe datafield berupa bilangan desimal dengan tambahan argumen max_digits = 3 untuk memberikan batasan agar maksimum digit yang dapat diinput ialah sebanyak 3. Selain itu, terdapat argumen decimal_places=2 yang berarti digit yang akan diperuntukan untuk bilangan di belakang koma ialah sebanyak 2 digit. Dan yang terkahir, terdapat tambahan argumen validators=[MinValueValidator(1) ,MaxValueValidator(5)] untuk mengatur nilai minimum (1) dan nilai maksimum dari rating (5).) 
- release_date (tipe datafield berupa tanggal)  
- review (tipe datafield berupa text)
- is_watched (tipe datafield berupa boolean)

Hal tersebut diimplementasikan dengan kode berikut:
```
class MyWatchList(models.Model):
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators= [MinValueValidator(1) ,MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()
    is_watched = models.BooleanField()
```

### Menambahkan Data Untuk Objek MyWatchList
Untuk menambahkan data yang merupakan objek MyWatchList, kita dapat membuat sebuah dokumen JSON dengan path : 
folder root project > folder mywatchlist > folder fixtures > file dokumenJSON). 
Setelahnya, kita dapat mulai membuat object berdasarkan model yang telah dibuat di file models.py dengan cara sebagai berikut:

- inisiasikan sebuah tanda kurung kotak ([ ]) yang akan menjadi penampung dari setiap data-object yang akan dibuat berdasarkan model.
- Setiap data-object "dibungkus" dalam sebuah tanda kurung kurawal ({ }), dimana di dalamnya terdapat pasangan key-values yang akan mendefinisikan atribut dari data-object. 
- Berdasarkan konvensi pendefinisian data berdasarkan models dari Django, setiap data memiliki 3 key, yaitu "models" dengan value "{nama_folder_aplikasi}.{nama_class_model}" (tanpa tanda { }), "pk" dengan value angka tertentu dari 1 hingga seterusnya (sebagai id), dan "fields" dengan value pendefinisian atribut-atribut dari object-model. 
- Antara satu object dengan object lain dipisahkan dengan tanda koma (,)
- Salah satu contoh pengaplikasiannya ialah sebagai berikut (untuk 2 object) :

```
[
    {
        "model" : "mywatchlist.mywatchlist",
        "pk" : 9,
        "fields":{
            "title" : "Luck",
            "rating": 5.00,
            "release_date": "1921-02-11",
            "review" : "Proin turpis turpis, eleifend et mauris vel, vulputate placerat ante. Suspendisse bibendum lacus ac hendrerit posuere. ",
            "is_watched": true
        }
    },

    {
        "model" : "mywatchlist.mywatchlist",
        "pk" : 10,
        "fields":{
            "title" : "Monsters, Inc.",
            "rating": 4.99,
            "release_date": "1921-02-11",
            "review" : "-",
            "is_watched": false
        }
    }
]
```
Untuk 10 data-object yang ditambahkan, Anda dapat melihatnya di file initial_mywatchlist_data.json.


Setelah itu, kita dapat memigrasikan schema model yang telah dibuat ke database dengan perintah:
`python manage.py makemigrations` untuk tahap persiapan migrasi, dan `python manage.py migrate` untuk menerapkan skema model.


Setelahnya, kita dapat memasukkan data yang telah dibuat di dalam file initial_mywatchlist_data.json dengan perintah `python manage.py loaddata initial_mywatchlist_data.json`.

### Mengimplementasikan sebuah fitur untuk menyajikan data dalam format HTML, XML, dan JSON
Untuk dapat menyajikan data dalam bentuk HTML, dibentuk sebuah fungsi yang menerima argumen request dari client. Fungsi tersebut akan mengembalikan hasil dari rendering data ke template html. Berikut ialah kode untuk fungsi tersebut:
```
def show_html(request):
    watchlist_objects = MyWatchList.objects.all()
    context  = {
        'watchlist_list': watchlist_objects,
        'name' : "Ardhito Nurhadyansah",
        'NPM' : "2106750206",
    }
    return render(request, "mywatchlist.html", context)
``` 

Sementara itu, untuk mengembalikan data dalam bentuk XML, kita dapat membuat sebuah fungsi yang menerima argumen request dari client dan mengembalikan hasil dari fungsi HttpResponse. Argumen di dalam fungsi HttpResponse berupa data yang diserialisasikan ke dalam format xml dengan fungsi serialize dari modul serializers. Argumen pertama dalam fungsi serialize ialah format hasil serialisasi yang diinginkan, sedangkan  argumen kedua berisi data yang ingin diserialisasikan. 

```
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

Untuk mengembalikan data dalam format json, kita dapat membuat suatu fungsi yang memiliki struktur yang sangat mirip sebagaimana jika kita ingin mengembalikand data dalam format XML. Perbedaannya hanya terletak pada argumen pertama di fungsi serialize, dimana kita ingin menserialisasikan data ke format json. 
```
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Berikut ialah fungsi yang mengembalikan data berdasarkan id, dimana object yang diambil difilter terlebih dahulu agar sesuai dengan id yang direquest client. 

Untuk format xml:
```
def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```


Untuk format json:
```
def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat routing untuk melihat data yang telah disajikan 
Untuk melakukan routing agar data yang telah disajikan dapat dilihat menggunakan browser, kita dapat mengimpor fungsi path dan fungsi-fungsi yang telah kita buat sebelumnya di views.py ke urls.py yang terdapat di folder aplikasi mywatchlist. Setelahnya, kita dapat menambahkan path baru sebagai elemen di urlpatterns dengan memanfaatkan fungsi path. Argumen pertama berisi routing untuk alamat dari response, sedangkan argumen kedua diperuntukkan untuk nama fungsi dari views.py yang akan dijalankan. 
```
from django.urls import path
from .views import show_html
from .views import show_xml 
from .views import show_json
from .views import show_html
from .views import show_json_by_id 
from .views import show_xml_by_id 

app_name = 'mywatchlist'

urlpatterns = [
    path('xml/', show_xml, name= 'show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]
```

### Hasil akses URL menggunakan Postman
HTML:
<br>
![HTML](https://github.com/ArdhitoN/Django-2/blob/main/mywatchlist/HtmlAccessResult.png?raw=true) <br>

XML:
<br>
![XML](https://github.com/ArdhitoN/Django-2/blob/main/mywatchlist/XMLAccessResult.png?raw=true) <br>
    
JSON:
<br>
![JSON](https://github.com/ArdhitoN/Django-2/blob/main/mywatchlist/JsonAccessResult.png?raw=true) <br>


### Pembuatan Test
Untuk membuat test yang akan mengecek respons dari URL, kita dapat memanfaatkan class TestCase dan class Client. Pertama-tama, kita dapat membuat sebuah class bernama MyWatchlistTestCase yang mengextend class TestCase. Setelahnya, kita dapat mendefinisikan fungsi test untuk masing-masing URL yang sudah didefinisikan sebelumnya. Di dalam fungsi tersebut, kita dapat membuat suatu object Client, kemudian menggunakan method get dengan argumen path URL yang ingin ditest. Hasil dari response tersebut akan dibandingkan dengan value 200. Jika sama, artinya request telah sukses dan responsenya sudah OK.

Berikut merupakan code untuk tests.py yang diperuntukkan untuk aplikasi mywatchlist:

```
import unittest
from django.test import Client

class MyWatchlistTestCase(unittest.TestCase):
    def test_html(self):
        client = Client()
        response = client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        client = Client()
        response = client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        client = Client()
        response = client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)

```
