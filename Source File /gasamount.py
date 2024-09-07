import tkinter as tk

def multiply_values():
    try:
        # Get values from entries and convert them to floats
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        # Calculate the product
        product = value1 * value2
        # Display the result
        result_label.config(text=f"Result: {product}")
    except ValueError:
        # Handle the case where input is not a number
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Multiplication Calculator")

# Create and place the widgets
tk.Label(root, text="Latest Gas Price (KG):").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Used Gas this Month:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Multiply", command=multiply_values).grid(row=2, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, columnspan=2)

# Run the application
root.mainloop()
