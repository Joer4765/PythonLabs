import tkinter as tk


def show_month():
    m = int(entry.get())

    match (m % 12):

        case 0:
            month = 'January'
        case 1:
            month = 'February'
        case 2:
            month = 'March'
        case 3:
            month = 'April'
        case 4:
            month = 'May'
        case 5:
            month = 'June'
        case 6:
            month = 'July'
        case 7:
            month = 'August'
        case 8:
            month = 'September'
        case 9:
            month = 'October'
        case 10:
            month = 'November'
        case 11:
            month = 'December'
        case _:
            month = 'Invalid month'

    result_label.config(text=month)


# Create the main Tkinter window
root = tk.Tk()
root.title('Month Finder')

# Create and place an Entry widget for user input
entry = tk.Entry(root, width=10)
entry.pack(pady=10)

# Create a Button widget to trigger the month calculation
button = tk.Button(root, text='Find Month', command=show_month)
button.pack(pady=10)

# Create a Label widget to display the result
result_label = tk.Label(root, text='')
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

