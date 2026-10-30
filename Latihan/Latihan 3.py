# PROGGRAM SEDERHANA DARI LIST
# LIST BUKU

list_buku = []
while True:
    print("\n masukan data buku")
    judul = input("Judul buku \t:")
    penulis = input("Penulis \t:")
    
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print("="*10,"DATA BUKU","="*10)
    
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("="*10,"="*10)
    Lanjut = input("Apakah dilanjutkan?9=(y/n)")
    
    if Lanjut == "y":
        continue
    
    elif Lanjut == "n":
        break
    else :
        print("ulangi lagi")
        break
        
    
print("=" * 5,"proggram selesai","=" * 5)