# TugasDockerCC

## Flask SQLite Web App in Docker
# Deskripsi Aplikasi
Aplikasi web ini adalah aplikasi manajemen pengguna sederhana yang menggunakan Flask sebagai framework dan SQLite sebagai database. Aplikasi ini menyediakan fitur login, registrasi, pengubahan password, penghapusan pengguna, serta tampilan admin untuk mengelola data pengguna.


1. Login:
Pengguna dapat login dengan username dan password.
Admin dapat melihat semua data pengguna di halaman admin.

2. Registrasi:
Pengguna baru dapat mendaftar dengan memasukkan nama, username, dan password.

3. Change Password:

Pengguna dapat mengubah password dengan memasukkan password lama dan baru.

4. Delete User:

Admin dapat menghapus pengguna dari database.

5. Logout:

Pengguna dapat logout dari aplikasi dan sesi akan dihapus.

# Dependensi yang digunakan
1. Flask
Flask adalah framework mikro untuk pengembangan aplikasi web dengan Python. Menurut sebuah studi yang diterbitkan di jurnal KESATRIA, Flask digunakan untuk membangun API yang kemudian di-deploy sebagai layanan Cloud Run di Google Cloud Platform (GCP). Penelitian ini menunjukkan bahwa Flask sangat efektif dalam memfasilitasi pembaruan data secara otomatis dan efisien, serta mudah diintegrasikan dengan layanan cloud seperti GCP.

2. SQLite3
SQLite3 adalah database relasional yang ringan dan self-contained. Dalam konteks Flask, SQLite3 sering digunakan untuk penyimpanan data lokal. Dokumentasi Flask menunjukkan bahwa SQLite3 dapat dengan mudah diintegrasikan dengan Flask untuk membuka dan menutup koneksi database sesuai permintaan, membuatnya ideal untuk aplikasi web kecil hingga menengah.

3. Pandas
Pandas adalah library Python yang kuat untuk analisis dan manipulasi data. Dalam konteks pengembangan web cloud, Pandas dapat digunakan untuk memproses dan menganalisis data yang disimpan dalam database seperti SQLite3. Penelitian menunjukkan bahwa Pandas sangat berguna untuk membersihkan, memproses, dan menganalisis data yang kemudian dapat diintegrasikan ke dalam aplikasi web untuk visualisasi dan laporan.


# Langkah Instalasi
1. Pastikan Docker Terinstal:

Windows/Mac: Unduh Docker Desktop dari sini.
Linux: Ikuti petunjuk instalasi di sini.
2. Clone Repository:
```
git clone https://github.com/username/repo.git
cd repo
```
3. Build Docker Image: Gunakan perintah ini untuk membangun image Docker:
```
docker-compose build
```
4. Jalankan Aplikasi di Container: Setelah image berhasil dibangun, jalankan container dengan:
```
docker-compose up
```
5. Akses Aplikasi: Buka browser dan akses aplikasi melalui URL:
```
http://localhost:5000
```
6. Hentikan Container: Jika Anda selesai, hentikan container dengan perintah:
```
docker-compose down
```
# Penjelasan Dockerfile
Dockerfile ini digunakan untuk membangun image Docker bagi aplikasi Flask Anda.
```
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

```
Penjelasan Perintah dalam Dockerfile:

1. FROM python:3.9-slim: Menggunakan image Python 3.9 yang ringan sebagai base image.
2. WORKDIR /app: Menentukan direktori kerja di dalam container ke /app.
3. COPY . .: Menyalin semua file dari proyek ke dalam direktori kerja container.
4. RUN pip install -r requirements.txt: Menginstal semua dependensi yang tercantum dalam file requirements.txt.
5. EXPOSE 5000: Mengekspos port 5000 agar aplikasi dapat diakses melalui port tersebut.
6. CMD ["python", "app.py"]: Menentukan perintah default untuk menjalankan aplikasi Flask ketika container dijalankan.

# Penjelasan docker-compose.yml
docker-compose.yml digunakan untuk mendefinisikan dan mengelola layanan aplikasi dalam container. Berikut adalah contoh konfigurasi docker-compose.yml yang digunakan untuk proyek ini:
```
version: '3.8'

services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
      - sqlite_data:/app/data

volumes:
  sqlite_data:

```
Penjelasan Konfigurasi:
1. version: '3.8': Menentukan versi dari Docker Compose.
2. flask-app: Mendefinisikan layanan untuk aplikasi Flask.
3. build: .: Menunjukkan direktori tempat Dockerfile berada.
4. ports: "5000:5000": Memetakan port 5000 pada host ke port 5000 di dalam container, sehingga aplikasi dapat diakses di http://localhost:5000.
5. volumes: Menyimpan file aplikasi dan data SQLite di volume untuk keamanan data.
6. volumes: Volume untuk memastikan data SQLite tidak hilang ketika container dihentikan atau di-restart.

# Struktur direktori

```
project/
│
├── app.py                 # File utama aplikasi Flask
├── Dockerfile             # Instruksi untuk membangun Docker image
├── docker-compose.yml     # Konfigurasi Docker Compose
├── requirements.txt       # Daftar dependensi aplikasi
├── data.db                # File database SQLite
├── templates/             # Template HTML untuk Flask
│   ├── login.html         # Halaman login
│   ├── register.html      # Halaman registrasi
│   └── home.html          # Halaman utama setelah login
└── README.md              # Dokumentasi proyek

```

Catatan:
1. Pastikan file data.db ada sebelum menjalankan aplikasi atau aplikasi akan membuatnya jika belum ada.
2. Anda dapat menguji aplikasi menggunakan browser atau alat seperti Postman untuk mengakses API-nya.

## Authors

- Marshaniswah Syamsul(1101210153) | [@marshaniswah](https://www.github.com/marshaniswah)
- Sadam Al Rasyid(1101210112) | [@sadam112](https://github.com/Sadam1122)
- M. Rafi Mahfuz(1101213355) |[@lionman9097](https://github.com/lionman9097)
- Bayu Dwi Pangestu(1101210293) | [@IcyCreamy](https://github.com/IcyCreamy)
- Rifky Agung Febrian(1101210431) | [@Lum1sty](https://github.com/Lum1sty)
