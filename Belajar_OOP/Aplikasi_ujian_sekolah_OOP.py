import random

class Soal:
    def __init__(self,pertanyaan,jawaban,jawaban_benar):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban
        self.jawaban_benar = jawaban_benar
        
        random.shuffle(self.jawaban)
    
    def cek_jawaban(self,jawaban_user):
        return jawaban_user == self.jawaban_benar
    
class SoalUjian:
    def __init__(self,soal_asli):
        self.daftar_soal = []
        
        random.shuffle(soal_asli)
        for i in range(50):
            soal = soal_asli[i]
            data = soal.split("|")
            
            pertanyaan = data[0]
            semua_jawaban = data[1]
            
            jawaban= semua_jawaban.split(",")
            jawaban_benar = jawaban[0]
            
            soal = Soal(pertanyaan,jawaban,jawaban_benar)
            self.daftar_soal.append(soal)
            
class Siswa:
    def __init__(self,nama):
        self.nama = nama
        self.jawaban_benar = 0
        self.jawaban_salah = 0
    def tambah_benar (self):
        self.jawaban_benar += 1
        
    def tambah_salah(self):
        self.jawaban_salah += 1
    
    def hitung_skor(self):
        total = self.jawaban_benar + self.jawaban_salah
        if total == 0:
            return 0 
        return self.jawaban_benar / total * 100
    
    def simpan_riwayat(self,file_riwayat="riwayat_nilai.txt"):
        skor = self.hitung_skor()
        with open(file_riwayat, "a") as file:
            file.write(f"{self.nama},{self.jawaban_benar},{self.jawaban_salah},{skor:.2f}\n")


class AplikasiUjianSekolah:
    def __init__(self,file_soal):
        soal_asli = []
        try:
            with open(file_soal, "r") as file:
                for line in file:
                    soal_asli.append(line.strip())
        except FileNotFoundError:
            print(f"dile {file_soal} tidak ditemukan")
            soal_asli = []
        self.soal_ujian = SoalUjian(soal_asli)
        
    def run(self):
        opsi = ["A","B","C","D"]
        
        nama_siswa = input("masukan nama kamu :").strip
        siswa = Siswa(nama_siswa)
        
        for i in range(len(self.soal_ujian.daftar_soal)):
            soal = self.soal_ujian.daftar_soal[i]
            print("Pertanyaan", i + 1, ":", soal.pertanyaan)
            print("Jawaban:")

            for j in range(len(soal.jawaban)):
                jawaban = soal.jawaban[j]
                print(opsi[j], ".", jawaban)
                
            jawaban_user = input("pilih jawaban (A/B/C/D) :").strip().upper()
            while jawaban_user not in opsi:
                print("input tidak valid silahkan pilih A/B/C/D")
                jawaban_user = input("pilih jawaban A/B/C/D : ").strip().upper()
            jawaban_user_index = opsi.index(jawaban_user)
            jawaban_asli_user = soal.jawaban[jawaban_user_index]
            
            
            if soal.cek_jawaban(jawaban_asli_user):
                print("jawaban benar")
                siswa.tambah_benar()
            else:
                print("jawaban salah")
                siswa.tambah_salah()
                
        print()
        print("Hasil Ujian")
        print("Nama",siswa.nama)
        print("Jawaban benar",siswa.jawaban_benar)
        print("Jawaban benar",siswa.jawaban_salah)
        print("Hasil ujian",siswa.hitung_skor(),"%")
        
        siswa.simpan_riwayat()
        print("Riwayat nilai tersimpan!")
if __name__ == "__main__":
    app = AplikasiUjianSekolah("bank_soal.txt")
    app.run()
    print("selesai")