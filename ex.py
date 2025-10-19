import tkinter as tk
from tkinter import messagebox

# Function to calculate percentage
def calculate_percentage():
    try:
        obtained = float(entry_obtained.get())
        total = float(entry_total.get())

        if total <= 0:
            messagebox.showerror("Error", "Total marks must be greater than zero!")
            return
        
        percentage = (obtained / total) * 100
                                                                                                                                                                                                                                         label_result.config(text=f"Percentage: {percentage:.2f}%")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Percentage Calculator")
root.geometry("300x250")
root.config(bg="#f0f4f7")

# Title label
label_title = tk.Label(root, text="Percentage Calculator", font=("Arial", 14, "bold"), bg="#f0f4f7", fg="#333")
label_title.pack(pady=10)

# Obtained marks entry
label_obtained = tk.Label(root, text="Enter obtained marks:", bg="#f0f4f7", font=("Arial", 11))
label_obtained.pack()
entry_obtained = tk.Entry(root, width=25, font=("Arial", 11))
entry_obtained.pack(pady=5)

# Total marks entry
label_total = tk.Label(root, text="Enter total marks:", bg="#f0f4f7", font=("Arial", 11))
label_total.pack()
entry_total = tk.Entry(root, width=25, font=("Arial", 11))
entry_total.pack(pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_percentage, bg="#0078D7", fg="white",
                          font=("Arial", 11, "bold"), width=15)
btn_calculate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f7", fg="#0078D7")
label_result.pack(pady=10)

# Run the window
root.mainloop()
