import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

_MAX_SIZE = (200, 200)
_ALPHA = 1.5
_BETA = 10

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Procesamiento de imagenes")
        self.geometry("960x720")
        self.resizable(False, False)
        self.preview_img = None  # Variable to handle a reference to selected Image. Without it, the image will not
        # appear
        self.output_img = None
        self.filepath = ""
        self.img_to_process = None

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
        button_ecualizar = tk.Button(process_img_option_frame, text="Ecualizar", font=('Segoe UI', 10), width=24,
                                     command=lambda: __equalization_image())
        button_expandir = tk.Button(process_img_option_frame, text="Expandir", font=('Segoe UI', 10), width=24,
                                    command=lambda: __expand_image())
        button_ecualizar.grid(row=0, column=0, padx=10, pady=10)
        button_expandir.grid(row=0, column=1, padx=10, pady=10)

        # output_frame elements
        label_output_image = tk.Label(output_frame)
        label_output_image.grid(row=0, column=0, padx=10, pady=10)

        def __verify_selected_image() -> bool:
            if self.img_to_process is None:
                messagebox.showerror(message="Debe de seleccionar una imagen", title="Imagen no seleccionada")
                return False
            else:
                return True

        def __embed_histogram_plot_to_tkinter(img, frame: tk.Frame, _row: int, _column: int) -> None:

            histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

            # Making the plot for the histogram
            figure = Figure(dpi=50)
            axis = figure.add_subplot(111)
            axis.plot(histogram, color='gray')

            # Embedding plot of matplotlib to Tk
            canvas = FigureCanvasTkAgg(figure, frame)
            canvas.get_tk_widget().grid(row=_row, column=_column, padx=10, pady=10)

        def __embed_img_to_tkinter(img) -> None:
            im = Image.fromarray(img)
            im.thumbnail(_MAX_SIZE, Image.Resampling.LANCZOS)
            self.output_img = ImageTk.PhotoImage(image=im)
            label_output_image.config(image=self.output_img)

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

            self.img_to_process = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

            __embed_histogram_plot_to_tkinter(self.img_to_process, select_img_frame, 0, 2)

        def __equalization_image():
            if __verify_selected_image() is not True:
                return None

            img = cv2.equalizeHist(self.img_to_process)
            __embed_histogram_plot_to_tkinter(img, output_frame, 0, 1)
            __embed_img_to_tkinter(img)

        def __expand_image():
            if __verify_selected_image() is not True:
                return None

            img = cv2.convertScaleAbs(self.img_to_process, alpha=_ALPHA, beta=_BETA)
            __embed_histogram_plot_to_tkinter(img, output_frame, 0, 1)
            __embed_img_to_tkinter(img)
