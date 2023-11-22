from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import messagebox


class Program(ABC):
    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def uninstall(self):
        pass


class Developer(ABC):
    @abstractmethod
    def write_code(self):
        pass

    @abstractmethod
    def test_code(self):
        pass


class OS(Program):
    def __init__(self, name='', version=''):
        self.name = name
        self.version = version

    def install(self):
        messagebox.showinfo('', f'Installing {self.name} version {self.version}')

    def uninstall(self):
        messagebox.showinfo('', f'Uninstalling {self.name} version {self.version}')

    def update(self):
        messagebox.showinfo('', f'Updating {self.name} to latest version')

    def boot(self):
        messagebox.showinfo('', f'Booting {self.name}')


class MobileApp(Program, Developer):
    def __init__(self, name='', version=''):
        self.name = name
        self.version = version

    def install(self):
        messagebox.showinfo('', f'Installing {self.name} version {self.version}')

    def uninstall(self):
        messagebox.showinfo('', f'Uninstalling {self.name} version {self.version}')

    def write_code(self):
        messagebox.showinfo('', f'Writing code for {self.name}')

    def test_code(self):
        messagebox.showinfo('', f'Testing code for {self.name}')

    def update(self):
        messagebox.showinfo('', f'Updating {self.name} to latest version')

    def launch(self):
        messagebox.showinfo('', f'Launching {self.name}')


class App:

    def __init__(self, master):
        self.master = master
        master.title("Tkinter GUI")

        self.os = OS()
        self.app = MobileApp()

        self.os_name_label = tk.Label(root, text="OS Name:")
        self.os_name_label.pack()

        self.os_name_entry = tk.Entry(root)
        self.os_name_entry.pack()

        self.os_version_label = tk.Label(root, text="OS Version:")
        self.os_version_label.pack()

        self.os_version_entry = tk.Entry(root)
        self.os_version_entry.pack()

        self.app_name_label = tk.Label(root, text="App Name:")
        self.app_name_label.pack()

        self.app_name_entry = tk.Entry(root)
        self.app_name_entry.pack()

        self.app_version_label = tk.Label(root, text="App Version:")
        self.app_version_label.pack()

        self.app_version_entry = tk.Entry(root)
        self.app_version_entry.pack()

        def create_os():
            self.os_name = self.os_name_entry.get()
            self.os_version = self.os_version_entry.get()
            self.os = OS(self.os_name, self.os_version)
            messagebox.showinfo(f"Created OS: {self.os.name} {self.os.version}")

        def create_app():
            self.app_name = self.app_name_entry.get()
            self.app_version = self.app_version_entry.get()
            self.app = MobileApp(self.app_name, self.app_version)
            messagebox.showinfo(f"Created App: {self.app.name} {self.app.version}")

        self.create_os_button = tk.Button(root, text="Create OS", command=create_os)
        self.create_os_button.pack()

        self.create_app_button = tk.Button(root, text="Create App", command=create_app)
        self.create_app_button.pack()

        self.os_install_button = tk.Button(master, text="Install OS", command=self.os.install)
        self.os_install_button.pack()

        self.os_uninstall_button = tk.Button(master, text="Uninstall OS", command=self.os.uninstall)
        self.os_uninstall_button.pack()

        self.os_update_button = tk.Button(master, text="Update OS", command=self.os.update)
        self.os_update_button.pack()

        self.os_boot_button = tk.Button(master, text="Boot OS", command=self.os.boot)
        self.os_boot_button.pack()

        self.app_install_button = tk.Button(master, text="Install App", command=self.app.install)
        self.app_install_button.pack()

        self.app_uninstall_button = tk.Button(master, text="Uninstall App", command=self.app.uninstall)
        self.app_uninstall_button.pack()

        self.app_write_code_button = tk.Button(master, text="Write App Code", command=self.app.write_code)
        self.app_write_code_button.pack()

        self.app_test_code_button = tk.Button(master, text="Test App Code", command=self.app.test_code)
        self.app_test_code_button.pack()

        self.app_update_button = tk.Button(master, text="Update App", command=self.app.update)
        self.app_update_button.pack()

        self.app_launch_button = tk.Button(master, text="Launch App", command=self.app.launch)
        self.app_launch_button.pack()


root = tk.Tk()
my_app = App(root)
root.mainloop()
