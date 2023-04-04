import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from matplotlib import pyplot as plt

_MAX_SIZE = (200, 200)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Procesamiento de imagenes")
        self.geometry("960x1080")
        self.resizable(False, False)
        self.preview_img = None  # Variable to handle a reference to selected Image. Without it, the image will not
        self.filepath = ""
        # appear

        main_frame = tk.Frame(self)
        main_frame.pack()

        # Frames
        title_frame = tk.Frame(main_frame)
        select_img_frame = tk.Frame(main_frame)
        process_img_option_frame = tk.Frame(main_frame)
        output_frame = tk.Frame(main_frame)

        # Packing the frames
        title_frame.pack()
        select_img_frame.pack()
        process_img_option_frame.pack()
        output_frame.pack()

        # Title frame elements
        label_title = tk.Label(title_frame, text="FrameForge", font=('Segoe UI', 30, 'bold'))
        label_title.pack(padx=10, pady=10)

        # Select_img_frame elements
        button_select_img = tk.Button(select_img_frame, text="Seleccionar imagen", font=('Segoe UI', 10),
                                      command=lambda: __open_browse_files())
        label_selected_img = tk.Label(select_img_frame)
        button_select_img.grid(row=0, column=0, padx=10, pady=10)
        label_selected_img.grid(row=0, column=1, padx=10, pady=10)

        # Process_img_option_frame elements
        button_ecualizar = tk.Button(process_img_option_frame, text="Ecualizar", font=('Segoe UI', 10), width=24)
        button_expandir = tk.Button(process_img_option_frame, text="Expandir", font=('Segoe UI', 10), width=24)
        button_ecualizar.grid(row=0, column=0, padx=10, pady=10)
        button_expandir.grid(row=0, column=1, padx=10, pady=10)

        def __open_browse_files():
            filepath = filedialog.askopenfilename(initialdir="/",
                                                  title="Select an image",
                                                  filetypes=[("Image files", ("*.jpg*", "*.png*", "*.jpeg*"))])
            self.filepath = filepath  # This is just for testing
            preview_img_loaded = Image.open(filepath)

            preview_img_loaded.thumbnail(_MAX_SIZE, Image.Resampling.LANCZOS)

            preview_img_loaded = preview_img_loaded.convert("L")

            self.preview_img = ImageTk.PhotoImage(preview_img_loaded)

            label_selected_img.config(image=self.preview_img)

            # Loading Histogram
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            hist = cv2.calcHist([img], [0], None, [256], [0, 256])
            plt.plot(hist, color='gray')
            plt.xlabel('Intensidad de gris')
            plt.ylabel('Cantidad de pixeles')
            plt.show()

