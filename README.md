# Final_Praktikum
# Muhammad Faiz Iqbal
# Kasir Kantin

## Link Youtube :
   - https://youtu.be/F8KK2M3231g
## Let's discuss 
### Daftar Menu (menu):
   - menu adalah kamus (dictionary) yang menyimpan daftar item makanan beserta harganya.
   - Setiap item memiliki nomor urut, nama item, dan harga.

### Fungsi tampilkan_menu():
   - Fungsi ini menampilkan daftar menu ke layar dengan nomor urut, nama item, dan harga.

### Fungsi hitung_total(pesanan):
   - Fungsi ini menghitung total harga pesanan berdasarkan item yang dipilih dan jumlahnya.
   - Iterasi melalui pesanan dan mengakumulasikan total harga setiap item.

### Fungsi tampilkan_promosi():
   - Fungsi ini menampilkan informasi promosi hari ini, seperti diskon untuk pembelian di atas Rp 50.000 dan gratis Es Teh untuk setiap pembelian Nasi Goreng.

### Fungsi terapkan_promosi(pesanan, total_harga):
   - Fungsi ini menerapkan potongan harga atau item gratis berdasarkan aturan promosi yang telah ditentukan.
   - Jika total harga melebihi Rp 50.000, maka diberikan diskon sebesar 10%.
   - Jika Nasi Goreng (item nomor 1) ada dalam pesanan, maka Es Teh (item nomor 4) ditambahkan ke pesanan sebagai bonus.

### Fungsi hitung_kembalian(total_harga, uang_tunai):
   - Fungsi ini menghitung kembalian berdasarkan total harga pesanan dan jumlah uang tunai yang diberikan.
   - Menampilkan informasi uang tunai, total harga, dan kembalian.

### Fungsi main():
   - Fungsi utama yang menjalankan program.
   - Pengguna diminta untuk memilih item dari menu, memasukkan jumlah yang diinginkan, dan mengulangi proses hingga pengguna memilih untuk berhenti.
   - Setelah pesanan selesai, promosi diterapkan, dan pengguna diminta memasukkan jumlah uang tunai.
   - Program menghitung total harga, kembalian, dan menampilkan struk pembelian.

### Eksekusi Program (if __name__ == "__main__": main()):
   - Memastikan bahwa program dijalankan hanya jika ini adalah eksekusi langsung (bukan diimpor sebagai modul).
   - Memanggil fungsi main() untuk menjalankan program.

### Catatan:
   - Gunakan nomor urut menu untuk memilih item.
   - Program memproses pesanan, menghitung total harga, menerapkan promosi, dan menghitung kembalian sesuai dengan uang tunai yang dimasukkan.
