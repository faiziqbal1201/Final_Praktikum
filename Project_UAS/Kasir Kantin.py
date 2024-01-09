menu = {
    1: {"item": "Nasi Goreng", "harga": 13000},
    2: {"item": "Mie Goreng", "harga": 13000},
    3: {"item": "Ayam Goreng", "harga": 18000},
    4: {"item": "Es Teh", "harga": 2000},
    5: {"item": "Es Jeruk", "harga": 5000},
}

def tampilkan_menu():
    print("========== Daftar Menu ==========")
    for key, value in menu.items():
        print(f"{key}. {value['item']} \t: Rp {value['harga']}\t|")
    print("=================================")

def hitung_total(pesanan):
    total = 0
    for pilihan, jumlah in pesanan.items():
        total += menu[pilihan]["harga"] * jumlah
    return total

def hitung_kembalian(total_harga, uang_tunai):
    kembalian = uang_tunai - total_harga
    if kembalian >= 0:
        print(f"\nUang Anda: Rp {uang_tunai}")
        print(f"Total Harga: Rp {total_harga}")
        print(f"Kembalian: Rp {kembalian}")
    else:
        print("\nMaaf, uang tunai Anda kurang. Pembayaran dibatalkan.")

def main():
    pesanan = {}
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Masukkan nomor menu yang diinginkan \t: "))
            if pilihan == 0:
                break
            elif pilihan not in menu:
                print("Pilihan tidak valid. Silakan masukkan nomor yang benar -_-")
            else:
                jumlah = int(input(f"Masukkan jumlah yang ingin dibeli\t: "))
                if pilihan in pesanan:
                    pesanan[pilihan] += jumlah
                else:
                    pesanan[pilihan] = jumlah
        except ValueError:
            print("Masukkan nomor atau jumlah yang valid.")

    if not pesanan:
        print("Anda belum memesan apapun.")
    else:
        total_harga = hitung_total(pesanan)
        uang_tunai = float(input("\nMasukkan jumlah uang tunai \t\t: "))
        hitung_kembalian(total_harga, uang_tunai)

        print("\n============ Struk Pembelian ============")
        for pilihan, jumlah in pesanan.items():
            print(f"{menu[pilihan]['item']} Sejumlah {jumlah} \t= Rp {menu[pilihan]['harga'] * jumlah}\t|")
        print(f"Total Harga \t\t= Rp {total_harga}\t|")
        print("=========================================")

if __name__ == "__main__":
    main()
