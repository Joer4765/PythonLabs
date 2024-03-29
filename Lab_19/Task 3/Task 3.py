from tkinter import Tk, Canvas, Button, filedialog, Label, Entry, Listbox, END
from PIL import Image, ImageTk, ImageFilter, ImageOps


class ImageManipulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Manipulation App")

        # Canvas
        self.canvas = Canvas(root, bg="white", width=500, height=500)
        self.canvas.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.load_button.grid(row=1, column=0, pady=5)

        self.apply_filter_button = Button(root, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.grid(row=1, column=1, pady=5)

        self.rotate_button = Button(root, text="Rotate", command=self.rotate_image)
        self.rotate_button.grid(row=1, column=2, pady=5)

        self.crop_button = Button(root, text="Crop", command=self.crop_image)
        self.crop_button.grid(row=1, column=3, pady=5)

        self.resize_button = Button(root, text="Resize", command=self.resize_image)
        self.resize_button.grid(row=2, column=0, pady=5)

        self.mirror_button = Button(root, text="Mirror", command=self.mirror_image)
        self.mirror_button.grid(row=2, column=1, pady=5)

        self.overlay_button = Button(root, text="Overlay", command=self.overlay_images)
        self.overlay_button.grid(row=2, column=2, pady=5)

        self.save_button = Button(root, text="Save Image", command=self.save_image)
        self.save_button.grid(row=2, column=3, pady=5)

        # Labels and Entries
        self.rotation_label = Label(root, text="Enter Rotation Angle:")
        self.rotation_label.grid(row=3, column=0, pady=5)

        self.rotation_entry = Entry(root)
        self.rotation_entry.grid(row=3, column=1, pady=5)

        self.crop_label = Label(root, text="Enter Crop Coordinates (x1, y1, x2, y2):")
        self.crop_label.grid(row=3, column=2, pady=5)

        self.crop_entry = Entry(root)
        self.crop_entry.grid(row=3, column=3, pady=5)

        self.resize_label = Label(root, text="Enter Resize Dimensions (width, height):")
        self.resize_label.grid(row=4, column=0, pady=5)

        self.resize_entry = Entry(root)
        self.resize_entry.grid(row=4, column=1, pady=5)

        self.opacity_label = Label(root, text="Enter Opacity (0-255):")
        self.opacity_label.grid(row=4, column=2, pady=5)

        self.opacity_entry = Entry(root)
        self.opacity_entry.grid(row=4, column=3, pady=5)

        # Listboxes
        self.orientation_label = Label(root, text="Choose Orientation:")
        self.orientation_label.grid(row=5, column=0, pady=5)

        self.orientation_listbox = Listbox(root, selectmode="single", height=7)
        orientations = ["FLIP_LEFT_RIGHT", "FLIP_TOP_BOTTOM", "ROTATE_90", "ROTATE_180", "ROTATE_270", "TRANSPOSE",
                        "TRANSVERSE"]
        for orientation in orientations:
            self.orientation_listbox.insert(END, orientation)
        self.orientation_listbox.grid(row=5, column=1, pady=5)

        self.filter_label = Label(root, text="Choose Filter:")
        self.filter_label.grid(row=5, column=2, pady=5)

        self.filter_listbox = Listbox(root, selectmode="single", height=3)
        filters = ["BLUR", "CONTOUR", "DETAIL"]
        for filter_name in filters:
            self.filter_listbox.insert(END, filter_name)
        self.filter_listbox.grid(row=5, column=3, pady=5)

        # Info Label
        self.info_label = Label(root, text="File Information:")
        self.info_label.grid(row=6, column=0, columnspan=4, pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.show_image(self.original_image)
            self.display_file_info()

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
                self.display_file_info()
            except ValueError:
                print("Please enter a valid rotation angle.")

    def crop_image(self):
        if self.original_image:
            try:
                coordinates = [int(coord) for coord in self.crop_entry.get().split(",")]
                if len(coordinates) == 4:
                    cropped_image = self.original_image.crop(coordinates)
                    self.show_image(cropped_image)
                    self.display_file_info()
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
                    self.display_file_info()
                else:
                    print("Please enter two comma-separated dimensions.")
            except ValueError:
                print("Please enter valid numerical dimensions.")

    def mirror_image(self):
        if self.original_image:
            selected_index = self.orientation_listbox.curselection()
            if selected_index:
                orientation = self.orientation_listbox.get(selected_index)
                if orientation == "FLIP_LEFT_RIGHT":
                    mirrored_image = ImageOps.mirror(self.original_image)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "FLIP_TOP_BOTTOM":
                    mirrored_image = ImageOps.flip(self.original_image)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "ROTATE_90":
                    mirrored_image = self.original_image.transpose(Image.ROTATE_90)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "ROTATE_180":
                    mirrored_image = self.original_image.transpose(Image.ROTATE_180)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "ROTATE_270":
                    mirrored_image = self.original_image.transpose(Image.ROTATE_270)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "TRANSPOSE":
                    mirrored_image = self.original_image.transpose(Image.TRANSPOSE)
                    self.show_image(mirrored_image)
                    self.display_file_info()
                elif orientation == "TRANSVERSE":
                    mirrored_image = self.original_image.transpose(Image.TRANSVERSE)
                    self.show_image(mirrored_image)
                    self.display_file_info()

    def apply_filter(self):
        if self.original_image:
            selected_index = self.filter_listbox.curselection()
            if selected_index:
                filter_name = self.filter_listbox.get(selected_index)
                filtered_image = self.apply_selected_filter(filter_name)
                self.show_image(filtered_image)
                self.display_file_info()

    def apply_selected_filter(self, filter_name):
        if filter_name == "BLUR":
            return self.original_image.filter(ImageFilter.BLUR)
        elif filter_name == "CONTOUR":
            return self.original_image.filter(ImageFilter.CONTOUR)
        elif filter_name == "DETAIL":
            return self.original_image.filter(ImageFilter.DETAIL)

    def overlay_images(self):
        if self.original_image:
            overlay_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if overlay_path:
                overlay_image = Image.open(overlay_path)

                try:
                    opacity = int(self.opacity_entry.get())
                    if not (0 <= opacity <= 255):
                        raise ValueError("Opacity must be between 0 and 255.")
                except ValueError:
                    print("Please enter a valid opacity value (0-255).")
                    return

                overlay_image = overlay_image.resize(self.original_image.size)
                overlay_image = overlay_image.convert("RGBA")
                overlay_image.putalpha(opacity)

                result_image = Image.alpha_composite(self.original_image.convert("RGBA"), overlay_image)
                self.show_image(result_image)
                self.display_file_info()

    def display_file_info(self):
        if self.image_path:
            filename = self.image_path
            file_info = f"File Information:\nFilename: {filename}\nFormat: {self.original_image.format}\nMode: {self.original_image.mode}\nWidth: {self.original_image.width}\nHeight: {self.original_image.height}"
            self.info_label.config(text=file_info)

    def save_image(self):
        if self.current_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                     filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                                ("All files", "*.*")])
            if save_path:
                img_pil = ImageTk.getimage(self.current_image)
                img_pil.save(save_path)


if __name__ == "__main__":
    root = Tk()
    app = ImageManipulationApp(root)
    root.mainloop()
