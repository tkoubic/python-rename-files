import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk


def select_directory():
    folder_path.set(filedialog.askdirectory())


def rename_files():
    directory = folder_path.get()
    prefix = prefix_entry.get() if prefix_var.get() else ""

    if not directory or not os.path.isdir(directory):
        messagebox.showerror("Error", "Nebyla vybrána žádná složka.")
        return

    if prefix_var.get() and not prefix:
        messagebox.showerror("Error", "Nebyl vložen žádný prefix")
        return

    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for idx, filename in enumerate(files, start=1):
            old_file = os.path.join(directory, filename)
            file_extension = os.path.splitext(filename)[1]  # zachováme příponu souboru
            new_filename = f"{prefix} {idx}{file_extension}" if prefix else f"{idx}{file_extension}"
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
        messagebox.showinfo("Hotovo!", "Soubory úspěšně přejmenovány.")
    except Exception as e:
        messagebox.showerror("Chyba", str(e))


def toggle_prefix():
    if prefix_var.get():
        prefix_label.grid(row=2, column=0, padx=5, pady=5)
        prefix_entry.grid(row=2, column=1, padx=5, pady=5)
    else:
        prefix_label.grid_remove()
        prefix_entry.grid_remove()


def open_url():
    webbrowser.open("https://github.com/tkoubic")


# TKINTER MAIN
root = tk.Tk()

root.title("Hromadné přejmenování souborů")
root.resizable(False, False)
# Nastavení ikony okna (volitelné)
root.iconbitmap("iconn.ico")

# Cesta k adresáři
folder_path = tk.StringVar()
tk.Label(root,
         text="Soubory budou přejmenovány, podle celkového počtu souborů ve složce. Pokud zvolíte prefix, bude vložen před pořadové číslo souboru. ( prefix 1.jpg )",
         wraplength=380).grid(row=0, columnspan=4, padx=10, pady=10)
tk.Label(root, text="Složka:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=folder_path, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Vybrat složku", command=select_directory).grid(row=1, column=2, padx=5, pady=5)

# Zaškrtávací políčko pro prefix
prefix_var = tk.BooleanVar()
prefix_var.set(True)
tk.Checkbutton(root, text="Použít prefix", variable=prefix_var, command=toggle_prefix).grid(row=2, column=2, padx=5,
                                                                                         pady=5)

# Prefix pro nový název souboru
prefix_label = tk.Label(root, text="Prefix:")  # Musí být definováno před použitím
prefix_entry = tk.Entry(root, width=50)  # Musí být definováno před použitím
prefix_label.grid(row=2, column=0, padx=5, pady=5)
prefix_entry.grid(row=2, column=1, padx=5, pady=5)

# Tlačítko pro přejmenování souborů
tk.Button(root, text="Přejmenovat ", command=rename_files).grid(row=3, column=2, pady=10)

# Změna velikosti ikony
original_icon_image = Image.open("github.png")  
resized_icon_image = original_icon_image.resize((32, 32))
icon_image = ImageTk.PhotoImage(resized_icon_image)

# Přidání tlačítka s ikonou, které otevře URL v prohlížeči

tk.Button(root, image=icon_image, command=open_url).grid(row=3, column=0, pady=10)

# Spuštění hlavní smyčky Tkinter
root.mainloop()
