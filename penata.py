import pygetwindow as gw
import time

# --- KONFIGURASI TATA LETAK ---
LEBAR_JENDELA   = 654
TINGGI_JENDELA  = 1039
POSISI_X_AWAL   = -7
POSISI_Y_AWAL   = 0
GESER_X         = 110
GESER_Y         = 0
JUMLAH_MAKSIMAL = 13
# -----------------------------

def atur_tata_letak():
    """
    Menemukan dan mengatur jendela Chrome sesuai konfigurasi.
    """
    try:
        all_windows = gw.getWindowsWithTitle('Chrome')
        
        # Mengabaikan jendela 'helper' yang mungkin digunakan untuk pengukuran
        target_windows = [win for win in all_windows if win.title not in ("UKUR", "INFO")]
        
        if not target_windows:
            print("Tidak ada jendela Chrome yang ditemukan untuk diatur.")
            return

        print(f"Mengatur {min(len(target_windows), JUMLAH_MAKSIMAL)} dari {len(target_windows)} jendela Chrome...")
        
        for i, window in enumerate(target_windows):
            if i >= JUMLAH_MAKSIMAL:
                break
            
            if window.isMinimized:
                window.restore()

            new_pos_x = POSISI_X_AWAL + (i * GESER_X)
            new_pos_y = POSISI_Y_AWAL + (i * GESER_Y)
            
            window.resizeTo(LEBAR_JENDELA, TINGGI_JENDELA)
            window.moveTo(new_pos_x, new_pos_y)
            time.sleep(0.05)

        print("Pengaturan tata letak selesai.")

    except Exception as e:
        print(f"Terjadi sebuah kesalahan: {e}")

if __name__ == "__main__":
    atur_tata_letak()