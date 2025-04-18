"Program Manajemen Kontak"
class kontak:
    def __init__(self):
        self.kontak = []


    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["Nama"]} ({item["No_Hp"]}), ({item["email"]})')
            #melihat semua kontak
        else:
            print("kontak Masih kosong")
            return 1


    def menambah_kontak(self):
        # menambahkan kontak
        Nama = input("Masukan Nama Kontak Baru")
        No_Hp = input("Masukan No Hp Baru")
        email = input("Masukan Email Baru")
        kontak_baru = {'Nama': Nama, 'No_Hp': No_Hp, 'email': email}
        self.kontak.append(kontak_baru)  # menambahkan satu list
        print(f"kontak Baru Bernama {Nama} Berhasil Ditambahkan")

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            # menghapus kontak
            i_hapus = int(input("Masukkan No Yang Akan Dihapus : "))
            del self.kontak[i_hapus - 1]
            print(f"kontak yang dimaksud sudah dihapus")

kontak_kantor = kontak()
kontak_keluarga = kontak()
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
        kontak_kantor.melihat_kontak()

    elif pilihan =='2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan =='4':
        break
    else :

        print('Anda Memasukan Pilihan Yang Salah')
        continue
