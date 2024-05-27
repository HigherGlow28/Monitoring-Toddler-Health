import tkinter as tk
from tkinter import messagebox

def cek_kesehatan_balita():
    try:
        umur = float(entry_umur.get())
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get())
        
        if umur < 1 or umur > 5:
            messagebox.showerror("Error", "Umur tersebut bukan balita")
        else:
            imt = berat / (tinggi ** 2)
            if imt < 18.5:
                hasil = "Gizi Buruk"
            elif 18.5 <= imt <= 24.9:
                hasil = "Normal"
            else:
                hasil = "Obesitas"
            
            messagebox.showinfo("Hasil", f"IMT: {imt:.2f}\nStatus: {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Setup GUI
root = tk.Tk()
root.title("Cek Kesehatan Balita")

tk.Label(root, text="Umur (tahun):").grid(row=0, column=0, padx=10, pady=10)
entry_umur = tk.Entry(root)
entry_umur.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Berat (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_berat = tk.Entry(root)
entry_berat.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Tinggi (m):").grid(row=2, column=0, padx=10, pady=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Cek Kesehatan", command=cek_kesehatan_balita).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()