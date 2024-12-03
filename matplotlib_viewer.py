import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import pickle

class PlotUnpicklerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matplotlib Figure Unpickler")

        self.load_button = tk.Button(root, text="Load .pkl Files", command=self.load_files)
        self.load_button.pack(pady=5)

        self.plot_button = tk.Button(root, text="Run Plotter", command=self.plot_files)
        self.plot_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=5)

        self.pkl_files = []

    def load_files(self):
        self.pkl_files = filedialog.askopenfilenames(title="Select .pkl Files", filetypes=[("Pickle Files", "*.pkl")])
        if self.pkl_files:
            messagebox.showinfo("Files Selected", f"Selected files:\n{self.pkl_files}")
        else:
            messagebox.showwarning("No Files Selected", "No files were selected.")

    def plot_files(self):
        if not self.pkl_files:
            messagebox.showwarning("No Files", "No .pkl files loaded. Please load files first.")
            return

        for file in self.pkl_files:
            with open(file, 'rb') as f:
                fig = pickle.load(f)
                fig.show()

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlotUnpicklerApp(root)
    root.mainloop()
