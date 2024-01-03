import tkinter as tk
from tkinter import messagebox

def hitung_diskon():
    hargaAwal = masukanHargaAwal.get()
    diskon = masukanDiskon.get()

    if hargaAwal and diskon:
        hargaAwal, diskon = int(hargaAwal.replace(".", "")), float(diskon)

        if 0 <= hargaAwal <= 1000000 and 0 <= diskon <= 100:
            hargaSetelahDiskon = hargaAwal * (1 - diskon / 100)
            hasil_label.config(text="Harga Setelah Diskon: Rp {:,.2f}".format(hargaSetelahDiskon))
        else:
            messagebox.showerror("Error", "Input tidak valid")
    else:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat GUI
app = tk.Tk()
app.title("Kalkulator Diskon (Rupiah)")
app.geometry('400x300')


# Fungsi untuk membuat Label dan Entry
def buat_label_dan_entry(teks):
    label = tk.Label(app, text=teks, pady='10')
    label.pack()

    entry = tk.Entry(app, width='30')
    entry.pack()

    return entry

# Label dan Entry untuk Harga Awal
masukanHargaAwal = buat_label_dan_entry("Harga Awal (Rp):")

# Label dan Entry untuk Persentase Diskon
masukanDiskon = buat_label_dan_entry("Diskon (%):")

# Tombol untuk Menghitung Diskon
hitung_button = tk.Button(app, text="Hitung Diskon", command=hitung_diskon)
hitung_button.pack()

# Label untuk Menampilkan Hasil
hasil_label = tk.Label(app, text="")
hasil_label.pack()

# Menjalankan aplikasi
app.mainloop()