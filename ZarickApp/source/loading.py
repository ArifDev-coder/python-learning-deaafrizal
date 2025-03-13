from time import sleep  # Impor fungsi sleep dari modul time

def loading():
    for i in range(5):  # Loop sebanyak 5 kali
        dots = '.' * ((i % 3) + 1)  # Buat string dengan 1 hingga 3 titik, berulang setiap 3 iterasi
        print(f"Loading{dots}", end='\r')  # Cetak pesan loading dengan titik, menimpa baris sebelumnya
        sleep(1)  # Jeda selama 1 detik
    print("Exiting...")
    print("Exit")  # Cetak pesan keluar setelah loop selesai

if __name__ == "__main__":
    loading()  # Panggil fungsi loading jika skrip ini dijalankan langsung