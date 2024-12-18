import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menampilkan pola
def tampilkan_pola():
    huruf = entry_huruf.get()  # Ambil input huruf
    angka = entry_angka.get()  # Ambil input angka
    
    # Validasi input angka
    if not angka.isdigit():
        messagebox.showerror("Error", "Input angka harus berupa bilangan positif.")
        return
    
    angka = int(angka)
    if angka <= 0:
        messagebox.showerror("Error", "Input angka harus lebih dari 0.")
        return

    # Buat pola
    output_text.delete("1.0", tk.END)  # Bersihkan teks sebelumnya
    for i in range(1, angka + 1):
        output_text.insert(tk.END, huruf * i + "\n")

# Inisialisasi GUI
root = tk.Tk()
root.title("Program Logika")
root.geometry("400x400")

# Label dan Input untuk Huruf
label_huruf = tk.Label(root, text="HURUF", font=("Arial", 10))
label_huruf.grid(row=0, column=0, padx=10, pady=10)
entry_huruf = tk.Entry(root, width=5)
entry_huruf.grid(row=0, column=1, padx=10, pady=10)

# Label dan Input untuk Angka
label_angka = tk.Label(root, text="ANGKA", font=("Arial", 10))
label_angka.grid(row=0, column=2, padx=10, pady=10)
entry_angka = tk.Entry(root, width=5)
entry_angka.grid(row=0, column=3, padx=10, pady=10)

# Tombol OK
button_ok = tk.Button(root, text="OK", command=tampilkan_pola, width=10)
button_ok.grid(row=0, column=4, padx=10, pady=10)

# Output Text untuk menampilkan hasil
output_text = tk.Text(root, height=20, width=40, font=("Arial", 10))
output_text.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Menjalankan GUI
root.mainloop()
