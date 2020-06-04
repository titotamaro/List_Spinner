list_awal = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] #akan diubah menjadi[3,6,9][2,5,8][1,4,7]

#[3,6,9] ==> setiap kolom selisih 3 angka
#[2,5,8]
#[1,4,7]

def counterClockwise (list_x): # fungsi counterClockwise untuk list_x
    hasil = [] # storage untuk penghitungan
    for i in range(1,len(list_x)+1): # jumlah baris
        for j in range(i,10,3): # isi kolom
           hasil.append(j)  # saat di run hasil masih terbalik [3,6,9] posisinya ada di bawah
    hasil = f"  {hasil[-3:]} '\n' {hasil[3:6]} '\n' {hasil[0:3]}"  # saya coba balik dengan slicing
    return hasil            
         

#Kalau yang diatas masih belum memuaskan saya coba bikin pakai lambda (semoga menambah nilai):
# def counterClockwise(list_x): # fungsi counterClockwise untuk list_x
#     a = map(lambda x: x*3 ,list_x[0]) # mengambil list pertama dan dikali 3 menggunakan map dan lambda
#     b = map(lambda x: x-1 , a) # mengambil list a dan dikurangi 1
#     c = map(lambda x: x-1, b) # mengambil list b dan dikurangi 1
#     return f" {[a]} \n {[b]} \n {[c]}" #return value sesuai output yg diinginkan soal

print(counterClockwise(list_awal)) # pemanggilan fungsi sesuai soal

#Created by Tito Tamaro