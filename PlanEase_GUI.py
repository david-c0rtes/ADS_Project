import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Listbox, messagebox, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

users = {}

def load_users_from_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    current_user = None

    for line in lines:
        line = line.strip()
        if not line: 
            continue
        if line.startswith("[") and line.endswith("]"): 
            current_user = line[1:-1]
            users[current_user] = {'habits': [], 'curr_XP': 0, 'curr_lvl': 1}
        elif line.startswith("XP:"):  
            xp = int(line.split(": ")[1])
            if current_user:
                users[current_user]['curr_XP'] = xp
        elif line.startswith("Level:"):  
            level = int(line.split(": ")[1])
            if current_user:
                users[current_user]['curr_lvl'] = level
        elif line.startswith("History:"):  
            history = line.split(": ")[1].split(", ")
            if current_user and users[current_user]['habits']:
                users[current_user]['habits'][-1]['history'] = history
        else:  
            habit_data = line.split(", ")
            if len(habit_data) < 4:  
                continue
            habit = {
                'name': habit_data[0],
                'frequency': habit_data[1],
                'pref_time': habit_data[2],
                'notifications': habit_data[3].lower() == "yes",
                'history': []  
            }
            if current_user:
                users[current_user]['habits'].append(habit)

def save_users_to_file(filepath):
    with open(filepath, 'w') as file:
        for user_id, data in users.items():
            file.write(f"[{user_id}]\n")
            file.write(f"XP: {data['curr_XP']}\n")
            file.write(f"Level: {data['curr_lvl']}\n")
            for habit in data['habits']:
                file.write(f"{habit['name']}, {habit['frequency']}, {habit['pref_time']}, {'yes' if habit['notifications'] else 'no'}\n")
                file.write(f"History: {', '.join(habit['history'])}\n")

def quick_sort_leaderboard(leaderboard):
    if len(leaderboard) <= 1:
        return leaderboard
    pivot = leaderboard[0]
    less = [entry for entry in leaderboard[1:] if
            (entry[1]['curr_lvl'], entry[1]['curr_XP']) >= (pivot[1]['curr_lvl'], pivot[1]['curr_XP'])]
    greater = [entry for entry in leaderboard[1:] if
               (entry[1]['curr_lvl'], entry[1]['curr_XP']) < (pivot[1]['curr_lvl'], pivot[1]['curr_XP'])]
    return quick_sort_leaderboard(less) + [pivot] + quick_sort_leaderboard(greater)

def calculate_streaks_and_levels(user_id, update_only=False):
    user = users[user_id]
    habits = user['habits']

    streak_multiplier = 10  
    base_xp = 5  
    xp_to_next_level = 100  

    total_xp = user['curr_XP']
    for habit in habits:
        current_streak = 0
        for day in habit['history']:
            if day == "yes":
                current_streak += 1
                total_xp += base_xp 
            else:
                current_streak = 0

        total_xp += current_streak * streak_multiplier

    if not update_only:  
        level = 1
        remaining_xp = total_xp
        while remaining_xp >= xp_to_next_level:
            remaining_xp -= xp_to_next_level
            level += 1

        user['curr_lvl'] = level
    user['curr_XP'] = total_xp

def generate_leaderboard_gui():
    leaderboard_window = Toplevel(root)
    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("500x400")

    leaderboard = list(users.items())
    leaderboard = quick_sort_leaderboard(leaderboard)

    Label(leaderboard_window, text="Leaderboard", font=("Arial", 16)).pack(pady=10)
    leaderboard_list = Listbox(leaderboard_window, width=60, height=20)
    leaderboard_list.pack()

    for rank, (user_id, user_data) in enumerate(leaderboard, start=1):
        leaderboard_list.insert(
            "end", f"{rank}. {user_id} - Level: {user_data['curr_lvl']} | XP: {user_data['curr_XP']}")

def plot_progress_in_gui():
    user_id = current_user.get()
    if user_id not in users:
        messagebox.showerror("Error", "User not found!")
        return

    user = users[user_id]
    habits = user['habits']

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title(f"Streak Progress for {user_id}")
    ax.set_xlabel("Days")
    ax.set_ylabel("Streak Count")
    ax.grid(alpha=0.3)

    for habit in habits:
        streaks = []
        current_streak = 0

        for day in habit['history']:
            if day == "yes":
                current_streak += 1
            else:
                current_streak = 0
            streaks.append(current_streak)

        ax.plot(streaks, label=habit['name'], marker="o")

    ax.legend(title="Habits")

    plot_window = Toplevel(root)
    plot_window.title("Progress Plot")
    canvas = FigureCanvasTkAgg(fig, plot_window)
    canvas.get_tk_widget().pack()
    canvas.draw()

def update_or_add_habit():
    def save_habit():
        habit_name = habit_name_entry.get().strip()
        frequency = frequency_entry.get().strip()
        pref_time = time_entry.get().strip()
        notifications = notifications_var.get()

        if not habit_name or not frequency or not pref_time:
            messagebox.showerror("Error", "All fields are required!")
            return

        user = users[current_user.get()]
        for habit in user['habits']:
            if habit['name'] == habit_name:
                habit['frequency'] = frequency
                habit['pref_time'] = pref_time
                habit['notifications'] = notifications
                messagebox.showinfo("Info", "Habit updated successfully!")
                save_users_to_file("user_data")
                update_habit_window.destroy()
                return

        user['habits'].append({
            'name': habit_name,
            'frequency': frequency,
            'pref_time': pref_time,
            'notifications': notifications,
            'history': ["no"] * 7
        })
        messagebox.showinfo("Info", "New habit added successfully!")
        save_users_to_file("user_data")
        update_habit_window.destroy()

    def update_progress():
        habit_index = habits_listbox.curselection()
        if not habit_index:
            messagebox.showerror("Error", "Please select a habit to update!")
            return

        habit_index = habit_index[0]
        user = users[current_user.get()]
        habit = user['habits'][habit_index]

        status = status_var.get().strip().lower()
        if status not in ("yes", "no"):
            messagebox.showerror("Error", "Please enter 'yes' or 'no' for the status.")
            return

        habit['history'].pop(0)  
        habit['history'].append(status) 

        if status == "yes":  
            calculate_streaks_and_levels(current_user.get())

        messagebox.showinfo("Info", f"Updated progress for habit: {habit['name']}")
        save_users_to_file("user_data")
        update_habit_window.destroy()

    update_habit_window = Toplevel(root)
    update_habit_window.title("Update/Add Habit")
    update_habit_window.geometry("400x400")

    Label(update_habit_window, text="Existing Habits:", font=("Arial", 12)).pack(pady=5)
    habits_listbox = Listbox(update_habit_window, height=7, selectmode="single")
    habits_listbox.pack(pady=5, fill="x")

    user = users[current_user.get()]
    for habit in user['habits']:
        habits_listbox.insert("end", habit['name'])

    Label(update_habit_window, text="Enter today's progress (yes/no):", font=("Arial", 12)).pack(pady=5)
    status_var = StringVar()
    Entry(update_habit_window, textvariable=status_var).pack(pady=5)

    Button(update_habit_window, text="Update Progress", command=update_progress).pack(pady=5)

    Label(update_habit_window, text="--- OR ---", font=("Arial", 10)).pack(pady=5)
    Label(update_habit_window, text="Add New Habit:", font=("Arial", 12)).pack(pady=5)

    Label(update_habit_window, text="Habit Name:").pack(pady=5)
    habit_name_entry = Entry(update_habit_window)
    habit_name_entry.pack(pady=5)

    Label(update_habit_window, text="Frequency (e.g., daily):").pack(pady=5)
    frequency_entry = Entry(update_habit_window)
    frequency_entry.pack(pady=5)

    Label(update_habit_window, text="Preferred Time:").pack(pady=5)
    time_entry = Entry(update_habit_window)
    time_entry.pack(pady=5)

    notifications_var = StringVar(value="no")
    Label(update_habit_window, text="Notifications:").pack(pady=5)
    Button(update_habit_window, text="Yes", command=lambda: notifications_var.set("yes")).pack(pady=2)
    Button(update_habit_window, text="No", command=lambda: notifications_var.set("no")).pack(pady=2)

    Button(update_habit_window, text="Add Habit", command=save_habit).pack(pady=10)

def main_menu():
    clear_window()
    Label(root, text=f"Welcome, {current_user.get()}!", font=("Arial", 16)).pack(pady=10)
    Button(root, text="View Progress", command=plot_progress_in_gui).pack(pady=5)
    Button(root, text="View Leaderboard", command=generate_leaderboard_gui).pack(pady=5)
    Button(root, text="Update/Add Habit", command=update_or_add_habit).pack(pady=5)
    Button(root, text="Exit", command=exit_program).pack(pady=5)

def exit_program():
    save_users_to_file("user_data")
    root.quit()

def login():
    user_id = user_id_entry.get().strip()
    if not user_id:
        messagebox.showerror("Error", "User ID cannot be empty!")
        return

    current_user.set(user_id)
    if user_id not in users:
        messagebox.showinfo("Info", "User ID not found. Creating a new account.")
        users[user_id] = {'habits': [], 'curr_XP': 0, 'curr_lvl': 1}
    main_menu()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

root = Tk()
root.title("Habit Tracker")
root.geometry("500x400")

current_user = StringVar()

Label(root, text="Enter User ID:", font=("Arial", 12)).pack(pady=10)
user_id_entry = Entry(root, font=("Arial", 12))
user_id_entry.pack(pady=5)
Button(root, text="Login", command=login).pack(pady=10)

load_users_from_file("user_data")

root.mainloop()
