from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, Label, Entry
from PIL import Image, ImageTk


class ImageManipulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Manipulation App")

        self.canvas = Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack()

        self.image_path = None
        self.original_image = None
        self.current_image = None

        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.rotation_label = Label(root, text="Enter Rotation Angle:")
        self.rotation_label.pack()

        self.rotation_entry = Entry(root)
        self.rotation_entry.pack()

        self.rotate_button = Button(root, text="Rotate", command=self.rotate_image)
        self.rotate_button.pack()

        self.overlay_button = Button(root, text="Overlay", command=self.overlay_images)
        self.overlay_button.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.show_image(self.original_image)

    def show_image(self, image):
        image = ImageTk.PhotoImage(image)
        self.current_image = image
        self.canvas.config(width=image.width(), height=image.height())
        self.canvas.create_image(0, 0, anchor="nw", image=image)

    def rotate_image(self):
        if self.original_image:
            try:
                angle = float(self.rotation_entry.get())
                rotated_image = self.original_image.rotate(angle)
                self.show_image(rotated_image)
            except ValueError:
                print("Please enter a valid rotation angle.")

    def overlay_images(self):
        if self.original_image:
            overlay_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if overlay_path:
                overlay_image = Image.open(overlay_path)
                overlay_image = overlay_image.resize(self.original_image.size)
                result_image = Image.alpha_composite(self.original_image.convert("RGBA"), overlay_image.convert("RGBA"))
                self.show_image(result_image)


if __name__ == "__main__":
    root = Tk()
    app = ImageManipulationApp(root)
    root.mainloop()
