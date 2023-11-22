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

        self.crop_label = Label(root, text="Enter Crop Coordinates (x1, y1, x2, y2):")
        self.crop_label.pack()

        self.crop_entry = Entry(root)
        self.crop_entry.pack()

        self.resize_label = Label(root, text="Enter Resize Dimensions (width, height):")
        self.resize_label.pack()

        self.resize_entry = Entry(root)
        self.resize_entry.pack()

        self.rotate_button = Button(root, text="Rotate", command=self.rotate_image)
        self.rotate_button.pack()

        self.crop_button = Button(root, text="Crop", command=self.crop_image)
        self.crop_button.pack()

        self.resize_button = Button(root, text="Resize", command=self.resize_image)
        self.resize_button.pack()

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

    def crop_image(self):
        if self.original_image:
            try:
                coordinates = [int(coord) for coord in self.crop_entry.get().split(",")]
                if len(coordinates) == 4:
                    cropped_image = self.original_image.crop(coordinates)
                    self.show_image(cropped_image)
                else:
                    print("Please enter four comma-separated coordinates.")
            except ValueError:
                print("Please enter valid numerical coordinates.")

    def resize_image(self):
        if self.original_image:
            try:
                dimensions = [int(dimension) for dimension in self.resize_entry.get().split(",")]
                if len(dimensions) == 2:
                    resized_image = self.original_image.resize((dimensions[0], dimensions[1]))
                    self.show_image(resized_image)
                else:
                    print("Please enter two comma-separated dimensions.")
            except ValueError:
                print("Please enter valid numerical dimensions.")

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
