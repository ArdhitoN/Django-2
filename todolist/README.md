Tautan aplikasi : https://cata-log.herokuapp.com/todolist/


## Kegunaan {% csrf_token %} Pada Elemen <form>

Tujuan utama penggunaan {% csrf_token %} ialah untuk mencegah dan memproteksi project dari serangan Cross Site Request Forgery (CSRF). Serangan dilakukan dengan memanfaatkan kredensial dari dari user yang telah terautentikasi dengan mengubah request dari yang mereka lakukan sehingga pada akhirnya korban melakukan hal yang tidak mereka inginkan. Misalnya, korban dapat masuk ke suatu link tanpa keinginannya sendiri ketika melakukan suatu hal di halaman web. Elemen `{% csrf_token %}` akan membuat sebuah token di server ketika proses rendering halaman web dilakukan. Token tersebut berupa kode alfanumerik atau nilai rahasia yang bersifat acak dan bersifat khusus untuk suatu situs tertentu. Setiap request yang masuk akan dicek melalui token tersebut. Oleh karena itu juga, aktivitas POST melalui form hanya akan dapat berjalan jika domain dimana ia berasal dapat dipercaya. 

## Pembuatan Elemen <form> Secara Manual 
Elemen form dapat dibuat secara manual langsung di html, dimana terdapat pre-defined tag untuk membuatnya. 

Form dapat diinisiasikan elemen dengan opening dan closing tag `<form></form>`, dimana di dalamnya kita dapat mendefinisikan atribut action dan method yang diinginkan. 

Di dalam tag form tersebut, kita dapat membuat elemen-elemen input dengan tag `<input>` .

Tipe dari tag input tersebut dapat dimodifikasi dengan atribut type. Untuk dapat melakukan submisi terhadap form, kita dapat menginisiasikan sebuah elemen input dengan tipe submit seperti berikut:

`<input type="submit">` 

## Alur Data (Submisi - Pop-up Data di Template HTML)
Pada awalnya, user akan menginput jawaban untuk form dan melakukan submisi. Setelahnya, form tersebut akan mengirimkan hasilnya melalui method POST. Pada views.py, terdapat method create_task yang menerima parameter request, dimana request tersebut memiliki method POST sebagai atributnya. Setelah itu, user yang sedang log in akan dideteksi dengan mengakses atribut user dari request dengan `request.user`. Selain itu, form yang telah diinput oleh user akan dicek validitasnya. Jika form tersebut valid, maka hasil dari form akan disave menuju database. Kemudian jika user kembali ke halaman utama, fungsi views yang sesuai akan kembali dipanggil dan pada akhirnya data yang baru saja dibuat akan tersedia.

## Langkah Implementasi
1. Melakukan inisialiasi aplikasi melalui command `python manage.py startapp todolist` 
2. Mendaftarkan aplikasi todolist di settings.py
3. Mendaftarkan path todolist di urls.py yang berada di folder project_django dengan menambahkan `path('todolist/', include('todolist.urls'))` sebagai salah satu elemen baru di urlpatterns.
4. Menginisiasikan template todolist.html (home aplikasi), register.html(untuk halaman register), login.html(untuk halaman login), create-task.html(halaman untuk menambahkan task) di (folder todolist > folder templates)
5. Membuat model Task di models.py yang berada di folder todolist dengan atribut user, date, title, dan description dengan tipe data yang sesuai. Pada atribut user, object Task akan menampung ForeignKey User untuk menunjukkan adanya relasi antara keduanya (Eksistensi Task akan bergantung pada User). Jika User didelete, maka Task yang terhubung dengannya akan ikut terdelete dengan atribut on_delete=models.CASCADE
6. Melakukan migrasi model
7. Mendefinisikan fungsi show_todolist di views.py yang berada di folder todolist untuk memberikan hasil render todolist.html yang telah dibuat dengan data yang ada di database.
8. Untuk dapat melihat home serta membuat proses registrasi, login, create-task, dan logout, berjalan dengan baik kita perlu mendefinisikan views yang sesuai untuk masing-masing fitur tersebut.

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

9. Melakukan routing sehingga fitur-fitur yang telah dibuat dapat diakses melalui web/internet sebagai berikut : 
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

10. Melakukan 3 mantra git yaitu git add, git commit, dan git push untuk mendeploy aplikasi.
11. Membuat 2 akun dummy dengan masing-masing diisi 3 dummy-task-data dengan langsung terjun ke halaman web untuk meregestrasikan 2 user baru, melakukan login, dan menambahkan 3 task baru untuk masing-masing user dengan memanfaatkan fitur create-task.
