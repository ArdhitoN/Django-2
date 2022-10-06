Tautan aplikasi : https://cata-log.herokuapp.com/todolist/


## Kegunaan {% csrf_token %} Pada Elemen <form>

Tujuan utama penggunaan {% csrf_token %} ialah untuk mencegah dan memproteksi aplikasi dari serangan Cross Site Request Forgery (CSRF). Serangan dilakukan dengan memanfaatkan kredensial dari dari user yang telah terautentikasi dengan mengubah request yang mereka lakukan sehingga pada akhirnya korban melakukan hal yang tidak mereka inginkan. Misalnya, korban dapat masuk ke suatu link tanpa keinginannya sendiri ketika melakukan sesuatu. Elemen `{% csrf_token %}` akan membuat sebuah token di server ketika proses rendering halaman web dilakukan. Token tersebut berupa kode alfanumerik atau nilai rahasia yang bersifat acak dan bersifat khusus untuk situs. Setiap request yang masuk akan dicek melalui token tersebut. Oleh karena itu juga, aktivitas POST melalui form hanya akan dapat berjalan jika domain dimana ia berasal dapat dipercaya. 

## Pembuatan Elemen <form> Secara Manual 
Elemen form dapat dibuat secara manual langsung di html, dimana terdapat pre-defined tag untuk membuatnya. 

Form dapat diinisiasikan dengan opening dan closing tag `<form></form>`, dimana di dalamnya kita dapat mendefinisikan atribut action dan method yang diinginkan. 

Di dalam tag form tersebut, kita dapat membuat elemen-elemen input dengan tag `<input>` .

Tipe dari tag input tersebut dapat dimodifikasi dengan atribut type. Untuk dapat melakukan submisi terhadap form, kita dapat menginisiasikan sebuah elemen input dengan tipe submit seperti berikut:

`<input type="submit">` 

## Alur Data (Submisi - Pop-up Data di Template HTML)
Sebelumnya, form dapat dikalibrasi sedemikian rupa sehingga dapat menampung isi yang sesuai dengan suatu model tertentu yang telah kita definisikan di models.py.Pertama-tama, jika user telah menginput jawaban untuk form dan melakukan submisi, hasilnya akan dikirim melalui HTTP Request dengan method POST. Kemudian, views yang sesuai akan menerima request tersebut. Di sana, hasil input form akan dicek validitasnya. Jika form tersebut valid, maka hasil dari form akan disave menuju database. Kemudian jika user kembali ke halaman utama, fungsi views yang sesuai akan kembali dipanggil dan pada akhirnya data yang baru saja dibuat akan tersedia.

## Langkah Implementasi
1. Melakukan inisialiasi aplikasi melalui command `python manage.py startapp todolist` 
2. Mendaftarkan aplikasi todolist di settings.py
3. Mendaftarkan path todolist di urls.py yang berada di folder project_django dengan menambahkan `path('todolist/', include('todolist.urls'))` sebagai salah satu elemen baru di urlpatterns.
4. Membuat forms.py untuk melakukan konfigurasi terhadap object Form.
5. Menginisiasikan template todolist.html (home aplikasi), register.html(untuk halaman register), login.html(untuk halaman login), create-task.html(halaman untuk menambahkan task) di (folder todolist > folder templates)
6. Membuat model Task di models.py yang berada di folder todolist dengan atribut user, date, title, dan description dengan tipe data yang sesuai. Pada atribut user, object Task akan menampung ForeignKey User untuk menunjukkan adanya relasi antara keduanya (Eksistensi Task akan bergantung pada User). Jika User didelete, maka Task yang terhubung dengannya akan ikut terdelete dengan atribut on_delete=models.CASCADE
7. Melakukan migrasi model
8. Mendefinisikan fungsi show_todolist di views.py yang berada di folder todolist untuk memberikan hasil render todolist.html yang telah dibuat dengan data yang ada di database.
9. Untuk dapat melihat home serta membuat proses registrasi, login, create-task, dan logout, berjalan dengan baik kita perlu mendefinisikan views yang sesuai untuk masing-masing fitur tersebut.

Untuk merender home aplikasi:
```
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_objects = Task.objects.filter(user = request.user)
    context  = {
        'todolist_list' : todolist_objects,
    }
    return render(request, "todolist.html", context)
```
Dari kode di atas, dapat terlihat bahwa user harus login terlebih dahulu untuk dapat mengakses halaman home, sehingga user akan langsung diredirect menuju halaman login. Jika sudah login, maka objek Task yang terikat dengan user akan diambil melalui filterisasi. Kemudian, data tersebut akan dipetakan menuju todolist.html dan hasilnya akan dikembalikan sebagai response. 


Untuk fitur register:
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Pada kode di atas, terlihat bahwa pada awalnya kita membuat sebuah instance form untuk membuat User baru. Jika pengguna mengirimkan hasil input mereka dengan method POST, maka hasil tersebut akan dicek validitasnya. Jika valid, maka pengguna baru akan disave di database.

Untuk fitur login:
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
Dari kode di atas, terlihat bahwa jika user telah mensubmit username dan passwordnya, maka kedua value tersebut akan diambil. Kemudian, user akan dicek autentikasinya dengan fungsi authenticate. Jika user telah terdaftar di database, maka login akan dilakukan dengan method login. Jika kondisinya sebaliknya, maka akan terdapat pesan bahwa username atau password yang diinput salah.

Untuk fitur create-task:
```

def create_task(request):
    response = {'input_form' : Input_Form}
    if request.method == 'POST':
        user = request.user
        form = Input_Form(request.POST or None)
        form.instance.date = datetime.datetime.now()
        form.instance.user = user
        if(form.is_valid and request.method == 'POST'):
            form.save()
    
    return render(request, 'create-task.html', response)
```
Dari kode di atas, terlihat bahwa pada awalnya, kita akan mengambil model form yang telah didefinisikan. Kemudian, jika form telah disubmit, hasilnya akan diambil. Perlu diperhatikan bahwa kita dapat mengakses hasil instance dari form tersebut dengan memanggil atribut instance dari hasil submit form. Hasil instance merupakan objek dengan kelas Task, karena pada pendefinisian Input_Form, kita mendefinisikan atribut model=Task. Dengan begitu, kita perlu memasukkan atribut date dan user, dimana kedua atribut tersebut tidak diinput di saat user menambahkan task baru. Hal tersebut dilakukan dengan memetakan atribut date dan user dari instance dengan value yang sesuai. Setelahnya, akan dilakukan pengecekan terhadap hasil form. Jika valid, maka hasilnya akan disave di database. Setelahnya, user akan tetap berada di situs yang sama, sehingga ia dapat menambahkan task baru berkali-kali. Jika ia ingin melihat task yang telah ia buat, ia dapat menekan tombol home. 

Untuk fitur logout:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response
```
Dapat dilihat bahwa pada kode di atas, akan dimanfaatkan fungsi logout dari Django. Setelahnya, user akan diredirect menuju halaman login.

10. Melakukan routing sehingga fitur-fitur yang telah dibuat dapat diakses melalui web/internet sebagai berikut : 
```
from django.urls import path

from .views import register
from .views import login_user
from .views import logout_user
from .views import show_todolist
from .views import create_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]
```
Pada kode di atas, dapat dilihat bahwa pada awalnya kita perlu mengimpor fungsi views untuk fitur-fitur yang ada. Selanjutnya, kita menambahkan path baru untuk menampilkan hasil dari pemrosesan fungsi-fungsi tersebut. 

11. Melakukan 3 mantra git yaitu git add, git commit, dan git push untuk mendeploy aplikasi.
12. Membuat 2 akun dummy dengan masing-masing diisi 3 dummy-task-data dengan langsung terjun ke halaman web untuk meregestrasikan 2 user baru, melakukan login, dan menambahkan 3 task baru untuk masing-masing user dengan memanfaatkan fitur create-task. 
Akun yang dibuat :

nama : dummy88 | password: GviMf2WJ4AfD2he

nama : dummy02 | password : h6jwcMWiWuGcw7i



===================================================
# CSS & Styling
## Perbedaan Inline, Internal, dan External CSS
Berdasarkan metode penggunaannya: 
- Inline CSS disimpan di dalam tag elemen HTML dengan mendefinisikan atribut `style` pada elemen. Atribut tersebut berisi properti CSS yang ingin diaplikasikan.
- Internal CSS disimpan di antara opening dan closing tag style yang didefinisikan di section head. Properti CSS yang ingin diaplikasikan akan disimpan di antara kedua tag tersebut, dimana kita dapat menggunakan selector untuk melakukan editorial pada kelompok/elemen yang spesifik.
- Eksternal style CSS disimpan di luar file HTML (terpisah) dengan file extension `.css`. Untuk dapat mengintegrasikan file HTML dengan eksternal style CSS, kita perlu memasukkan elemen link yang merujuk ke file external CSS di file HTML.


## Kelebihan dan Kekurangan Inline, Internal, dan External CSS

### Inline CSS
Kelebihan:
- Adanya elemen dan styler yang lebih terintegrasi dalam satu tempat, dimana kondisi ini dapat memudahkan developer untuk melakukan testing. Selain itu juga, hal tersebut menyebabkan styling jenis ini cocok untuk project yang berukuran kecil dan editorial hanya dibutuhkan untuk elemen tertentu saja.

Kekurangan:
- Kurangnya modularitas dan pemisahan antara konstruktor halaman web dengan editornya. Sehingga untuk skala project yang lebih besar akan membuat struktur code menjadi lebih panjang dan pada akhirnya menurunkan readibility.
- Menambah size dari file HTML, sehingga dapat meningkatkan load-time.
### Internal CSS
Kelebihan:
- Cocok untuk project yang berukuran kecil dan hanya mencakup 1 halaman karena konstruktor dan editor yang berada di 1 tempat.

Kekurangan:
- Kurangnya modularitas dan pemisahan antara konstruktor halaman web dengan editornya. Sehingga untuk skala project yang lebih besar akan membuat struktur code menjadi lebih panjang dan pada akhirnya menurunkan readibility.
- Menambah size dari file HTML, sehingga dapat meningkatkan load-time.

### External CSS
Kelebihan:
- Memiliki skala aksesibilitas editorial yang lebih besar, sehingga cocok digunakan untuk melakukan styling pada project yang besar.
- Meningkatkan modularitas dan pemisahan struktural antara file HTML sebagai kerangka dan file CSS sebagai editor.

Kekurangan:
- Membutuhkan waktu yang relatif lebih lama untuk merender dan melakukan load pada halaman web dibandingkan 2 metode penggunaan CSS sebelumnya, dikarenakan cakupan editorial yang lebih luas.

## Tag HTML5
- `<header>`--> digunakan untuk membuat section header
- `<footer>`--> digunakan untuk membuat section footer
- `<nav>`--> digunakan untuk membuat navigator
- `<article>` --> digunakan untuk mendefinisikan artikel
-  `<audio>`--> digunakan untuk memasukkan file audio 
- `<canvas>`--> digunakan sebagai wadah untuk menggambar objek (melalui scripting)

- `<dialog>`--> digunakan untuk mendefinisikan dialog-box
- `<embed>`--> digunakan untuk memasukkan file eksternal (video, audio, dll.)
## Tipe CSS Selector
Element selector

Selector tipe ini memanfaatkan nama dari pre-defined elemen dari HTML sebagai penunjuk bagi elemen yang ingin diedit. Format yang digunakan ialah :
```
namaElemen{
   //properti CSS 
} 
```

Class selector
Class selector akan memanfaatkan nama class untuk memperoleh elemen yang akan diedit. Format yang digunakan ialah:
```
.namaClass{
    //properti CSS
}
```

ID selector
ID selector memanfaatkan ID untuk memilih elemen yang akan diedit. Format yang digunakan ialah:

```
#idElemen{
    //properti CSS
}

```

Universal selector

Selector ini akan memilih seluruh elemen untuk diedit. Format yang digunakan :
```
*{
    //properti CSS
}
```

Kita juga dapat mengkombinasikan beberapa selector untuk memilih elemen-elemen yang ingin diedit dengan menggunakan tanda koma (,) antara satu selector dengan selector lainnya.

## Langkah Implementasi
Kustomisasi dilakukan dengan memanfaatkan framework CSS yaitu Bootstrap. Terdapat berbagai pre-defined elements yang dapat digunakan melalui framework tersebut. Elemen card dapat diperoleh melalui tautan https://getbootstrap.com/docs/4.0/components/card/. Jika kita ingin membuatnya secara manual, kita dapat mendefinisikan terlebih dahulu elemen div. Elemen tersebut perlu didefinisikan untuk memiliki atribut class="card". Di antara opening dan closing tag div tersebut, kita dapat mendefinisikan elemen-elemen pendukung seperti gambar, text, dan berbagai hal lainnya. Elemen-elemen tersebut dapat dikustomisasikan lebih lanjut dengan memasukkan properti CSS.

Dengan menggunakan bootstrap, responsiveness sudah terjadi secara automatis. Namun jika kita ingin mendefinisikan responsiveness secara lebih spesifik, media query dapat digunakan. Format dari query tersebut ialah sebagai berikut:

```
@media (condition){
    //edit elements 
}
```