import pygetwindow as gw
import time

LEBAR_JENDELA_STATIS = 654
TINGGI_JENDELA_STATIS = 1039
POSISI_X_AWAL = -7
JUMLAH_MAKSIMAL_ASLI = 13
GESER_X_ASLI = 110

def atur_tata_letak_presisi(jumlah_jendela_diminta):
    try:
        lebar_total_pergeseran_asli = (JUMLAH_MAKSIMAL_ASLI - 1) * GESER_X_ASLI
        if jumlah_jendela_diminta <= 1:
            geser_x_dinamis = 0
        else:
            geser_x_dinamis = lebar_total_pergeseran_asli / (jumlah_jendela_diminta - 1)
        GESER_X_BARU = int(geser_x_dinamis)
        print(f"Untuk {jumlah_jendela_diminta} jendela, pergeseran presisi dihitung: {GESER_X_BARU}px")
        all_windows = gw.getWindowsWithTitle('Chrome')
        target_windows = [win for win in all_windows if win.title not in ("UKUR", "INFO")]
        if not target_windows:
            print("Tidak ada jendela Chrome yang ditemukan untuk diatur.")
            return
        jumlah_untuk_diatur = min(len(target_windows), jumlah_jendela_diminta)
        print(f"Mengatur {jumlah_untuk_diatur} dari {len(target_windows)} jendela yang ditemukan...")
        for i, window in enumerate(target_windows):
            if i >= jumlah_untuk_diatur:
                break
            if window.isMinimized:
                window.restore()
                time.sleep(0.05)
            new_pos_x = POSISI_X_AWAL + (i * GESER_X_BARU)
            window.resizeTo(LEBAR_JENDELA_STATIS, TINGGI_JENDELA_STATIS) 
            window.moveTo(new_pos_x, 0)
            time.sleep(0.05)
        print("selesai.")
    except Exception as e:
        print(f"Terjadi sebuah kesalahan: {e}")
def dapatkan_input_pengguna():
    try:
        masukan = input("Masukkan jumlah jendela Chrome yang ingin diatur (min 5 dan maks 13): ")
        jumlah = int(masukan)
        if 5 <= jumlah <= 13:
            return jumlah
        else:
            print("Input tidak valid. Harap masukkan angka antara 5 dan 13.")
            exit()
    except ValueError:
        print("Input tidak valid. Harap masukkan sebuah angka.")
        exit()
if __name__ == "__main__":
    print("---PENATA ---")
    jumlah_yang_diinginkan = dapatkan_input_pengguna()
    atur_tata_letak_presisi(jumlah_yang_diinginkan)
