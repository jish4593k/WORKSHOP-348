from tkinter import *
from PIL import Image, ImageDraw

canvas_width = 600
canvas_height = 600
brush_size = 10


img = Image.new("L", (canvas_width, canvas_height), 255)
img_draw = ImageDraw.Draw(img)

def paint(event):

    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    color = "black"

    c.create_oval(x1, y1, x2, y2, fill=color, outline=color)  # Tkinter canvas
    img_draw.ellipse([(x1, y1), (x2, y2)], fill=color, outline=color)  # PIL parallel

def clear_canvas():

    c.delete("all")
    img_draw.rectangle([(0, 0), (canvas_width, canvas_height)], fill=255, outline=255)

def save_image():

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)

# Set up tkinter components
root = Tk()
root.resizable(False, False)
root.title("Simple Drawing App")

c = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
c.pack(expand=YES, fill=BOTH)
c.bind('<B1-Motion>', paint)

clear_btn = Button(root, text="Clear Canvas", command=clear_canvas)
clear_btn.pack(side=LEFT)

save_btn = Button(root, text="Save Image", command=save_image)
save_btn.pack(side=RIGHT)

root.mainloop()
