## Perbedaan antara asynchronous programming dengan synchronous programming.

- Synchronous programming bersifat single-thread dan dijalankan secara sekuensial, sedangkan asynchronous bersifat multi-thread dan tidak bergantung pada urutan (dapat berjalan secara paralel).
- Terdapat sistem blocking di dalam synchronous programming, dimana request akan dikirim ke server sekali dan kemudian hasilnya akan ditunggu. Sementara itu, asynchronous programming bekerja tanpa adanya blocking, dimana banyak request ke server dapat dilakukan di satu waktu yang sama.
- Karena kedua hal di atas, hasil kerja yang dihasilkan asynchronous programming akan lebih besar dan cepat dibandingkan synchronous programming.

## Paradigma Event-Driven Programming dan Contoh Penerapannya
Event-driven programming merupakan suatu paradigma pemrograman dimana suatu prosedur suatu algoritma pemrograman dijalankan jika terdapat suatu event/kejadian tertentu. Terdapat beragam event-triggerer, seperti mouseclick, keyboard-press, dan lain sebagainya. Setiap event dapat kita korelasikan dengan sebuah handler. Contoh penerapannya ialah saat user ingin menambahkan task, dimana jika mereka menekan tombol Add Task, maka suatu modal tempat mereka mengisi data to-do baru akan muncul. Selain itu, jika user menekan tombol delete pada suatu task, maka task tersebut akan langsung terhapus.

## Penerapan asynchronous programming pada AJAX.
Agar data yang ingin ditampilkan dapat muncul secara langsung tanpa mereload halaman, asynchronous programming dapat diterapkan, salah satunya dengan menggunakan AJAX (Asynchronous JavaScript and XML). Di saat terdapat suatu event tertentu, XMLHHttpRequest akan dibuat oleh JavaScript. Kemudian, XMLHttpRequest akan mengirimkan HTTPrequest ke server, dimana server akan memrposes HTTPrequest tersebut dan hasilnya akan diserahkan kembali ke browser untuk diproses dengan JavaScript. Pada aplikasi todolist ini, AJAX diterapkan saat user melakukan load pada halaman web, menambahkan task baru, dan menghapus suatu task tertentu. 

## Langkah Implementasi
- Membuat views yang mengembalikan data dalam bentuk json, views untuk menambah data dengan memanfaatkan forms, dan views untuk menghapus task tertentu. Kemudian, masing-masing views dibuat pemetaannya di urls.py
- Untuk membuat modal, kita dapat menggunakannya dengan mengimpor salah satu modal yang terdapat pada situs dokumentasi Bootstrap. Di dalam modal tersebut, kita dapat mengaplikasikan form untuk mengambil input dari user, dimana hasil submit dari input tersebut akan dapat langsung direalisasikan tanpa load ulang seluruh halaman web dengan menggunakan AJAX.
- Untuk melakukan AJAX GET dan AJAX POST, kita dapat memanfaatkan keyword fetch, await, dan async yang berasal dari JavaScript. Selain itu, integrasi antara suatu elemen html tertentu (misalnya button) dengan suatu fungsi tertentu pada tag script dapat dilakukan. Dalam aplikasi ini, salah satu contohnya ialah pada button Add seperti berikut:
```
<button type="button" id="addbtn" class="btn btn-primary" onclick="addTodo()">Add</button>
```
Berikut merupakan fungsi addTodo yang akan dijalankan ketika button tersebut diklik:

```
  function addTodo() {
    console.log("TES")
    fetch("{% url 'todolist:add_task' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#form'))
      }).then(refreshTodolist)
    return false
  }
```
- AJAX GET dilakukan dengan fungsi berikut :
```
  async function getTodo() {
    return fetch("{% url 'todolist:show_json' %}").then((res) => res.json())
  }
```
  fungsi show_json akan mengembalikan data terkait entitas todolist dalam bentuk JSON.

- Untuk merefresh halaman web, fungsi berikut akan dipanggil:
```
async function refreshTodolist() {
      
        const todo = await getTodo();
        console.log("TESSSSSSSS" + " " + todo + " aa");
        let htmlString = ''
        todo.forEach((item) => {
          htmlString += `\n
          <div class="flex-container justify-content-center align-self-center d-flex h-100""">
            <div class="card" style="width: 18rem;">
              <img src="https://tse1.mm.bing.net/th?id=OIP.lR17CZXTy9_eI8zq4t6fUAHaEK&pid=Api&P=0" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">${item.fields.title}</h5>
                <p class="card-title">${item.fields.description}</h5>
              </div>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">Tanggal pembuatan: ${item.fields.date}</li>
                <li class="list-group-item"> Status: ${item.fields.is_finished ? "Finished" : "Unfinished"} </li>
              </ul>
              <div class="card-body">
                <a href="set-status/${item.pk}" class="card-link">Ubah</a>
                <button type="button" id="button-delete" class="btn btn-primary" onclick="deleteTodo(${item.pk})">Delete</button>
              </div>
            </div>
          </div>
          ` 
        })
        document.getElementById("content").innerHTML = htmlString
  
```

- Untuk menghapus suatu todo secara asinkronus, fungsi berikut akan dipanggil:

```
  function deleteTodo(todoPK) {
    console.log("TESzzz")
    fetch(`/todolist/delete/${todoPK}`, {
      method: "GET",
      }
      ).then(refreshTodolist)
    return false
  }
```
Catatan : Fetch digunakan untuk memanggil suatu views tertentu dengan mendefinisikan path dari views tersebut.