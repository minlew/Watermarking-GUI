import tkinter as tk
from tkinter import filedialog as fido
from PIL import Image, ImageTk

# Color palette hex codes
DARK_BLUE = "#7286D3"
MEDIUM_BLUE = "#8EA7E9"
LAVENDER = "#E5E0FF"
BEIGE = "#FFF2F2"


# When using canvas.create_image within a function, Python automatically deletes the references to the variable by a
# process known as Garbage Collection. The solution is to save the reference or to create a new reference.
# This is why I created this global list.
image_list = []

# Match global variable to initial canvas size. Change within functions in order to resize.
canvas_width = 600
canvas_height = 600


def choose_image():
    global canvas_width, canvas_height
    chosen_image_filepath = fido.askopenfilename(title="Pick your image")
    if chosen_image_filepath:
        canvas.delete("all")
        my_image = tk.PhotoImage(file=chosen_image_filepath)
        canvas_width, canvas_height = my_image.width(), my_image.height()
        image_list.append(my_image)  # Save the reference to the image in order to avoid garbage collection.
        canvas.config(width=canvas_width, height=canvas_height)
        canvas.create_image(0, 0, image=my_image, anchor=tk.NW)


def apply_watermark():
    global canvas_width, canvas_height
    image = Image.open("watermark.png")
    image = image.resize((canvas_width, canvas_height))
    watermark_image = ImageTk.PhotoImage(image)  # Convert image to photo image before putting on canvas.
    image_list.append(watermark_image)
    canvas.create_image(0, 0, image=watermark_image, anchor=tk.NW)


def save_and_quit():
    canvas.postscript(file="output.eps", colormode="color")
    saved_image = Image.open("output.eps")
    saved_image.save("output.png", "png")
    window.quit()


window = tk.Tk()
window.title("Watermarking App")
window.config(padx=50, pady=50, bg=BEIGE, highlightthickness=0)

canvas = tk.Canvas(width=600, height=600, bg=BEIGE, highlightthickness=0)
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(300, 300, image=logo_image)
canvas.create_text(300, 300, text="Watermarker App!", fill=LAVENDER, font=("Courier", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=3)


image_button = tk.Button(text="Choose Image", bg="white", highlightthickness=0, command=choose_image)
image_button.grid(row=1, column=0)

watermarking_button = tk.Button(text="Apply Watermark", bg="white", highlightthickness=0, command=apply_watermark)
watermarking_button.grid(row=1, column=1)

save_button = tk.Button(text="Save Image", bg="white", highlightthickness=0, command=save_and_quit)
save_button.grid(row=1, column=2)

window.update()
window.mainloop()
