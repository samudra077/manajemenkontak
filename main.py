"Program Manajemen Kontak"

def melihat_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["Nama"]} ({item["No_Hp"]}), ({item["email"]})')
        #melihat semua kontak
    else:
        print("kontak Masih kosong")
        return 1


def menambah_kontak():
    # menambahkan kontak
    Nama = input("Masukan Nama Kontak Baru")
    No_Hp = input("Masukan No Hp Baru")
    email = input("Masukan Email Baru")
    kontak_baru = {'Nama': Nama, 'No_Hp': No_Hp, 'email': email}
    kontak.append(kontak_baru)  # menambahkan satu list
    print(f"kontak Baru Bernama {Nama} Berhasil Ditambahkan")

def menghapus_kontak():
    if melihat_kontak() == 1:
        return
    else:
        # menghapus kont  ak
        i_hapus = int(input('Masukkan No Yang Akan Dihapus'))
        del kontak[i_hapus - 1]
        print(f"kontak yang dimaksud sudah dihapus")

#type Dictionery {"Key" : "Velue"}
kontak1 = {'Nama' : "Samudra", 'No_Hp':"081113502486", 'email': "Samudra@python"}
kontak2 = {'Nama' : "andi", 'No_Hp':"081113502484", 'email': "andi@python"}
kontak3 = {'Nama' : "andri", 'No_Hp':"081113502446", 'email': "andri@python"}

#type List []
kontak = [kontak1, kontak2, kontak3]

while True:
    print("Menu Kontak Saya")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Dari kontak")

    pilihan = input("Masukan Pilihan Menu Kontak ")
    if pilihan =='1':
        melihat_kontak()

    elif pilihan =='2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

    elif pilihan =='4':
        break
    else :

        print('Anda Memasukan Pilihan Yang Salah')
        continue
