def hitung_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000

    total_biaya = tarif * durasi_parkir
    return total_biaya

print("=====================================")
print("        SISTEM BIAYA PARKIR          ") 
print("=====================================")

jenis_kendaraan = input("jenis kendaraan mobil/motor: ")
jam_masuk = int(input("jam masuk: "))
jam_keluar = int(input("jam keluar: "))

lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, lama_parkir)

print("\n========== HASIL PARKIR ============")
print("jenis kendaraan:", jenis_kendaraan)
print("jam masuk:", jam_masuk)
print("jam keluar:", jam_keluar)
print("lama parkir:", lama_parkir, "jam")
print("total biaya parkir: Rp", total_biaya)