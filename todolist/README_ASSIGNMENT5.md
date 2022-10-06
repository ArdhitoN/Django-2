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




