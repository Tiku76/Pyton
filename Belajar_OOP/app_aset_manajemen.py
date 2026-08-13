import os


class Aset:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga


class AsetKendaraan(Aset):
    def __init__(self, kode, nama, harga, stnk, tahun):
        super().__init__(kode, nama, harga)
        self.stnk = stnk
        self.tahun = tahun


class AsetElektronik(Aset):
    def __init__(self, kode, nama, harga, serial_number):
        super().__init__(kode, nama, harga)
        self.serial_number = serial_number


class AsetTanahBangunan(Aset):
    def __init__(self, kode, nama, harga, sertifikat, njop, luas):
        super().__init__(kode, nama, harga)
        self.sertifikat = sertifikat
        self.njop = njop
        self.luas = luas


class DaftarAset:
    def __init__(self):
        # FIX: sebelumnya "datar_aset" (typo), diseragamkan jadi "daftar_aset"
        self.daftar_aset = []

    def tambah_aset(self, aset):
        self.daftar_aset.append(aset)

    def ambil_aset(self, kode):
        for aset in self.daftar_aset:
            if aset.kode == kode:
                return aset
        return None

    def hapus_aset(self, kode):
        for i, aset in enumerate(self.daftar_aset):
            if aset.kode == kode:
                del self.daftar_aset[i]
                # FIX: sebelumnya tidak ada return True, jadi selalu dianggap gagal
                return True
        return False


class AplikasiAsetManagement:
    def __init__(self):
        self.daftar_aset = DaftarAset()

    def run(self):
        while True:
            print("1. Tambah aset")
            print("2. Lihat daftar aset")  # FIX: typo "dahtar" -> "daftar"
            print("3. Keluar")
            pilih = int(input("pilih menu: "))

            if pilih == 1:
                self.run_tambah_aset()
            elif pilih == 2:
                self.run_lihat_daftar_aset()
            elif pilih == 3:
                break

    def run_tambah_aset(self):
        while True:
            print("1. Tambah Kendaraan")
            print("2. Tambah Elektronik")
            print("3. Tambah Tanah Bangunan")
            print("4. Kembali")
            pilih = int(input("Pilih menu: "))

            if pilih == 1:
                self.run_tambah_aset_kendaraan()
            elif pilih == 2:
                self.run_tambah_aset_elektronik()
            elif pilih == 3:
                self.run_tambah_aset_tanah_bangunan()
            elif pilih == 4:
                break

    def run_tambah_aset_kendaraan(self):
        print("Tambah Kendaraan")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = int(input("Harga: "))
        stnk = input("STNK: ")  # FIX: typo "STKN" -> "STNK"
        tahun = int(input("Tahun: "))

        aset_kendaraan = AsetKendaraan(kode, nama, harga, stnk, tahun)
        self.daftar_aset.tambah_aset(aset_kendaraan)

    def run_tambah_aset_elektronik(self):
        print("Tambah Elektronik")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = int(input("Harga: "))
        serial_number = input("Serial Number: ")

        aset_elektronik = AsetElektronik(kode, nama, harga, serial_number)
        self.daftar_aset.tambah_aset(aset_elektronik)

    def run_tambah_aset_tanah_bangunan(self):
        print("Tambah Tanah Bangunan")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = int(input("Harga: "))
        sertifikat = input("Sertifikat: ")
        njop = int(input("NJOP: "))
        luas = int(input("Luas: "))

        aset_tanah_bangunan = AsetTanahBangunan(
            kode, nama, harga, sertifikat, njop, luas
        )
        self.daftar_aset.tambah_aset(aset_tanah_bangunan)

    # FIX: nama method typo "datar_aset" -> "daftar_aset"
    def run_lihat_daftar_aset_kendaraan(self, aset):
        print("Aset Kendaraan")
        print("Kode:", aset.kode)
        print("Nama:", aset.nama)
        print("Harga:", aset.harga)
        print("STNK:", aset.stnk)  # FIX: "aset.stkn" -> "aset.stnk"
        print("Tahun:", aset.tahun)
        print()

    def run_lihat_daftar_aset(self):
        for aset in self.daftar_aset.daftar_aset:
            if isinstance(aset, AsetKendaraan):
                self.run_lihat_daftar_aset_kendaraan(aset)
            elif isinstance(aset, AsetElektronik):
                print("Aset Elektronik")
                print("Kode:", aset.kode)
                print("Nama:", aset.nama)
                print("Harga:", aset.harga)
                print("Serial Number:", aset.serial_number)
                print()
            elif isinstance(aset, AsetTanahBangunan):
                print("Aset Tanah Bangunan")
                print("Kode:", aset.kode)
                print("Nama:", aset.nama)
                print("Harga:", aset.harga)
                print("Sertifikat:", aset.sertifikat)
                print("NJOP:", aset.njop)
                print("Luas:", aset.luas)
                print()

        print("Menu")
        print("1. Ubah Aset")
        print("2. Hapus Aset")
        print("3. Kembali")
        pilih = int(input("Pilih menu:"))

        if pilih == 1:
            self.run_ubah_aset()
        elif pilih == 2:
            self.run_hapus_aset()

    def run_hapus_aset(self):
        kode = input("Kode:")
        if self.daftar_aset.hapus_aset(kode):
            print("Aset berhasil dihapus")  # FIX: typo "berhaasil" -> "berhasil"
        else:
            print("Tidak ditemukan aset dengan kode : ", kode)

    def run_ubah_aset(self):
        kode = input("Kode :")
        aset = self.daftar_aset.ambil_aset(kode)

        if aset is None:
            print(f"Tidak ditemukan aset dengan kode : {kode}")
        else:
            if isinstance(aset, AsetKendaraan):
                nama = input("Nama: ")
                harga = int(input("Harga: "))
                stnk = input("STNK: ")
                tahun = int(input("Tahun: "))

                aset.nama = nama
                aset.harga = harga
                aset.stnk = stnk  # FIX: "aset.stkn" -> "aset.stnk"
                aset.tahun = tahun

                print("Aset berhasil diubah")
            # FIX: sebelumnya tidak ada penanganan untuk AsetElektronik
            elif isinstance(aset, AsetElektronik):
                nama = input("Nama: ")
                harga = int(input("Harga: "))
                serial_number = input("Serial Number: ")

                aset.nama = nama
                aset.harga = harga
                aset.serial_number = serial_number

                print("Aset berhasil diubah")
            # FIX: sebelumnya tidak ada penanganan untuk AsetTanahBangunan
            elif isinstance(aset, AsetTanahBangunan):
                nama = input("Nama: ")
                harga = int(input("Harga: "))
                sertifikat = input("Sertifikat: ")
                njop = int(input("NJOP: "))
                luas = int(input("Luas: "))

                aset.nama = nama
                aset.harga = harga
                aset.sertifikat = sertifikat
                aset.njop = njop
                aset.luas = luas

                print("Aset berhasil diubah")


if __name__ == "__main__":
    app = AplikasiAsetManagement()
    app.run()
    print("selesai")
    # FIX: "cls" hanya berjalan di Windows, ditambahkan pengecekan OS
    os.system("cls" if os.name == "nt" else "clear")