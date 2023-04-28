import tkinter as tk

# Create main window
root = tk.Tk()

# Create 2D array
arr = [[0 for x in range(5)] for y in range(5)]


# Function to write array to binary file
def write_to_file(filename, arr):
    with open(filename, "wb") as f:
        for row in arr:
            f.write(bytearray(row))


# Function to read array from binary file
def read_from_file(filename):
    arr = []
    with open(filename, "rb") as f:
        while True:
            row = list(f.read(5))
            if not row:
                break
            arr.append(row)
    return arr


# Function to handle "Save" button press
def save():
    for i in range(5):
        for j in range(5):
            arr[i][j] = int(entries[i][j].get())
    write_to_file("array.bin", arr)


# Function to handle "Load" button press
def load():
    arr = read_from_file("array.bin")
    transposed_array = list(map(list, zip(*arr)))
    write_to_file("transposed_array.bin", transposed_array)
    for i in range(5):
        for j in range(5):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, transposed_array[i][j])


# Create input widgets
entries = [[tk.Entry(root, width=5) for x in range(5)] for y in range(5)]
for i in range(5):
    for j in range(5):
        entries[i][j].grid(row=i, column=j)

# Create "Save" and "Load" buttons
save_button = tk.Button(root, text="Save", command=save)
save_button.grid(row=6, column=0, columnspan=2)
load_button = tk.Button(root, text="Load", command=load)
load_button.grid(row=6, column=3, columnspan=2)

# Start main loop of program
root.mainloop()
