import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrollable Whiteboard")

        # Initialize attributes
        self.canvas = tk.Canvas(root, bg='white', scrollregion=(0, 0, 6000, 6000))
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Add scrollbars
        self.hbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.hbar.grid(row=1, column=0, sticky='we')
        self.vbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.vbar.grid(row=0, column=1, sticky='ns')

        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # Tool icons (placeholders for actual icon images)
        self.pencil_icon = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Programing\Project\Advance Digital White Board\Logo\pencile1.png")
        self.eraser_icon = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Programing\Project\Advance Digital White board\Logo\erasser.png")
        self.clear_icon  = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Programing\Project\Advance Digital White board\Logo\clear_all.png")
        self.image_icon  = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Programing\Project\Advance Digital White board\Logo\add_image.png")
        self.color_icon  = tk.PhotoImage(file=r"C:\Users\Binit Shaw\Desktop\Programing\Project\Advance Digital White board\Logo\color.png")

        # Add toolbar with icon buttons
        self.toolbar = tk.Frame(root)
        self.toolbar.grid(row=2, column=0, columnspan=2, sticky='we')

        self.pencil_button = tk.Button(self.toolbar, image=self.pencil_icon, command=self.use_pencil)
        self.pencil_button.grid(row=0, column=0)

        self.eraser_button = tk.Button(self.toolbar, image=self.eraser_icon, command=self.use_eraser)
        self.eraser_button.grid(row=0, column=1)

        self.color_button = tk.Button(self.toolbar, image=self.color_icon, command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.clear_button = tk.Button(self.toolbar, image=self.clear_icon, command=self.clear_canvas)
        self.clear_button.grid(row=0, column=3)

        self.image_button = tk.Button(self.toolbar, image=self.image_icon, command=self.add_image)
        self.image_button.grid(row=0, column=4)

        # Add pencil size slider
        self.pencil_size_slider = tk.Scale(self.toolbar, from_=1, to=100, orient=tk.HORIZONTAL, label="Size")
        self.pencil_size_slider.set(2)
        self.pencil_size_slider.grid(row=0, column=5)

        # Default tool settings
        self.current_tool = "pencil"
        self.eraser_active = False
        self.color = "black"
        self.line_width = 5
        self.last_x, self.last_y = None, None
        self.current_image = None
        self.image_moving = False  # Flag to track image movement
        self.image_coords = None  # Store image coordinates for detection

        # Bind canvas events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Use platform-independent scrolling
        self.canvas.bind("<MouseWheel>", self.scroll_canvas)  # For Windows
        self.canvas.bind("<Button-4>", self.scroll_canvas)  # For Linux (scroll up)
        self.canvas.bind("<Button-5>", self.scroll_canvas)  # For Linux (scroll down)

    def use_pencil(self):
        self.current_tool = "pencil"
        self.canvas.config(cursor="pencil")

        # Disable image movement when pencil tool is active
        if self.current_image:
            self.canvas.tag_unbind(self.current_image, "<ButtonPress-1>")
            self.canvas.tag_unbind(self.current_image, "<B1-Motion>")

    def use_eraser(self):
        self.current_tool = "eraser"
        self.canvas.config(cursor="circle")

        # If an image is present, bind events for moving the image
        if self.current_image:
            self.canvas.tag_bind(self.current_image, "<ButtonPress-1>", self.start_image_move)
            self.canvas.tag_bind(self.current_image, "<B1-Motion>", self.move_image)
            self.canvas.tag_bind(self.current_image, "<ButtonRelease-1>", self.stop_image_move)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.current_image = None  # Clear image as well

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((700, 700))  # Resize the image for the canvas
            self.img_tk = ImageTk.PhotoImage(img)
            self.current_image = self.canvas.create_image(100, 100, image=self.img_tk, anchor="nw")

            # Get image coordinates for detection
            self.image_coords = self.canvas.bbox(self.current_image)

            # Bind events for moving the image only if eraser is selected
            if self.current_tool == "eraser":
                self.canvas.tag_bind(self.current_image, "<ButtonPress-1>", self.start_image_move)
                self.canvas.tag_bind(self.current_image, "<B1-Motion>", self.move_image)
                self.canvas.tag_bind(self.current_image, "<ButtonRelease-1>", self.stop_image_move)

    def start_image_move(self, event):
        self.image_moving = True

    def move_image(self, event):
        if self.image_moving and self.current_image:
            self.canvas.coords(self.current_image, event.x, event.y)
            self.image_coords = self.canvas.bbox(self.current_image)  # Update image coordinates

    def stop_image_move(self, event):
        self.image_moving = False

    def paint(self, event):
        if self.image_moving:
            return  # Prevent drawing while moving the image

        # Convert window coordinates to canvas coordinates (account for scrolling)
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)

        # Determine if the cursor is over the image
        cursor_over_image = self.is_cursor_over_image(canvas_x, canvas_y)

        if self.current_tool == "pencil":
            color = self.color
        elif self.current_tool == "eraser":
            if cursor_over_image:
                return  # Do not erase, just allow moving the image
            else:
                color = "white"  # Erase on the canvas

        self.line_width = self.pencil_size_slider.get()  # Get the current pencil size from slider

        if self.last_x and self.last_y:
            # Draw on the canvas (or erase depending on tool)
            self.canvas.create_line(self.last_x, self.last_y, canvas_x, canvas_y,
                                    width=self.line_width, fill=color, capstyle=tk.ROUND, smooth=True)

        self.last_x, self.last_y = canvas_x, canvas_y

    def reset(self, event):
        # Reset the drawing coordinates after the mouse is released
        self.last_x, self.last_y = None, None

    def scroll_canvas(self, event):
        # Scroll the canvas based on mouse wheel actions
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")  # Scroll up
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")  # Scroll down

    def is_cursor_over_image(self, x, y):
        """Check if the cursor is over the image."""
        if self.current_image and self.image_coords:
            x1, y1, x2, y2 = self.image_coords  # Image bounding box
            return x1 <= x <= x2 and y1 <= y <= y2
        return False


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    # Expand canvas on window resize
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    app = WhiteboardApp(root)
    root.mainloop()
