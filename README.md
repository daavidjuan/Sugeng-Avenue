# Pengimplementasian Checklist

 '*' Pertama, saya membuat sebuah direktori baru pada laptop saya, menginisiasi git dengan `git init`, dan mengkonfigurasi hal-hal yang diperlukan, seperti username dan email serta autentikasi.
 '*' Setelah itu, saya menginisiasi repositori di GitHub dan membuat file README.md sebagai commit pertama.
 '*' Setelah melakukan kedua langkah di atas, saya membuat branch utama baru terlebih dahulu `git branch -M main` dan menghubungkan repositori lokal dengan repositori di GitHub dengan `git remote add origin https://github.com/daavidjuan/Sugeng-Avenue.git`, kemudian saya melakukan push pada branch utama tersebut.
 '*' Saya memutuskan untuk melakukan cloning pada repositori ini ke komputer lokal, sehingga saya menjalankan perintah `git clone` di direktori berbeda dari yang sedang dikerjakan.
 '*' Setelah semua langkah di atas dilakukan, saya membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan `env\Scripts\activate`.
 '*' Di dalam direktori utama, saya membuat sebuah file bernama 'requirements.txt' dan mengisi file tersebut dengan sebuah dependencies yaitu
 '''bash
  django
  gunicorn
  whitenoise
  psycopg2-binary
  requests
  urllib3
 '''
 '*' Instalasi dependencies dilakukan dengan menjalankan perintah `pip install -r requirements.txt`. Setelah itu, saya membuat sebuah project Django baru bernama 'Sugeng_Avenue' dengan perintah `django-admin startproject Sugeng_Avenue .`.
 '*' Kemudian, saya menambahkan string "localhost, "127.0.0.1" pada ALLOWED_HOST di settings.py dan menonaktifkan virtual environment dengan perintah `deactivate`
