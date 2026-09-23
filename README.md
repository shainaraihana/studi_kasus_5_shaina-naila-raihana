# studi_kasus_5_shaina-naila-raihana

Nama: Shaina Naila Raihana

NIM: 2609116090

# PENJELASAN PROGRAM

# 1. Function 

<img width="381" height="16" alt="Screenshot 2026-09-23 101629" src="https://github.com/user-attachments/assets/4ff0d14b-d2e3-4b23-9faf-e714ca8a7636" />

def digunakan untuk membuat function

nama function nya adalah

hitung_biaya_parkir

di dalam kurung ada 2 parameter:

- jenis_kendaraan = menyimpan jenis kendaraan, yaitu mobil atau motor
- durasi_parkir = menyimpan berapa jam kendaraan

jadi function ini tugasnya menghitung biaya parkir berdasarkan jenis kendaraan dan lama parkir.

# 2. mengecek jenis kendaraan 

<img width="254" height="27" alt="Screenshot 2026-09-23 101653" src="https://github.com/user-attachments/assets/1dfdb35e-d4ba-454a-8342-3449e076c316" />

if digunakan untuk membuat kondisi.

== artinya membandingkan apakah nilainya sama dengan.

jadi kalau jenis_kendaraan diisi "mobil", maka:

<img width="152" height="15" alt="Screenshot 2026-09-23 111602" src="https://github.com/user-attachments/assets/266d74ad-031a-4500-818f-2a7d19f8772e" />

artinya tarif parkir mobil adalah Rp. 5000 per jam

# 3. kalau kendaraan motor 

<img width="254" height="29" alt="Screenshot 2026-09-23 101801" src="https://github.com/user-attachments/assets/cdf0c4a7-d54e-478c-87c4-89bf752d4e34" />

elif adalah kondisi tambahan setelah if

kalau jenis kendaraan bukan mobil, program mengecek apakah kendaraan tersebut "motor".

kalau iya:

<img width="153" height="13" alt="Screenshot 2026-09-23 112227" src="https://github.com/user-attachments/assets/912025bf-1e74-40e5-8c39-38799d5c27fa" />

artinya tarif motor adalah Rp.3000 per jam

# 4. menghitung total biaya

<img width="280" height="11" alt="Screenshot 2026-09-23 101828" src="https://github.com/user-attachments/assets/19a42914-8816-44e7-afa5-4ab0cb669114" />

disini program menghitung:

tarif x lama parkir

misalnya:

- kendaraan = mobil
- tarif = 5000
- lama parkir = 3 jam

maka:

5000 x 3 = 15000

jadi total_biaya adalah 15000

# 5. mengembalikan hasil function

<img width="181" height="21" alt="Screenshot 2026-09-23 101842" src="https://github.com/user-attachments/assets/d83348d4-572f-47b1-bbc0-80a21940c4f2" />

return digunakan untuk mengembalikan hasil dari function

jadi setelah biaya selesai dihitung, hasilnya dikirim kembali ke bagian program yang memanggil function tersebut.

# bagian tampilan program

<img width="314" height="44" alt="Screenshot 2026-09-23 101905" src="https://github.com/user-attachments/assets/289b996f-6143-4fb3-af0c-b9c5ea896169" />

print() digunakan untuk menampilkan sesuatu ke layar.

tiga baris ini hanya digunakan untuk membuat tampilan judul program supaya lebih rapi.

# 6. Meminta jenis kendaraan

<img width="370" height="17" alt="Screenshot 2026-09-23 101924" src="https://github.com/user-attachments/assets/f4675a9b-616b-42f2-858a-7c80cb1dd883" />

input() digunakan untuk menerima input dari pengguna.

# 7. input jam masuk

<img width="256" height="19" alt="Screenshot 2026-09-23 101948" src="https://github.com/user-attachments/assets/da7d0e41-d9d2-42d8-af07-5b64a7c5de20" />

meminta pengguna memasukkan jenis kendaraan dan menyimpannya ke variabel jenis_kendaraan.

# 8. Input jam keluar

<img width="269" height="13" alt="Screenshot 2026-09-23 102004" src="https://github.com/user-attachments/assets/fd54e30f-76c7-4b3a-a9cd-e7e387fa55cf" />

meminta pengguna memasukkan jam keluar dan mengubahnya menjadi bilangan bulat.

# 9. Menghitung durasi

<img width="249" height="20" alt="Screenshot 2026-09-23 102022" src="https://github.com/user-attachments/assets/10cabfe9-02f8-4c8a-ae47-3ce9206c4865" />

Menghitung lama parkir dengan mengurangi jam masuk dari jam keluar.

# 10. Memanggil function

<img width="406" height="14" alt="Screenshot 2026-09-23 102041" src="https://github.com/user-attachments/assets/e1171e92-06ed-4d4d-a223-8c7376a39b54" />

memanggil function hitung_biaya_parkir dengan memasukkan jenis kendaraan dan lama parkir. hasilnya disimpan dalam total_biaya.

# 11.  Menampilkan bagian hasil

<img width="314" height="15" alt="Screenshot 2026-09-23 102102" src="https://github.com/user-attachments/assets/31b1271b-70bd-4730-b2c3-9078f78a71f7" />

Menampilkan judul bagian hasil. \n digunakan untuk membuat baris baru.

# 12. Menampilkan jenis kendaraan

<img width="283" height="14" alt="Screenshot 2026-09-23 102139" src="https://github.com/user-attachments/assets/9a2c7fc5-79d1-4d75-b637-5a046d305756" />

Menampilkan jenis kendaraan yang telah dimasukkan.

# 13. Menampilkan jam masuk

<img width="215" height="13" alt="Screenshot 2026-09-23 102203" src="https://github.com/user-attachments/assets/f5de51c9-8209-4e17-864f-93ffbd71b7cc" />

Menampilkan jam masuk kendaraan.

# 14. Menampilkan jam keluar

<img width="221" height="14" alt="Screenshot 2026-09-23 102234" src="https://github.com/user-attachments/assets/dfe9eba4-938c-41f5-82cb-b6f0672151ef" />

Menampilkan jam keluar kendaraan

# 15. Menampilkan lama parkir

<img width="271" height="11" alt="Screenshot 2026-09-23 102248" src="https://github.com/user-attachments/assets/52f677c3-05d5-4f4b-a578-3350962631f5" />

Menampilkan lama kendaraan berada di tempat parkir.

# 16. Menampilkan total biaya

<img width="292" height="16" alt="Screenshot 2026-09-23 102352" src="https://github.com/user-attachments/assets/a4ac90bc-6e55-466a-a751-d96864abc19c" />

Menampilkan total biaya parkir yang sudah dihitung oleh function.

# OUTPUT

OUTPUT MOBIL

<img width="358" height="174" alt="Screenshot 2026-09-23 122946" src="https://github.com/user-attachments/assets/f4fbe350-fcf1-4621-9ec6-8cb2f0fd9d56" />

OUTPUT MOTOR

<img width="391" height="194" alt="Screenshot 2026-09-23 123002" src="https://github.com/user-attachments/assets/a46af7ad-f53a-4402-b386-050120e70e30" />
