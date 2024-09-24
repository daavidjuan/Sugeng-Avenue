Nama  : David Juan Ananda
NPM   : 2306221913
Kelas : B

Link Deployment PWS : http://david-juan-sugengavenue.pbp.cs.ui.ac.id


<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 2 PBP</b></span>
</summary>

## Pengimplementasian Checklist

 - Pertama, saya membuat sebuah direktori baru pada laptop saya, menginisiasi git dengan `git init`, dan mengkonfigurasi hal-hal yang diperlukan, seperti username dan email serta autentikasi.
 - Setelah itu, saya menginisiasi repositori di GitHub dan membuat file README.md sebagai commit pertama.
 - Setelah melakukan kedua langkah di atas, saya membuat branch utama baru terlebih dahulu `git branch -M main` dan menghubungkan repositori lokal dengan repositori di GitHub dengan `git remote add origin https://github.com/daavidjuan/Sugeng-Avenue.git`, kemudian saya melakukan push pada branch utama tersebut.
 - Saya memutuskan untuk melakukan cloning pada repositori ini ke komputer lokal, sehingga saya menjalankan perintah `git clone` di direktori berbeda dari yang sedang dikerjakan.
 - Setelah semua langkah di atas dilakukan, saya membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan `env\Scripts\activate`.
 - Di dalam direktori utama, saya membuat sebuah file bernama 'requirements.txt' dan mengisi file tersebut dengan sebuah dependencies yaitu
 '''
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
 '''
- Instalasi dependencies dilakukan dengan menjalankan perintah `pip install -r requirements.txt`. Setelah itu, saya membuat sebuah project Django baru bernama 'Sugeng_Avenue' dengan perintah `django-admin startproject Sugeng_Avenue .`.
- Kemudian, saya menambahkan string "localhost, "127.0.0.1" pada ALLOWED_HOST di settings.py dan menonaktifkan virtual environment dengan perintah `deactivate`
- Setelah itu, saya menambahkan berkas `.gitignore` yang berisikan konfigurasi yang digunakan dalam repositori Git untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git. Kemudian saya melakukan `add, commit, dan push`.
  
  ### Membuat Aplikasi Django
  - Pertama, saya mengaktifkan virtual environment dengan perintah `env\Scripts\activate`. Setelah itu saya menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru bernama main.
  - Setelah itu, saya mendaftarkan aplikasi main ke dalam project dengan menambahkan string 'main' pada file `settings.py` di dalam direktori project 'Sugeng-Avenue'.
  - Kemudian, saya membuat direktori baru bernama 'templates' di dalam direktori aplikasi main dan di dalamnya saya membuat file bernama `main.html` yang berisi `name, price, dan description`.
  - Setelah selesai membuat templates, saya melanjutkan dengan membuat models. Models dibuat dengan mengisi berkas `models.py` dengan atribut name, price, dan description dengan tipe data sesuai apa yang diperlukan.
  - Kemudian, saya melakukan migrasi model dengan perintah `python manage.py makemigrations` kemudian menerapkan migrasi ke dalam basis data lokal dengan `python manage.py migrate`.
 
  ### Mengintegrasikan Komponen MVT
  - Pengintegrasian dilakukan dengan menambahkan `from django.shortcuts import render` pada file `views.py`. Kemudian dalam file tersebut ditambahkan fungsi `show_main` yang berisikan komponen yang diperlukan dalam models, yaitu `name, price, dan description` dari product.
  - Dalam `views.py`, terdapat perintah `return render(request, "main.html", context)` yang menghubungkan views dengan template HTML, function show_main menerima parameter request yang akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
  - Kemudian, saya memodifikasi file `main.html` pada `templates` kemudian mengubah isinya dengan {{ name }}, {{ price }}, {{ description }}.
  - Kemudian saya membuat urls.py pada direktori aplikasi main untuk memetakan function pada views.py, dalam urls.py terdapat function path yang menerima parameter ' ' agar halaman aplikasi tersebut muncul pada halaman utama localpath.
  - Kemudian saya mengisi file test.py untuk melakukan unit testing. Setelah itu menjalankan perintah `python manage.py test`
 ### Deployment PWS
 - Karena sudah memiliki akun, saya membuat sebuah project baru bernama Sugeng-Avenue. Kemudian mengganti kode pada settings.py di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada ALLOWED_HOSTS.
 - Kode yang diubah menjadi `ALLOWED_HOSTS = ["localhost", "127.0.0.1", "david-juan-sugengavenue.pbp.cs.ui.ac.id"]`. Kemudian saya melakukan `add, commit, dan push`.
 - Setelah itu, saya mengubah nama branch utama menjadi main dengan `git branch -M main`. Kemudian melakukan `push` ke PWS dengan `git push pws main:master`.

## BAGAN
![image](https://github.com/user-attachments/assets/b6df3c23-49a1-4726-b22f-3e8edaacbc4c)

## Fungsi Git dalam pengembangan perangkat lunak
Git memungkinkan para penggunanya untuk dapat bekerja secara kolaboratif atau bekerja sama bersama kelompok, melacak setiap perubahan yang dibuat, dan mengelola perubahan yang terjadi pada kode dari waktu ke waktu. Git memiliki fitur dimana memungkinkan pemilik kode untuk membuat branch untuk mengerjakan fitur atau perbaikan secara terpisah dari branch utama, meminimalisir terjadinya error pada branch utama. 

## Pemilihan Framework Django sebagai permulaan
Sebagai permulaan, penggunaan bahasa python sangat memudahkan para penggunanya karena bahasa python jauh lebih mudah untuk dikenal bagi para pemula. Sebagai mahasiswa yang baru menjalankan 1 tahun perkuliahan di Fasilkom, saya merasa tidak terlalu kesulitan ketika menulis kode dengan bahasa python. Kemudian, Django juga memiliki tutorial dan sumber daya yang banyak untuk mendukung pembelajaran. Django telah digunakan untuk membangun berbagai macam aplikasi web, menunjukkan bahwa Django adalah framework yang dapat diandalkan untuk sebuah project.

## Alasan model Django disebut sebagai ORM
Model Django adalah sebuah representasi objek dari data yang akan disimpan ke dalam database. Sebagai contoh, dalam model saya di atas, terdapat atribut name, price, dan description, Django akan membuat tabel model tersebut dengan kolom name, price, dan description. Selain itu, ORM Django terintegrasi secara erat dengan framework Django lainnya, sehingga memudahkan para pengguna juga untuk memabangun sebuah aplikasi web. ORM pada Django memungkinkan pengembangan aplikasi berbasis data menjadi lebih sederhana, cepat, dan mudah dipahami oleh para penggunanya.
</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 3 PBP</b></span>
</summary>

## Data Delivery dalam pengimplementasian sebuah platform
Dalam sebuah platform, data delivery memungkinkan untuk memberikan kita beberapa kemudahan. Dengan adanya sistem data delivery yang efisien, kita bisa memastikan bahwa pengguna menerima data yang relevan dengan kebutuhan mereka, tanpa hambatan, kapan pun dan di mana pun mereka berada. Hal ini pada gilirannya meningkatkan performa platform secara keseluruhan. Beberapa aspek utama yang dipengaruhi oleh efektivitas data delivery meliputi skalabilitas, di mana platform mampu menangani volume data yang terus meningkat seiring dengan pertumbuhan jumlah pengguna dan interaksi keamanan data, yang menjamin bahwa data sensitif terlindungi dari akses yang tidak sah atau manipulasi selama proses pengiriman; serta user experience, yang secara langsung berkaitan dengan kecepatan dan efisiensi data yang diterima pengguna, sehingga menciptakan interaksi yang lebih responsif dan memuaskan.

## XML or JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik daripada XML karena lebih familiar bagi orang-orang. Namun, tetap antara JSON dan XML memiliki kelebihannya masing-masing. JSON memiliki sintaks yang lebih sederhana dan ringkas, sehingga membuatnya lebih mudah dibaca oleh manusia maupun mesin. JSON memiliki ukuran data yang relatif lebih ringan dan hal ini membuat transmisi data semakin cepat. 

## Fungsi dari Method `is_valid()` dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` adalah untuk memvalidasi fields yang terdapat pada forms atau dengan kata lain memastikan jawaban yang dimasukkan ke dalam form sudah benar. Dengan method ini, kita dapat memeriksa fields apakah sudah terisi dengan benar atau belum sehingga data yang masuk difilter dan masuk ke dalam database. 

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` digunakan untuk melindungi dari penyerangan di mana penyerang menjalankan aksi yang tidak diinginkan tanpa sepengetahuan pengguna. `csrf_token` akan memverifikasi setiap tindakan yang dilakukan benar-benar dilakukan oleh pengguna yang seharusnya dan bukan dari sumber eksternal. Jika tidak menambahkan `csrf_token` pada form Django, kemungkinan yang akan terjadi adalah penyerang mendapatkan celah untuk melakukan hal yang tidak diinginkan seperti di atas. Request dari penyerang akan tetap dijalankan karena tidak ada token yang dapat digunakan untuk memverifikasi request dari pengguna.

## Pengimplementasian Checklist
  - Pertama, saya membuat `base.html` sebagai template untuk template html lainnya, kemudian mengedit `TEMPLATES` yang terdapat di `settings.py` agar `base.html` dapat terdeteksi sebagai file template.
  - Setelah itu, saya mengubah kode pada berkas pada `main.html` sehingga menggunakan `base.html` sebagai template utamanya. 
  - Kemudian, saya membuat sebuah file bernama `forms.py` untuk membuat suatu struktur form. Tidak lupa, saya mengimport form tersebut pada file `views.py`.
  - Membuat function `create_product_entry` pada `views.py` untuk menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form.
  - Kemudian, mengubah fungsi `show_main` pada `views.py` supaya dapat diakses pada `main.html`.
  - Membuat file html baru dengan nama `create_product_entry.html` pada `main/templates` dan mengisinya dengan:
    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Mood Entry</h1>

    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td>
            <input type="submit" value="Add Mood Entry" />
          </td>
        </tr>
      </table>
    </form>

    {% endblock %}
    ```
  - Membuat function `show_json` dan `show_xml` pada `views.py` dan menambahkan pada file `urls.py`.
    - `show_json`
      ```
      def show_json(request):
      data = ProductEntry.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```
    - `show_xml`
      ```
      def show_xml(request):
      data = ProductEntry.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```
  - Mengimport kedua function tersebut pada `urls.py` dan membuat url untuk kedua fungsi tersebut agar dapat diakses sesuai url-nya masing-masing.
  - Membuat function `show_json_by_id` dan `show_xml_by_id` pada `views.py` dan menambahkan pada file `urls.py`.
    - `show_json_by_id`
      ```
      def show_json_by_id(request, id):
      data = ProductEntry.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```
    - `show_xml_by_id`
      ```
      def show_xml_by_id(request, id):
      data = ProductEntry.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```
  - Mengimport kedua function tersebut pada `urls.py` dan membuat url untuk kedua fungsi tersebut agar dapat diakses sesuai url-nya masing-masing.

- XML
![image](https://github.com/user-attachments/assets/7cdc8593-d3ed-4a67-ab00-3c27f0b0be43)
- JSON
![image](https://github.com/user-attachments/assets/7f50acd5-29b9-4ffa-a543-5a9334779167)
- XML by id
![image](https://github.com/user-attachments/assets/7a20c6cc-cdcf-4408-afd2-8558bfff235c)
- JSON by id
![image](https://github.com/user-attachments/assets/103d785a-b5ba-4fd5-a4ff-e88df9c9b42a)

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 4 PBP</b></span>
</summary>

## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

## Cara kerja penghubungan model `Product` dengan `User`

## Perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

## Pengimplementasian Checklist