import tkinter as tk
from tkinter import colorchooser

class ShapeDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAD App")

        # Initialize variables
        self.color = "#000000"
        self.fill_color = ""  # Default no fill
        self.eraser_mode = False
        self.shape_var = tk.StringVar()  # Variable to store selected shape
        self.shape_var.set("line")  # Default shape is line

        self.create_menu()
        self.create_toolbar()
        self.create_canvas()

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.start_x = None
        self.start_y = None

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="black")
        toolbar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(toolbar, text="Line", command=lambda: self.set_shape("line"), bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)
        tk.Button(toolbar, text="Rectangle", command=lambda: self.set_shape("rectangle"), bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)
        tk.Button(toolbar, text="Oval", command=lambda: self.set_shape("oval"), bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)
        tk.Button(toolbar, text="Eraser", command=self.set_eraser, bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)
        tk.Button(toolbar, text="Fill Color", command=self.choose_fill_color, bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)
        tk.Button(toolbar, text="Clear", command=self.clear_canvas, bg="white", fg="black").pack(side=tk.TOP, padx=2, pady=2, fill=tk.X)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", width=1980, height=1080)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def set_shape(self, shape):
        self.shape_var.set(shape)
        self.eraser_mode = False

    def set_color(self, color):
        self.color = color
        self.eraser_mode = False

    def set_eraser(self):
        self.eraser_mode = True

    def choose_fill_color(self):
        color_code = colorchooser.askcolor(title="Choose fill color")
        if color_code:
            self.fill_color = color_code[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        self.canvas.delete("preview")
        if self.eraser_mode:
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.canvas["bg"], width=10)
            self.start_x, self.start_y = event.x, event.y
        else:
            shape = self.shape_var.get()  # Get selected shape
            if shape == "line":
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, tags="preview")
            elif shape == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, fill=self.fill_color, tags="preview")
            elif shape == "oval":
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color, fill=self.fill_color, tags="preview")

    def on_release(self, event):
        if self.eraser_mode:
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.canvas["bg"], width=10)
        else:
            shape = self.shape_var.get()  # Get selected shape
            if shape == "line":
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color)
            elif shape == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, fill=self.fill_color)
            elif shape == "oval":
                self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color, fill=self.fill_color)
        self.start_x = None
        self.start_y = None
        self.canvas.delete("preview")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawingApp(root)
    root.mainloop()
