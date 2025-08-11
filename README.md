README - Skrip Pengatur Tata Letak Jendela Chrome (Metode Presisi)
=================================================================

Deskripsi:
-----------
Skrip ini digunakan untuk mengatur tata letak beberapa jendela Google Chrome secara otomatis di layar. 
Jendela akan diatur secara presisi dengan lebar, tinggi, dan jarak horizontal yang disesuaikan berdasarkan 
jumlah jendela yang ingin diatur.

Fitur utama:
-------------
- Mengatur posisi dan ukuran jendela Chrome secara otomatis.
- Mendukung pengaturan antara 5 sampai 13 jendela.
- Memastikan jendela yang diminimize akan dikembalikan (restore) sebelum diatur.
- Menyesuaikan jarak antar jendela secara dinamis agar rapi dan tidak tumpang tindih.

Persyaratan:
-------------
- Python 3.x
- Modul Python `pygetwindow` (bisa diinstall via pip: pip install pygetwindow)
- Sistem operasi dengan dukungan manajemen jendela (biasanya Windows/Linux dengan GUI)

Cara menjalankan:
-----------------
1. Pastikan semua jendela Chrome yang ingin diatur sudah terbuka.
2. Jalankan skrip dengan perintah: `python nama_script.py`
3. Masukkan jumlah jendela Chrome yang ingin diatur ketika diminta (minimal 5, maksimal 13).
4. Skrip akan otomatis mengatur ukuran dan posisi jendela-jendela tersebut.
5. Tekan Enter untuk keluar setelah selesai.

Variabel konfigurasi utama:
----------------------------
- LEBAR_JENDELA_STATIS: Lebar jendela Chrome dalam piksel (default 654).
- TINGGI_JENDELA_STATIS: Tinggi jendela Chrome dalam piksel (default 1039).
- POSISI_X_AWAL: Posisi horizontal awal jendela paling kiri (default -7).
- JUMLAH_MAKSIMAL_ASLI: Jumlah maksimal jendela default untuk referensi jarak (default 13).
- GESER_X_ASLI: Jarak geser horizontal default antar jendela (default 110 px).

Catatan:
---------
- Skrip hanya mengatur jendela yang berjudul mengandung "Chrome".
- Pastikan jendela Chrome tidak dalam kondisi minimize untuk hasil terbaik (meskipun skrip akan restore).
- Rentang jumlah jendela yang bisa diatur dibatasi antara 5 sampai 13 untuk menjaga tata letak tetap rapi.

Lisensi:
---------
Skrip ini dibagikan secara bebas untuk penggunaan pribadi dan edukasi.
