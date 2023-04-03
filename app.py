import tkinter
import tkinter as tk

class App(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title("Procesamiento de imagenes")
        self.geometry("600x700")
        self.resizable(0,0)

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
        button_select_img = tk.Button(select_img_frame, text="Seleccionar imagen", font=('Segoe UI', 10))
        button_select_img.grid(row=0, column=0, padx=10, pady=10)

        # Process_img_option_frame elements
        button_ecualizar = tk.Button(process_img_option_frame, text="Ecualizar", font=('Segoe UI', 10), width=24)
        button_expandir = tk.Button(process_img_option_frame, text="Expandir", font=('Segoe UI', 10), width=24)
        button_ecualizar.grid(row=0, column=0, padx=10, pady=10)
        button_expandir.grid(row=0, column=1, padx=10, pady=10)




