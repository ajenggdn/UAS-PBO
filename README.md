Nama Kelompok

Idznii Sholekha (G1F022001)

Dewi Margiani (G1F022037)

Diajeng Noviana Sari (G1F022065)

Program yang kami jalankan adalah Server ruang obrolan menggunakan Python: Menggunakan ide soket dan threading, skrip ini membantu menyiapkan Ruang Obrolan sederhana yang memungkinkan beberapa klien untuk terhubung. Kode ini bekerja dengan ide soket dan threading.


Source Code


![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/e7c934d6-967c-4762-ac64-b61fe71819d2)

Penjelasan Source Code


![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/d780eb71-024f-4937-8eee-c3b66440e8de)

Pada kode diatas berfungsi untuk mengimport library dari dalam flask agar dapat digunakan service web menggunakan bahasa pemrograman python kemudian digunakan juga render_template untuk menampilkan file html. Kemudian dengan kode request berfungsi untuk menampung inputan dari html dan url_for artinya untuk menjalankan form ke dalam routing yang kita inginkan.


![Screenshot 2023-12-17 113808](https://github.com/ajenggdn/UAS-PBO/assets/145746946/36518e6d-f2c1-4144-a766-74f5d7416b50)

Pada kode diatas import statement itu seperti membuka kotak alat. Nah, dari kotak alat Flask SocketIO, kita ambil beberapa alat spesifik, yaitu SocketIO, join_room, dan leave_room. SocketIO itu ibaratnya alat utama yang bisa kita gunakan untuk bikin layanan obrolan atau notifikasi langsung. Terus, join_room digunakan buat masuk ke dalam ruang percakapan tertentu, kayak masuk ke dalam ruang obrolan. Sementara leave_room digunakan buat keluar dari ruang obrolan. Jadi, dengan alat-alat ini, kita bisa masuk dan keluar dari ruangan obrolan sesuai kebutuhan.


![Screenshot 2023-12-17 114332](https://github.com/ajenggdn/UAS-PBO/assets/145746946/516950a8-b14b-41e1-aaf4-637927b1d2c3)

Pada kode diatas akan menciptakan sebuah objek aplikasi Flask (app) dan objek SocketIO (socketio). Kemudian untuk fungsi dari ['SECRET_KEY'] ialah untuk melindungan sesi aplikasi Flask.


![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/fcf8cf70-dddb-4a0b-8562-a63b6a0f004a)

Kode diatas ialah berfungsi untuk membuat sebuah variabel berbentuk objek yang dapat menampung data room dari aplikasi chat.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/0b027f61-6cb5-4598-a971-a294e627587a)

Kode ini memiliki fungsi route utama yang merender template 'index.html' saat pengguna mengakses halaman utama aplikasi.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/c9796e1e-cab6-4403-b05f-5fdee30763a2)

Kode ini adalah route yang merespons data form yang disubmit oleh pengguna saat mereka masuk ke ruang obrol. Data ini kemudian digunakan untuk merender template 'chat.html' dengan informasi username dan room.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/5d757db9-5b1a-4528-b458-b446b36e7165)

Pada kode diatas merupakan penjelasan dari Event handler yang menangani peristiwa ketika pengguna bergabung ke dalam ruangan obrol. user akan bergabung ke ruangan menggunakan join_room dan mengirim pesan ke semua pengguna di ruangan melalui socketio.emit.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/254c56cb-74d7-41d0-a0a0-7343815bacbc)

Pada kode diatas merupakan Event handler yang menangani peristiwa ketika pengguna mengirim pesan. Pesan tersebut kemudian disiarkan ke semua pengguna di ruangan dengan menggunakan socketio.emit.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/905651d1-c3a3-4d86-927b-026feb3ea8f9)

Pada kode diatas merupakan Event handler yang menangani peristiwa ketika pengguna keluar dari ruangan obrol. Mereka meninggalkan ruangan menggunakan leave_room dan mengirim pesan ke semua pengguna di ruangan melalui socketio.emit.

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/f3da93ca-ce4d-4a02-bd74-e6e0f9b7b387)

Pada kode diatas merupakan kode yang akan menjalankan aplikasi Flask menggunakan SocketIO. Jika aplikasi dijalankan langsung (bukan diimpor sebagai modul), maka mode debug akan diaktifkan.

HASIL TAMPILAN PROGRAM

1. Tampilan Pertama


![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/b60d1427-c904-4d74-a7e9-be4e910c1a99)

Penjelasan:

Tampilan program server ruang obrolan dalam gambar yang Anda kirim menunjukkan halaman selamat datang untuk ruang obrolan. Halaman ini menampilkan pesan selamat datang untuk pengguna yang baru masuk ke ruang obrolan, serta daftar pengguna yang saat ini berada di ruang obrolan.

Pada bagian atas halaman, terdapat pesan selamat datang yang bertuliskan "Welcome, Diajeng Noviana Sari!" Pesan ini menunjukkan bahwa pengguna dengan nama "Diajeng Noviana Sari" baru saja masuk ke ruang obrolan.

Di bawah pesan selamat datang, terdapat daftar pengguna yang saat ini berada di ruang obrolan. Pada gambar ini, daftar pengguna berisi tiga nama, yaitu: Diajeng Noviana Sari (baru saja masuk), Dewi Margiani (baru saja masuk), Idzni Sholekha (baru saja masuk).

Pada bagian bawah halaman, terdapat kolom untuk memasukkan pesan. Pengguna dapat menggunakan kolom ini untuk mengirim pesan ke pengguna lain di ruang obrolan. Untuk mengirim pesan, pengguna cukup mengetikkan pesan dan kemudian menekan tombol "Send".

2. Tampilan Lanjutan

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/94749e2b-6334-4dc9-80e4-f1707b6d857e)

Penjelasan:

Tampilan diatas menunjukkan sebuah formulir yang meminta pengguna untuk memasukkan nama, dan nama ruang obrolan. Formulir ini digunakan untuk mendaftar ke ruang obrolan.

Pada bagian atas formulir, terdapat label "Nama". Pengguna harus memasukkan nama mereka di kolom yang disediakan. Kemudian pada gambar diatas Nama yang mendaftar adalah Dewi Margiani dan dengan nama ruang obrolan Proyek PBO.

Setelah melakukan pengisian form dapat dilanjutkan dengan klik tombol "Join Chat" agar dapat bergabung kedalam ruang obrolan Proyek PBO.


3. Tampilan Lanjutan

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/74091d3a-5fe3-473a-8833-565ac44031bf)

Penjelasan :

Tampilan diatas menunjukkan sebuah formulir yang meminta pengguna untuk memasukkan nama, dan nama ruang obrolan. Formulir ini digunakan untuk mendaftar ke ruang obrolan.

Pada bagian atas formulir, terdapat label "Nama". Pengguna harus memasukkan nama mereka di kolom yang disediakan. Kemudian pada gambar diatas Nama yang mendaftar adalah Idzni Sholekha dan dengan nama ruang obrolan Proyek PBO.

Setelah melakukan pengisian form dapat dilanjutkan dengan klik tombol "Join Chat" agar dapat bergabung kedalam ruang obrolan Proyek PBO.

4. Tampilan Ruang Obrolan Dari User Diajeng

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/a5b7fc01-7bfb-4c75-872b-58849d532c0c)

Penjelasan:

Tampilan ruang obrolan dari user Diajeng menunjukkan bahwa dia baru saja masuk ke ruang obrolan. Hal ini terlihat dari pesan selamat datang yang bertuliskan "Welcome, Diajeng Noviana Sari!" Di bawah pesan selamat datang, terdapat daftar pengguna yang saat ini berada di ruang obrolan.

Pada gambar ini, terlihat bahwa Diajeng baru saja mengirim pesan pertamanya ke ruang obrolan. Pesan tersebut bertuliskan "hallo gess apa kabarr". Pesan ini ditujukan kepada semua pengguna yang saat ini berada di ruang obrolan. Dan disambung obrolan seperti pada gambar diatas.

Kemudian terdapat kolom untuk memasukkan pesan yang digunakan pengguna untuk mengirim pesan ke pengguna lain di ruang obrolan. Dan tombol "Send" untuk mengirim pesan yang telah diketik oleh pengguna.

5. Tampilan Ruang Obrolan Dari User Idzni

![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/88afa93d-c696-4b32-9ea3-0b56cea36464)

Penjelasan:

Tampilan ruang obrolan dari user Idzni menunjukkan bahwa dia baru saja masuk ke ruang obrolan. Hal ini terlihat dari pesan selamat datang yang bertuliskan "Welcome, Idzni Sholekha!"

Pada bagian bawah halaman, terdapat kolom untuk memasukkan pesan. Pengguna dapat menggunakan kolom ini untuk mengirim pesan ke pengguna lain di ruang obrolan. Untuk mengirim pesan, pengguna cukup mengetikkan pesan dan kemudian menekan tombol "Send".

6. Tampilan Ruang Obrolan Dari User Dewi


![image](https://github.com/ajenggdn/UAS-PBO/assets/145746946/10a8f707-0daa-4625-af67-9a5d628f8901)

Penjelasan:

Tampilan ruang obrolan dari user Dewi menunjukkan bahwa dia baru saja masuk ke ruang obrolan. Hal ini terlihat dari pesan selamat datang yang bertuliskan "Welcome, Dewi Margiani!"

Pada gambar ini, terlihat bahwa Dewi baru saja mengirim pesan pertamanya ke ruang obrolan. Pesan tersebut bertuliskan "Baik". Pesan ini ditujukan kepada semua pengguna yang saat ini berada di ruang obrolan.

Kemudian untuk bagian bawah halaman, terdapat kolom untuk memasukkan pesan. Pengguna dapat menggunakan kolom ini untuk mengirim pesan ke pengguna lain di ruang obrolan. Untuk mengirim pesan, pengguna cukup mengetikkan pesan dan kemudian menekan tombol "Send".





















