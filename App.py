import tkinter as tk

current_color = "black"
brush_size = 2

def paint(event):
    """Draw a circle on the canvas."""
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)

def set_color(color):
    """Set the current drawing color."""
    global current_color
    current_color = color

def set_brush_size(size):
    """Set the current brush size."""
    global brush_size
    brush_size = size

# Create the main window
root = tk.Tk()
root.title("Basic Paint App")

# Create and place widgets
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(expand=True, fill=tk.BOTH)
canvas.bind("<B1-Motion>", paint)

frame_controls = tk.Frame(root)
frame_controls.pack()

colors = ["black", "red", "green", "blue", "yellow", "purple"]
for color in colors:
    button = tk.Button(frame_controls, bg=color, width=2, command=lambda c=color: set_color(c))
    button.pack(side=tk.LEFT)

frame_brush_sizes = tk.Frame(root)
frame_brush_sizes.pack()

for size in range(2, 11, 2):
    button = tk.Button(frame_brush_sizes, text=str(size), command=lambda s=size: set_brush_size(s))
    button.pack(side=tk.LEFT)

# Start the main loop
root.mainloop()
