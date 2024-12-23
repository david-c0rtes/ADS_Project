# PlanEase

<div align="center">PlanEase is an app designed to turn the hassle of planning and the boredom of calendars

<div align="center">Into an intuitive and interactive experience, helping people across generations

<div align="center">To make habit tracking fun and easy 

<div align="left">- The PlanEase Team: David Cortes, Mariana Serrano, Kristian Giuffré, Andrea Salamini, Marcos Ruano
  
## Features

### 1. Tracking Progress

Users can log their daily habit progress (e.g. whether a task was completed).

A visual streak progress graph of the last week is displayed to help users monitor their consistency.

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

## Usage
Launch the Program:

Run the file to start the GUI.

**Login:**
Enter your User ID to log in or create a new account.
If the User ID does not exist, a new account will be created automatically.

**Main Menu:**
The main menu provides the following options:

**View Progress:**
Displays a visual streak progress graph for your habits.

**View Leaderboard:**
Shows the leaderboard, ranking users based on levels and XP.

**Update/Add Habit:**
Update progress for an existing habit or add a new habit.

**Exit:**
Saves data and exits the application.

## Data Management
### How the Test Data was Stored:

File Name: user_data

XP: Total XP accumulated based on habit streaks.

Level: Calculated from the XP.

Habit Name

Frequency

Preferred Time

Notification Preference: yes or no

History: record of whether the habit was completed (yes or no).

### Example Data Format in user_data:

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

**Leaderboard:**

Ranks users by levels and XP using a quicksort algorithm.

Hash tables are transformed to a list for quicksort.

Displays the top performers in a separate window.

**Habit Updates:**

Modify existing habits or add new ones directly through the GUI.


## Technical Details

### Data Structures:

**Dictionaries:**

Used to store user data, including habits, XP, and levels.

**Lists:**

Used to create test data to simulate the GUI and temporary data for leaderboard sorting.

### Algorithms:

**Quick Sort:**

Efficiently sorts users for the leaderboard based on XP and levels.

**XP and Level Calculation:**

XP is calculated from streaks and habit completion using multipliers.

Levels are determined by cumulative XP (100 XP per level).

## Authors

This project was developed by:

David Cortes

Kristian Giuffre 

Marcos Ruano

Mariana Serrano

Andrea Salamini
