users = [
    {'user_id': 1, 'alamat': 'Jl. Fitness', 'nama': 'Hayyan'},
    {'user_id': 2, 'alamat': 'Jl. Kesehatan', 'nama': 'Fares'},
    {'user_id': 3, 'alamat': 'Jl. Kebugaran', 'nama': 'Hizam'},
    {'user_id': 4, 'alamat': 'Jl. Olahraga', 'nama': 'Nizar'},
    {'user_id': 5, 'alamat': 'Jl. Sehat', 'nama': 'Singgih'},
    {'user_id': 6, 'alamat': 'Jl. Sentosa', 'nama': 'Asa'},
]

products = [
    {'produk_id': 1, 'nama_produk': 'Suplemen', 'jumlah_produk': 50},
    {'produk_id': 2, 'nama_produk': 'Membership Bulanan', 'jumlah_produk': 100}
]

tax_categories = [
    {'item_category': 'S', 'tax_rate': 0.15},  # Suplemen dengan 15% pajak
    {'item_category': 'M', 'tax_rate': 0.1}   # Membership dengan 10% pajak
]

# Hitung Pajak Penjualan untuk Layanan atau Produk Gym
def compute_sales_tax(item_type: str, sales_amount: int):
    # Validasi input
    if not isinstance(sales_amount, (int, float)) or sales_amount < 0:
        print("Jumlah penjualan harus berupa angka positif")
        return None

    for category in tax_categories:
        if item_type.upper() == category['item_category']:
            sales_tax = sales_amount * category['tax_rate']
            print(f"Pajak untuk item {item_type.upper()}: {sales_tax}")
            return sales_tax

    print("Item tidak valid. Gunakan 'S' untuk Suplemen atau 'M' untuk Membership")
    return None

# Cari Anggota Gym Berdasarkan ID
def find_user_by_id(user_id: int):
    if not isinstance(user_id, int):
        print("ID user harus berupa angka.")
        return None

    for user in users:
        if user['user_id'] == user_id:
            print(f"User ditemukan: {user['nama']}, Alamat: {user['alamat']}")
            return user

    print("User tidak ditemukan.")
    return None

# Cari Produk Gym Berdasarkan ID (contoh: Suplemen atau Membership)
def find_product_by_id(produk_id: int):
    if not isinstance(produk_id, int):
        print("ID produk harus berupa angka.")
        return None

    for product in products:
        if product['produk_id'] == produk_id:
            print(f"Produk ditemukan: {product['nama_produk']}, Jumlah: {product['jumlah_produk']}")
            return product

    print("Produk tidak ditemukan.")
    return None

# Tambah Produk atau Layanan Gym ke Database
def add_product(produk_id: int, nama_produk: str, jumlah_produk: int):
    if not isinstance(produk_id, int) or not isinstance(jumlah_produk, int) or not nama_produk:
        print("Data produk tidak valid. Pastikan ID dan jumlah berupa angka, nama produk tidak boleh kosong.")
        return None

    for product in products:
        if product['produk_id'] == produk_id:
            print(f"Produk dengan ID {produk_id} sudah ada.")
            return None

    new_product = {'produk_id': produk_id, 'nama_produk': nama_produk, 'jumlah_produk': jumlah_produk}
    products.append(new_product)
    print(f"Produk/Layanan {nama_produk} berhasil ditambahkan ke database.")

# Update Jumlah Produk Gym (misal stok suplemen atau kapasitas membership)
def update_product_quantity(produk_id: int, jumlah_produk: int):
    if not isinstance(produk_id, int) or not isinstance(jumlah_produk, int) or jumlah_produk < 0:
        print("Data tidak valid. ID dan jumlah harus berupa angka, dan jumlah tidak boleh negatif.")
        return None

    for product in products:
        if product['produk_id'] == produk_id:
            product['jumlah_produk'] = jumlah_produk
            print(f"Jumlah produk {product['nama_produk']} diperbarui menjadi {jumlah_produk}")
            return product

    print("Produk tidak ditemukan.")
    return None

# Hapus Produk Gym Berdasarkan ID
def delete_product(produk_id: int):
    if not isinstance(produk_id, int):
        print("ID produk harus berupa angka.")
        return None

    global products
    initial_length = len(products)
    products = [product for product in products if product['produk_id'] != produk_id]

    if len(products) < initial_length:
        print(f"Produk dengan ID {produk_id} berhasil dihapus.")
    else:
        print(f"Produk dengan ID {produk_id} tidak ditemukan.")

# Fungsi untuk menampilkan menu
def display_menu():
    print("\n=== Menu Aplikasi Gym ===")
    print("1. Hitung Pajak Penjualan")
    print("2. Cari Anggota Gym")
    print("3. Cari Produk Gym")
    print("4. Tambah Produk")
    print("5. Update Jumlah Produk")
    print("6. Hapus Produk")
    print("0. Keluar")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        display_menu()
        choice = input("Pilih opsi (0-6): ")

        if choice == '1':
            item_type = input("Masukkan jenis item (S untuk Suplemen, M untuk Membership): ")
            sales_amount = float(input("Masukkan jumlah penjualan: "))
            compute_sales_tax(item_type, sales_amount)

        elif choice == '2':
            user_id = int(input("Masukkan ID pengguna: "))
            find_user_by_id(user_id)

        elif choice == '3':
            produk_id = int(input("Masukkan ID produk: "))
            find_product_by_id(produk_id)

        elif choice == '4':
            produk_id = int(input("Masukkan ID produk: "))
            nama_produk = input("Masukkan nama produk: ")
            jumlah_produk = int(input("Masukkan jumlah produk: "))
            add_product(produk_id, nama_produk, jumlah_produk)

        elif choice == '5':
            produk_id = int(input("Masukkan ID produk yang ingin diupdate: "))
            jumlah_produk = int(input("Masukkan jumlah produk baru: "))
            update_product_quantity(produk_id, jumlah_produk)

        elif choice == '6':
            produk_id = int(input("Masukkan ID produk yang ingin dihapus: "))
            delete_product(produk_id)

        elif choice == '0':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Opsi tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
