import matplotlib.pyplot as plt

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

def calculate_streaks_and_levels(user_id, update_only=False):
    user = users[user_id]
    total_xp_to_add = 0

    for habit in user['habits']:
        streak = 0
        streak_xp = 0 

        if update_only: 
            for day in habit['history']:
                if day == "yes":
                    streak += 1
                    multiplier = 1 + (streak - 1) * 0.5  
                    streak_xp += int(10 * multiplier)  
                else:
                    streak = 0

        total_xp_to_add += streak_xp 

    if update_only: 
        user['curr_XP'] += total_xp_to_add
        user['curr_lvl'] = user['curr_XP'] // 100 + 1


def quick_sort_leaderboard(leaderboard):
    if len(leaderboard) <= 1:
        return leaderboard
    pivot = leaderboard[0]
    less = [entry for entry in leaderboard[1:] if
            (entry[1]['curr_lvl'], entry[1]['curr_XP']) >= (pivot[1]['curr_lvl'], pivot[1]['curr_XP'])]
    greater = [entry for entry in leaderboard[1:] if
               (entry[1]['curr_lvl'], entry[1]['curr_XP']) < (pivot[1]['curr_lvl'], pivot[1]['curr_XP'])]
    return quick_sort_leaderboard(less) + [pivot] + quick_sort_leaderboard(greater)

def generate_leaderboard():
    leaderboard = list(users.items())
    sorted_leaderboard = quick_sort_leaderboard(leaderboard)
    print("\nLeaderboard:")
    print(f"{'Rank':<5} {'User':<15} {'Level':<10} {'XP':<10}")
    print("-" * 40)
    for rank, (user_id, user_data) in enumerate(sorted_leaderboard, start=1):
        print(f"{rank:<5} {user_id:<15} {user_data['curr_lvl']:<10} {user_data['curr_XP']:<10}")

def plot_progress(user_id):
    user = users[user_id]
    habits = user['habits']

    plt.figure(figsize=(10, 6))
    plt.title(f"Streak Progress for {user_id}")
    plt.xlabel("Days")
    plt.ylabel("Streak Count")
    plt.grid(alpha=0.3)

    for habit in habits:
        streaks = []
        current_streak = 0

        for day in habit['history']:
            if day == "yes":
                current_streak += 1
            else:
                current_streak = 0
            streaks.append(current_streak)

        plt.plot(streaks, label=habit['name'], marker="o")

    plt.legend(title="Habits")
    plt.show()

def add_new_participant():
    user_id = input("Enter your name or ID: ").strip()
    if user_id in users:
        print("User already exists!")
        return

    users[user_id] = {'habits': [], 'curr_XP': 0, 'curr_lvl': 1}
    while True:
        habit_name = input(f"Enter the habit name for {user_id}: ").strip()
        frequency = input("Enter the habit frequency (e.g., daily, weekly): ").strip()
        pref_time = input("Enter the preferred time for this habit (e.g., 8:30 pm): ").strip()
        notifications = input("Do you want reminders? (yes/no): ").strip().lower() == "yes"

        users[user_id]['habits'].append({
            'name': habit_name,
            'frequency': frequency,
            'pref_time': pref_time,
            'notifications': notifications,
            'history': ["no"] * 7 
        })

        add_more = input("Do you want to add another habit? (yes/no): ").strip().lower()
        if add_more != "yes":
            break

def update_data(user_id):
    if user_id not in users:
        print("User ID not found.")
        return

    user = users[user_id]

    while True:
        print("\nExisting Habits:")
        for idx, habit in enumerate(user['habits'], start=1):
            print(f"{idx}. {habit['name']}")

        choice = input(f"Do you want to update a habit or add a new one for {user_id}? (update/new): ").strip().lower()

        if choice == "update":
            habit_index = int(input("Enter the number of the habit you want to update: ")) - 1
            if 0 <= habit_index < len(user['habits']):
                habit = user['habits'][habit_index]
                print(f"Updating habit: {habit['name']}")
                status = input(f"Enter today's completion status for '{habit['name']}' (yes/no): ").strip().lower()
                habit['history'].pop(0) 
                habit['history'].append(status) 
            else:
                print("Invalid habit selection.")
        elif choice == "new":
            habit_name = input("Enter the new habit name: ").strip()
            frequency = input("Enter the habit frequency (e.g., daily, weekly): ").strip()
            pref_time = input("Enter the preferred time for this habit (e.g., 8:30 pm): ").strip()
            notifications = input("Do you want reminders? (yes/no): ").strip().lower() == "yes"

            user['habits'].append({
                'name': habit_name,
                'frequency': frequency,
                'pref_time': pref_time,
                'notifications': notifications,
                'history': ["no"] * 7  
            })
        else:
            print("Invalid choice.")

        more = input("Do you want to update more data? (yes/no): ").strip().lower()
        if more != "yes":
            break

    calculate_streaks_and_levels(user_id, update_only=True)

def view_user_data(user_id):
    if user_id not in users:
        print("No data found for this user.")
        return

    user = users[user_id]
    print(f"\nData for {user_id}:")
    for habit in user['habits']:
        print(f"  Habit: {habit['name']}")
        print(f"    Frequency: {habit['frequency']}")
        print(f"    Preferred Time: {habit['pref_time']}")
        print(f"    Notifications: {'Yes' if habit['notifications'] else 'No'}")
        print(f"    History: {', '.join(habit['history'])}")
    print()

    plot_progress(user_id)

def main():
    file_path = "user_data"
    load_users_from_file(file_path)

    user_id = input("Enter your user ID: ").strip()
    if user_id not in users:
        print("User ID not found. Redirecting to create a new account...")
        add_new_participant()
    else:
        print(f"Welcome back, {user_id}!")

    while True:
        print("\n=== Main Menu ===")
        print("1. View Your Progress")
        print("2. View Leaderboard")
        print("3. Update Data")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_user_data(user_id)
        elif choice == "2":
            generate_leaderboard()
        elif choice == "3":
            update_data(user_id)
        elif choice == "4":
            save_users_to_file(file_path)
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

main()
