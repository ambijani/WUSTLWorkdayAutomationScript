import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading


# Function to handle clock-in in a separate thread
def clock_in_thread():
    selected_position = position_var.get()
    if selected_position == "Select a Position" or not selected_position:
        messagebox.showerror("Error", "Please select a valid position.")
        return

    try:
        position_index = dropdown["values"].index(selected_position) + 1
        log_text.insert(tk.END, f"Clocking in for position: {selected_position}...\n")
        result = subprocess.run(
            ["python", "workdayClockIn.py", str(position_index)],
            capture_output=True,
            text=True
        )
        output = result.stdout or result.stderr or "Clock-In completed successfully!"
        log_text.insert(tk.END, f"Clock-In Output: {output}\n")
        if result.returncode == 0:
            messagebox.showinfo("Success", "Clock-In completed successfully!")
        else:
            messagebox.showerror("Error", "Clock-In failed. Check the logs for details.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Function to handle clock-out in a separate thread
def clock_out_thread():
    try:
        log_text.insert(tk.END, "Clocking out...\n")
        result = subprocess.run(
            ["python", "workdayClockout.py"],
            capture_output=True,
            text=True
        )
        output = result.stdout or result.stderr or "Clock-Out completed successfully!"
        log_text.insert(tk.END, f"Clock-Out Output: {output}\n")
        if result.returncode == 0:
            messagebox.showinfo("Success", "Clock-Out completed successfully!")
        else:
            messagebox.showerror("Error", "Clock-Out failed. Check the logs for details.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Start threads for clock-in or clock-out
def clock_in():
    threading.Thread(target=clock_in_thread).start()


def clock_out():
    threading.Thread(target=clock_out_thread).start()


# Load positions into dropdown
def load_positions():
    try:
        with open("positions.txt", "r") as file:
            positions = [line.strip() for line in file if line.strip()]
            if positions:
                dropdown["values"] = positions
                dropdown.set("Select a Position")  # Default placeholder text
            else:
                messagebox.showerror("Error", "No positions found in positions.txt.")
    except FileNotFoundError:
        messagebox.showerror("Error", "positions.txt file not found.")


# Main GUI setup
root = tk.Tk()
root.title("WashU Workday Automation")
root.geometry("600x500")
root.configure(bg="#f9f9f9")  # Light background

# Title Label
title_label = tk.Label(
    root,
    text="WashU Workday Automation Tool",
    font=("Helvetica", 16, "bold"),
    fg="#660000",  # WashU red
    bg="#f9f9f9"
)
title_label.pack(pady=15)

# Dropdown for position selection
frame_top = tk.Frame(root, bg="#f9f9f9")
frame_top.pack(pady=10)

position_var = tk.StringVar()
dropdown_label = tk.Label(
    frame_top,
    text="Select Position:",
    font=("Helvetica", 12),
    fg="#004b23",  # WashU green
    bg="#f9f9f9"
)
dropdown_label.pack(side=tk.LEFT, padx=10)
dropdown = ttk.Combobox(frame_top, textvariable=position_var, state="readonly", width=40)
dropdown.pack(side=tk.LEFT, padx=10)
load_positions()

# Buttons for clocking in and out
frame_buttons = tk.Frame(root, bg="#f9f9f9")
frame_buttons.pack(pady=20)

clock_in_button = tk.Button(
    frame_buttons,
    text="Clock In",
    font=("Helvetica", 12, "bold"),
    bg="#004b23",  # WashU green
    fg="white",
    width=15,
    height=2,
    command=clock_in
)
clock_in_button.grid(row=0, column=0, padx=10)

clock_out_button = tk.Button(
    frame_buttons,
    text="Clock Out",
    font=("Helvetica", 12, "bold"),
    bg="#660000",  # WashU red
    fg="white",
    width=15,
    height=2,
    command=clock_out
)
clock_out_button.grid(row=0, column=1, padx=10)

# Log viewer
frame_logs = tk.Frame(root, bg="#f9f9f9")
frame_logs.pack(pady=20)

log_label = tk.Label(
    frame_logs,
    text="Logs:",
    font=("Helvetica", 12),
    fg="#004b23",  # WashU green
    bg="#f9f9f9"
)
log_label.pack(anchor=tk.W, padx=10)
log_text = tk.Text(frame_logs, height=12, width=70, bg="#f4f4f4", fg="black", font=("Helvetica", 10))
log_text.pack(pady=10, padx=10)

# Run the GUI
root.mainloop()
