
Auto Window Tiler - Chrome Layout Organizer
===========================================

Script ini secara otomatis mengatur tata letak jendela Chrome di layar kamu berdasarkan konfigurasi posisi, ukuran, dan jumlah maksimum jendela. Cocok digunakan untuk pengujian otomatis, multi-login, atau workflow paralel menggunakan banyak instance Chrome.

Fitur
-----
- Mengatur ukuran dan posisi hingga 15 jendela Chrome.
- Mengabaikan jendela Chrome tertentu (misalnya jendela dengan judul 'UKUR' atau 'INFO').
- Otomatis membuka kembali jendela jika diminimize.
- Ukuran dan posisi dapat disesuaikan melalui konfigurasi.

Cara Menggunakan
----------------
1. Install dependensi terlebih dahulu (jika belum):
   pip install pygetwindow

2. Jalankan script dengan Python:
   python atur_tata_letak.py

3. Pastikan jendela-jendela Chrome yang ingin diatur sudah dibuka sebelumnya.

Konfigurasi
-----------
Di bagian atas script, kamu bisa mengubah konfigurasi berikut:

LEBAR_JENDELA   = 654     # Lebar jendela Chrome
TINGGI_JENDELA  = 1039    # Tinggi jendela Chrome
POSISI_X_AWAL   = -7      # Posisi X awal dari jendela pertama
POSISI_Y_AWAL   = 0       # Posisi Y awal dari jendela pertama
GESER_X         = 110     # Perpindahan X antar jendela
GESER_Y         = 0       # Perpindahan Y antar jendela
JUMLAH_MAKSIMAL = 15      # Jumlah maksimal jendela yang akan diatur

Contoh Output
-------------
Mengatur 10 dari 10 jendela Chrome...
Pengaturan tata letak selesai.

Catatan
-------
- Script ini hanya bekerja pada Windows OS karena menggunakan pygetwindow yang berbasis Win32 API.
- Judul jendela Chrome harus mengandung kata 'Chrome' (case-sensitive).

Lisensi
-------
Proyek ini bebas digunakan untuk keperluan pribadi atau produktivitas. Tidak untuk dijual kembali dalam bentuk apapun.
