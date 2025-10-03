import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import struct

class DarknessV4:
    def __init__(self, root):
        self.root = root
        self.root.title("DarknessV4 - SM64 ROM Manager")
        self.rom = None

        # Menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open ROM", command=self.open_rom)
        filemenu.add_command(label="Save ROM", command=self.save_rom)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Tabs
        self.notebook = ttk.Notebook(root)
        self.tab_levels = ttk.Frame(self.notebook)
        self.tab_textures = ttk.Frame(self.notebook)
        self.tab_patches = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_levels, text="Levels")
        self.notebook.add(self.tab_textures, text="Textures")
        self.notebook.add(self.tab_patches, text="Patches")
        self.notebook.pack(fill="both", expand=True)

        # Treeview for Levels
        self.level_tree = ttk.Treeview(self.tab_levels, columns=("offset","segment"))
        self.level_tree.heading("#0", text="Level")
        self.level_tree.heading("offset", text="Offset")
        self.level_tree.heading("segment", text="Segment")
        self.level_tree.pack(fill="both", expand=True)

    def open_rom(self):
        path = filedialog.askopenfilename(filetypes=[("N64 ROM","*.z64")])
        if not path: return
        with open(path,"rb") as f:
            self.rom = bytearray(f.read())

        # Parse header
        title = self.rom[0x20:0x34].decode("ascii","ignore").strip()
        messagebox.showinfo("ROM Loaded", f"Game Title: {title}")

        # Example: Add BOB entry (placeholder)
        self.level_tree.insert("", "end", text="Bob-omb Battlefield", values=("0x123456","0x0E"))

    def save_rom(self):
        if not self.rom:
            messagebox.showerror("Error","No ROM loaded!")
            return
        path = filedialog.asksaveasfilename(defaultextension=".z64")
        if not path: return
        with open(path,"wb") as f:
            f.write(self.rom)
        messagebox.showinfo("Saved","ROM saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    DarknessV4(root)
    root.mainloop()
