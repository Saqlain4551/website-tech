import tkinter as tk
from tkinter import messagebox

# Function to register voter
def register_voter():
    name = name_entry.get().title().strip()
    
    # Validate age
    try:
        age = int(age_entry.get().strip())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid age (number).")
        return

    if age < 18:
        messagebox.showinfo("Ineligible", "Sorry, you must be at least 18 to register to vote.")
        return

    # Open new window for party selection
    party_window = tk.Toplevel(root)
    party_window.title("Choose Your Party")
    party_window.geometry("350x300")

    tk.Label(party_window, text=f"Congratulations, {name}!\nYou are eligible to register to vote.",
             font=("Arial", 12), fg="green").pack(pady=10)

    tk.Label(party_window, text="Select your political party:", font=("Arial", 10)).pack()

    parties = ["Democratic", "Republican", "Libertarian", "Independent", "Green"]
    selected_party = tk.StringVar(value="")

    for party in parties:
        tk.Radiobutton(party_window, text=party, variable=selected_party, value=party, font=("Arial", 10)).pack()

    # Function to confirm party selection
    def confirm_party():
        chosen_party = selected_party.get()
        if chosen_party:
            msg = f"Congratulations, {name}! You have joined the {chosen_party} party.\n"
            if chosen_party in ["Democratic", "Republican"]:
                msg += "This is a major party!"
            elif chosen_party == "Independent":
                msg += "You are an independent person!"
            else:
                msg += "This is not a major party."

            msg += f"\n{name}, you are officially registered as a member of the {chosen_party} party."
            messagebox.showinfo("Registration Complete", msg)
            party_window.destroy()
        else:
            messagebox.showerror("Selection Error", "Please choose a party before submitting.")

    tk.Button(party_window, text="Submit", command=confirm_party, font=("Arial", 10), bg="blue", fg="white").pack(pady=10)

# Main window setup
root = tk.Tk()
root.title("Voter Registration App")
root.geometry("400x300")

tk.Label(root, text="Welcome to Voter Register App", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack()
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack()

tk.Label(root, text="Enter your age:", font=("Arial", 12)).pack()
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.pack()

tk.Button(root, text="Register", command=register_voter, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

root.mainloop()
