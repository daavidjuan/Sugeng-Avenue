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
</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 4 PBP</b></span>
</summary>

## Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` adalah suatu kelas yang bawaan Django, digunakan untuk membuat redirect response. Kelas ini menerima URL secara eksplisit sebagai argumen. `redirect()` dirancang untuk menyederhanakan redirect yang dilakukan. `redirect()` dapat menerima view atau model.

## Cara kerja penghubungan model `Product` dengan `User`
- Menambahkan `ForeignKey` ke dalam model untuk menghubungkan model Product dengan User. Dengan menambahkan `ForeignKey`, setiap produk terkait dengan satu pengguna, dan satu pengguna dapat memiliki banyak produk. Selain itu, saya menggunakan `on_delete=models.CASCADE`, yang artinya jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

- Untuk menetapkan pengguna yang membuat entri produk baru, field `user` di model Product akan diisi dengan pengguna yang sedang login. Hal ini dilakukan dengan memodifikasi fungsi `create_product_entry`, di mana pengguna yang sedang login dapat membuat entri produk baru melalui form. Penggunaan `commit=False` memungkinkan kita menambahkan informasi pengguna terlebih dahulu sebelum menyimpan objek ke dalam database, sehingga objek dapat dimodidifikasi sebelum proses penyimpanan.

- Pada fungsi `show_main`,  menambahkan kode `product_entries = Product.objects.filter(user=request.user)`, yang berfungsi untuk menampilkan semua entri produk yang terkait dengan pengguna yang sedang login.

## Perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Autentikasi adalah proses untuk memverifikasi identitas user yang berusaha untuk login. Proses ini benar-benar menentukan user yang sah untuk dapat mengakses program tersebut. Hal yang dilakukan saat pengguna login adalah memeriksa apakah username dan password sesuai dengan yang ada di database, kemudian jika sudah terauntentikasi user tersebut akan diberikan akses untuk melanjutkan ke sistem, kemudian informasi login akan disimpan dalam session.
Django memiliki fungsi seperti authenticate() dan login() untuk memverifikasi kredensial dan memulai session pengguna.
- Otorisasi adalah proses untuk menentukan apakah seoarang user yang sudah terauntentikasi memiliki izin atau hak untuk mengakses program. Setelah pengguna login (terautentikasi), Django akan memeriksa apakah pengguna tersebut memiliki izin yang diperlukan untuk mengakses halaman atau fungsi tertentu. Misalnya, hanya pengguna dengan peran admin yang dapat mengakses panel admin. 

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan Session ID, yang disimpan dalam bentuk cookie di browser pengguna. Setiap kali pengguna mengirimkan request baru ke server, cookie yang berisi Session ID akan dikirim bersama request HTTP tersebut. Django kemudian memeriksa cookie tersebut untuk mendapatkan Session ID dan mencocokkannya dengan data session yang tersimpan di server. Jika Session ID valid dan sesuai dengan data di server, Django akan mengenali bahwa pengguna tersebut masih dalam keadaan terautentikasi dan login. Untuk menjaga keamanan, cookie sebaiknya diberi flag HttpOnly dan secure. Hal ini mencegah cookie diakses oleh skrip berbahaya dan memastikan cookie hanya dikirim melalui koneksi yang aman. Dengan mengikuti praktik terbaik, penggunaan cookie secara default bisa menjadi lebih aman bagi developer.


## Pengimplementasian Checklist
- Sebelum membuat fungsi login dan logout, diperlukan adanya fungsi untuk registrasi. Dimulai dengan import `UserCreationForm` dan `messages` pada `views.py` dan menambahkan fungsi `register` yang berisi : 
  ```
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
  ```
  Tidak lupa dengan membuat sebuah file html baru bernama `register.html` pada `main/templates`. Fungsi login dilakukan dengan import `authenticate`, `login`, dan `AuthenticationForm` pada `views.py`. Setelah itu menambahkan fungsi `login_user` berisi :
  ```
  def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
              user = form.get_user()
              login(request, user)
              return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
  ```
  Kemudian membuat `login.html` pada `main/templates`. Fungsi logout dilakukan dengan import `logout` pada `views.py`. Setelah itu menambahkan `logout_user` pada `views.py`. Kemudian menambahkan button logout pada file `main.html`.

- Untuk menghubungkan model `Product` dengan `User`, import `User` pada `models.py`. Kemudian menambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model `ProductEntry`. Setelah itu pada fungsi `create_product_entry`, menambahkan `product_entry` untuk menerima parameter `commit=False` dan mengganti `product_entry.user` menjadi `request.user`. Begitu juga pada `show_main`. Terakhir, pada `settings.py`, menambahkan import os dan mengubah variabel DEBUG pada `settings.py` dengan :
  ```
  PRODUCTION = os.getenv("PRODUCTION", False)
  DEBUG = not PRODUCTION  
  ```

- Untuk menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi, pertama-tama menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py`. Kemudian memodifikasi kode pada `login_user` menjadi :
  ```
  if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
  ```
  Setelah itu, menambahkan `'last_login': request.COOKIES['last_login']` pada fungsi `show_main` pada variabel `context`. Setelah itu mengganti `logout_user` menjadi :
  ```
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
  Kemudian, menambahkan text sesi terakhir login pada `main.html`.


</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 5 PBP</b></span>
</summary>

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Terdapat istilah CSS specificity yang digunakan untuk menentukan prioritas penerapan aturan styling. CSS specificity dapat dihitung melalui selector dan menggunakan sistem bilangan desimal. Berikut adalah urutan prioritas CSS selector dari yang tertinggi hingga terendah:

- Aturan !important: Aturan ini mengesampingkan semua gaya lainnya, termasuk inline styles.
- Inline Styles: Gaya yang diterapkan langsung pada elemen HTML melalui atribut style memiliki prioritas lebih tinggi dibandingkan semua selector CSS lainnya.
- ID Selector (#): Selector ini diterapkan pada elemen yang memiliki atribut id.
- Pseudo-Class Selector (:): Selector ini digunakan pada elemen dalam kondisi tertentu, seperti `:hover`, `:focus`, atau `:nth-child()`.
- Attribute Selector ([]): Selector ini digunakan untuk elemen berdasarkan atributnya, seperti `[type="text"]` atau `[href]`.
- Class Selector (.): Selector ini diaplikasikan pada elemen yang memiliki atribut class dan memiliki prioritas lebih tinggi daripada selector elemen.
- Element Type Selector: Selector ini mengacu pada elemen HTML seperti `<div>`, `<p>`, atau `<h1>`.
- Universal Selector (*): Selector ini memiliki prioritas terendah dan berlaku untuk semua elemen.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Pengalaman User yang Lebih Baik: design responsif memastikan website tampil dan berfungsi dengan optimal di berbagai perangkat, mulai dari desktop hingga smartphone, sehingga memberikan pengalaman yang konsisten dan nyaman bagi user.

Peningkatan Traffic Seluler: Dengan semakin banyaknya user yang mengakses web melalui perangkat seluler, memiliki situs yang ramah seluler menjadi sangat penting. design responsif membantu menarik dan mempertahankan pengunjung dari kalangan ini.

SEO yang Lebih Optimal: Mesin pencari seperti Google memberikan prioritas lebih tinggi kepada situs yang dioptimalkan untuk seluler. Dengan design responsif, visibilitas dan peringkat situs di mesin pencari dapat meningkat secara signifikan.

Efisiensi Biaya: Daripada membuat situs terpisah untuk perangkat yang berbeda, design responsif memungkinkan Anda mengelola satu situs yang dapat menyesuaikan dengan berbagai ukuran layar, sehingga menghemat waktu dan biaya pengembangan.

Kesiapan Masa Depan: Seiring dengan munculnya perangkat baru dengan ukuran dan resolusi layar yang bervariasi, design responsif memastikan situs Anda tetap dapat diakses dan berfungsi dengan baik di perangkat-perangkat tersebut.

Contoh aplikasi yang sudah menggunakan design responsif:
- Google
- YouTube
Contoh aplikasi yang belum menggunakan design responsif:
- SiakNG

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah jarak antara elemen dan elemen lain di luar kotak elemen tersebut. Margin menciptakan ruang di luar batas elemen. Margin dapat diatur dengan properti margin, yang bisa diterapkan ke semua sisi atau sisi tertentu (atas, kanan, bawah, kiri). 
  '''
  div {
  margin-top: 10px;
  margin-right: 15px;
  margin-bottom: 20px;
  margin-left: 25px;
  }
  '''

Border adalah garis yang mengelilingi elemen. Border berada di antara margin dan padding, membungkus elemen serta padding-nya. Border dapat diatur menggunakan properti border yang mencakup lebar, gaya, dan warna, atau properti spesifik seperti border-width, border-style, dan border-color.
  '''
  div {
  border-top: 3px dashed red;
  border-right: 4px dotted blue;
  border-bottom: 5px double green;
  border-left: 6px solid orange;
  }
  '''

Padding adalah jarak antara konten elemen dan batas dalam (border) elemen tersebut. Padding menciptakan ruang di dalam elemen, di sekitar konten elemen. Padding bisa diatur dengan properti padding, baik untuk semua sisi atau secara spesifik untuk tiap sisi.
  '''
  div {
  padding-top: 5px;
  padding-right: 10px;
  padding-bottom: 15px;
  padding-left: 20px;
  }
  '''

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
CSS Flexbox adalah sistem tata letak satu dimensi yang digunakan untuk mendistribusikan dan menyelaraskan ruang antara item dalam suatu container. Flexbox sangat berguna untuk menciptakan tata letak responsif yang menyesuaikan dengan berbagai ukuran layar dan perangkat, tanpa perlu banyak menggunakan properti seperti `float` dan `position` dalam kode CSS. Flexbox memudahkan pengaturan tata letak horizontal atau vertikal elemen-elemen di dalam container.

Di sisi lain, CSS Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen dalam bentuk baris dan kolom. Grid Layout ideal untuk membuat tata letak yang lebih kompleks dan terstruktur, memudahkan pengelolaan elemen-elemen di halaman web secara fleksibel dan terorganisir, baik secara horizontal maupun vertikal.

## Implementasi Checklist
- Pertama, saya mengintegrasikan Tailwind CSS ke aplikasi dengan memodifikasi file base.html, menambahkan tag `<meta name="viewport">` dan menyertakan `<script src="https://cdn.tailwindcss.com">`. Setelah itu, saya mengimplementasikan fitur Edit Product dengan memodifikasi `views.py`, membuat fungsi baru bernama `edit_product` yang menerima parameter `request` dan `id`. Saya juga menambahkan import `reverse` dan `HttpResponseRedirect`.
- Selanjutnya, saya membuat file HTML baru bernama `edit_product.html`, yang memungkinkan pengeditan input dari form yang sudah ada, dengan tampilan yang sama seperti di `create_product_entry.html`. Saya kemudian memperbarui `urls.py` untuk menambahkan path baru untuk fitur edit.
- Setelah itu, saya mengimplementasikan fitur delete product dengan menambahkan fungsi baru di `views.py`, mengikuti tutorial, dan menambahkan path URL baru untuk fitur tersebut.
- Kemudian, saya membuat navigation bar dengan menambahkan file `navbar.html` yang berisi desain dengan background putih eperti "Home" dan "About", juga menampilkan pesan selamat datang dengan {{nama}}, serta tombol logout. Untuk saat ini, navbar masih bersifat dummy kecuali tombol logout. Saya juga menambahkan logo_sugengavenue.png di bagian navbar.
- Setelah membuat navbar, fitur edit, dan delete product, saya mengonfigurasi static files dalam aplikasi dengan memodifikasi `settings.py`, menambahkan `'whitenoise.middleware.WhiteNoiseMiddleware'` ke bagian `MIDDLEWARE`, serta mengatur `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL`.
- Saya juga menambahkan file `global.css` di folder `static/css`, berisi desain custom saya. Kemudian, saya memodifikasi `base.html` agar `global.css` bisa digunakan di seluruh template Django.
- Selanjutnya, saya menata ulang `login.html`, `register.html`, dan `create_product_entry.html` menggunakan styling dari Tailwind. Untuk `login.html`, saya menambahkan gambar statis bernama logo_sugengavenue.png, yang ditampilkan di sebelah form login. Selain itu, saya juga menambahkan logo_sugengavenue.png di `main.html`.
- Saya juga membuat file `card_mood.html`, yang berfungsi untuk menampilkan card baru setiap kali ada entri produk baru, lengkap dengan tombol untuk edit dan delete product. Selain itu, saya menambahkan sandal-jepit.png di setiap produk yang ditambahkan.
- Setelah menyelesaikan semua file HTML di folder template, saya memodifikasi `main.html` agar seluruh file HTML lain terintegrasi dengan baik.

</details>

<details>
<summary>
  <span style="font-size:16px;"><b>Tugas 6 PBP</b></span>
</summary>

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript adalah bahasa pemrograman tingkat tinggi yang bersifat cross-platform dan mendukung berbagai paradigma. Dalam pengembangan aplikasi web, JavaScript sangat populer karena memungkinkan perubahan halaman web secara dinamis dan meningkatkan interaksi antara halaman dan user. Beberapa manfaat utama JavaScript meliputi:
- Interaktivitas: JavaScript memungkinkan pengembang menambahkan elemen interaktif, seperti validasi form, manipulasi DOM, dan animasi, yang membuat halaman web terasa lebih hidup dan dinamis.
- Pemrosesan Asinkron: Dengan memanfaatkan AJAX atau Fetch API, JavaScript dapat mengambil atau mengirim data ke server tanpa harus memuat ulang seluruh halaman, memberikan pengalaman yang lebih cepat.
- Pengalaman User yang Lebih Baik: JavaScript membantu meningkatkan kecepatan respons halaman, memungkinkan proses berjalan secara real-time, dan memperbarui konten tertentu tanpa mengganggu aktivitas user pada halaman tersebut.

## Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()!` Apa yang akan terjadi jika kita tidak menggunakan `await`?
`await` digunakan untuk menunggu penyelesaian dari sebuah promise. Dalam konteks `fetch()`, `await` digunakan untuk menunggu respons dari permintaan HTTP yang dikirim ke server. Tanpa `await`, JavaScript akan melanjutkan eksekusi kode berikutnya tanpa menunggu respons dari `fetch()`, yang dapat menyebabkan masalah jika ada kode yang bergantung pada hasil respons tersebut. 

Jika `await` tidak digunakan, kode setelah `fetch()` akan dijalankan sebelum permintaan selesai, sehingga variabel yang seharusnya berisi data dari respons mungkin belum terisi dengan benar. Hal ini dapat menyebabkan perilaku yang tidak diinginkan karena proses `fetch()` belum selesai.

## Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
Decorator `csrf_exempt` digunakan untuk menonaktifkan pemeriksaan CSRF token pada view tertentu yang menerima permintaan `POST` dari AJAX. Secara default, Django mengharuskan setiap `POST` request disertai CSRF token sebagai langkah pengamanan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yang memungkinkan penyerang mengirimkan permintaan atas nama pengguna yang sah. Namun, dalam beberapa kasus, seperti ketika menggunakan AJAX `POST`, CSRF token mungkin tidak disertakan secara otomatis.

Oleh karena itu, pada view seperti `add_product_entry_ajax` di `main/views.py`, decorator `csrf_exempt` digunakan untuk menonaktifkan pengecekan CSRF, sehingga permintaan `POST` dari AJAX tetap dapat diproses. Namun, menonaktifkan CSRF harus dilakukan dengan sangat hati-hati. Jika tidak, hal ini dapat membuka celah keamanan dan membuat aplikasi rentan terhadap serangan. Oleh sebab itu, sangat penting untuk memastikan ada langkah-langkah pengamanan lain yang diterapkan ketika CSRF dinonaktifkan, seperti membatasi akses hanya ke pengguna atau aplikasi yang tepercaya.

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Validasi dan pembersihan data di frontend (JavaScript) bisa dilewati atau dimanipulasi oleh pengguna, misalnya dengan menggunakan developer tools. Oleh karena itu, membersihkan data hanya di frontend tidak cukup aman. Di backend, pembersihan data memastikan bahwa data yang diterima server benar-benar aman, melindungi dari ancaman seperti SQL Injection dan XSS. Selain itu, pengembang memiliki kontrol penuh di backend terkait bagaimana data diproses dan divalidasi, sehingga tidak bergantung pada kondisi di frontend atau browser pengguna. Karena validasi dan sanitasi di frontend bisa diabaikan oleh pengguna, misalnya dengan menonaktifkan JavaScript, backend menjadi lapisan terakhir yang memastikan semua data sudah aman dan valid. Backend juga berperan dalam memastikan bahwa data yang diterima sesuai dengan aturan yang ditetapkan, seperti tipe data, format, atau nilai yang benar, sehingga menjaga konsistensi dan akurasi.

## Pengimplementasian Checklist
Pertama, saya membuat suatu function `add_product_entry_ajax` untuk menambahkan suatu product baru ke basis data AJAX.
  ```
  @csrf_exempt
  @require_POST
  def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    rating = request.POST.get("rating")
    user = request.user

    new_product = ProductEntry(
        name=name, price=price, 
        description=description,
        rating=rating,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
  ```
Setelah itu, saya melakukan routing dengan mengimport fungsi tersebut ke `urls.py` dan menambahkan path url ke dalam `urlpatterns` agar dapat mengakses fungsi tersebut. Untuk menampilkan data produk secara dinamis menggunakan `fetch()` API, saya melakukan beberapa perubahan pada kode. Ssaya menghapus `product_entries = Product.objects.filter(user=request.user)` serta `'product_entries': product_entries` dari `main/views.py`. Lalu, saya memodifikasi baris pertama pada fungsi show_json dan show_xml dengan mengganti menjadi `data = ChocolateProduct.objects.filter(user=request.user)` untuk hanya menampilkan produk yang dimiliki oleh pengguna yang sedang login.

Di `template main/templates/main.html`, saya menghapus blok kondisional yang sebelumnya digunakan untuk menampilkan produk secara statis dan menggantinya dengan `<div id="product_entry_cards"></div>`. Saya membuat fungsi JavaScript bernama `getProductEntries()` yang menggunakan `fetch()` untuk mengambil data produk dalam format JSON dari URL yang hanya mengembalikan produk milik pengguna yang sedang login. Setelah itu, data produk ini akan diteruskan ke fungsi `refreshProductEntries()` yang bertugas menampilkan data tersebut dalam elemen div yang sudah disediakan.

Selain itu, saya menambahkan sebuah tombol di `main/templates/main.html` yang akan membuka modal berisi form untuk menambahkan produk baru ketika ditekan. Tombol ini memanggil fungsi JavaScript `showModal()` untuk menampilkan modal tersebut. Di dalam modal, terdapat form dengan field seperti `name`, `price`, `description`, dan `rating` yang nantinya akan dikirimkan ke server melalui AJAX `POST`.

Selanjutnya, saya membuat fungsi JavaScript `addProductEntry()` yang bertugas mengirimkan data produk baru ke server menggunakan `POST` request melalui `fetch()`. Fungsi ini mengirim permintaan POST ke URL /create-product-entry-ajax/ untuk menambahkan produk baru. Setelah produk berhasil ditambahkan, fungsi refreshProductEntries() dipanggil untuk memperbarui daftar produk tanpa perlu me-refresh halaman. Selain itu, form di dalam modal akan di-reset, dan modal akan ditutup setelah produk ditambahkan.