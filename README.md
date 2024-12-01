# PlanEase
PlanEase is a platform designed to help users build consistent habits, track their progress, and level up their achievements.

Our platform has three main functions:

It allows users to track their daily habits and monitor progress over time through streaks.
It displays a leaderboard to compare achievements among users.
It enables users to update existing habits or add new ones seamlessly.
## Features
### 1. Tracking Progress
Users can log their daily habit progress (e.g., whether a task was completed).
A visual streak progress graph is displayed to help users monitor their consistency.
### 2. Leaderboard
The leaderboard ranks users based on their levels and XP.
XP and levels are determined by the user's habit streaks and consistent progress.
The leaderboard updates dynamically as users log their progress or add new habits.
### 3. Updating or Adding Habits
Users can update the progress of an existing habit or add new habits with details such as:
Habit name
Frequency (e.g., daily, weekly)
Preferred time
Notification preferences

## Installation
To run this program, ensure you have the following installed on your system:

**Python**: Version 3.6 or higher.
Libraries:
**matplotlib** for data visualization
**tkinter** for the GUI
To install the required libraries, use the following command:

_bash
Copy code
pip install matplotlib_

## Usage
Launch the Program:

Run the file habit_tracker.py to start the GUI.
Login:

Enter your User ID to log in or create a new account.
If the User ID does not exist, a new account will be created automatically.
Main Menu:

The main menu provides the following options:
View Progress:
Displays a visual streak progress graph for your habits.
View Leaderboard:
Shows the leaderboard, ranking users based on levels and XP.
Update/Add Habit:
Update progress for an existing habit or add a new habit.
Exit:
Saves data and exits the application.
## Data Management
How the Data is Stored:

File Name: user_data

Each user's data includes:

XP: Total XP accumulated based on habit streaks.

Level: Calculated from the XP.

Habits: 
Each habit includes:
Name, Frequency, Preferred Time, Notification Preference, History: A 7-day record of whether the habit was completed (yes or no).
Example Data Format in user_data:

[JohnDoe]
XP: 150
Level: 2
Habit1, daily, 8:00 AM, yes
History: yes, yes, no, yes, yes, yes, yes
Habit2, weekly, 6:00 PM, no
History: yes, no, yes, no, yes, yes, no

## Key Functionalities
**Streak Progress:**

Visualize streaks for each habit in a line chart.
Track your consistency over time.
Leaderboard:

Ranks users by levels and XP using a quicksort algorithm.
Displays the top performers in a separate window.
Habit Updates:

Modify existing habits or add new ones directly through the GUI.
Save changes to the user_data file for future sessions.
## Technical Details
Data Structures:
Dictionaries:
Used to store user data, including habits, XP, and levels.
Lists:
Maintains habit histories and temporary data for leaderboard sorting.
### Algorithms:
**Quick Sort:**
Efficiently sorts users for the leaderboard based on XP and levels.
**XP and Level Calculation:**
XP is calculated from streaks and habit completion using multipliers.
Levels are determined by cumulative XP (100 XP per level).
## Authors
This project was developed by:

David Cortes, Kristian Giuffre, Marcos Ruano, Mariana Serrano, Andrea Salamini
