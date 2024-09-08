import tkinter as tk
from tkinter import messagebox

def computePayment(interest_rate, num_years, loan_amount):
    monthly_rate = interest_rate / 1200
    num_months = num_years * 12
    monthly_payment = loan_amount * monthly_rate / (1 - (1 / (1 + monthly_rate)**num_months))
    total_payment = monthly_payment * num_months
    return monthly_payment, total_payment

def getMonthlyPayment():
    try:
        interest_rate = float(entry_interest_rate.get())
        num_years = int(entry_num_years.get())
        loan_amount = float(entry_loan_amount.get())
        
        monthly_payment, total_payment = computePayment(interest_rate, num_years, loan_amount)
        
        label_monthly_payment_value.config(text=f"${monthly_payment:.2f}")
        label_total_payment_value.config(text=f"${total_payment:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Loan Payment Calculator")

# Create and place the labels and entry boxes
tk.Label(root, text="Annual Interest Rate (e.g., 5.5)").grid(row=0, column=0, padx=10, pady=5)
entry_interest_rate = tk.Entry(root)
entry_interest_rate.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Years (e.g., 10)").grid(row=1, column=0, padx=10, pady=5)
entry_num_years = tk.Entry(root)
entry_num_years.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Loan Amount (e.g., 10000)").grid(row=2, column=0, padx=10, pady=5)
entry_loan_amount = tk.Entry(root)
entry_loan_amount.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Monthly Payment:").grid(row=3, column=0, padx=10, pady=5)
label_monthly_payment_value = tk.Label(root, text="")
label_monthly_payment_value.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Total Payment:").grid(row=4, column=0, padx=10, pady=5)
label_total_payment_value = tk.Label(root, text="")
label_total_payment_value.grid(row=4, column=1, padx=10, pady=5)

# Create and place the button
tk.Button(root, text="Compute Payments", command=getMonthlyPayment).grid(row=5, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
