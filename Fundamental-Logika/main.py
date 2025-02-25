member = [ "Felix", "Ricko", "Arif"]

while True:
    tambah_member = input("Masukkan nama member yang ingin ditambahkan: ").capitalize()
    
    if not tambah_member.strip():
        print("Tidak boleh kosong")
    else:
        member.append(tambah_member)
        print(f'{tambah_member} berhasil ditambahkan')

    print("Daftar member: ")
    index = 0
    for nama in member:
        index+=1
        print(f'{"*" * index}. {nama}')