📊 Weekly Study Performance Tracker

A simple, command-line Python utility to track, analyze, and visualize daily study hours over a week, providing immediate performance feedback.

✨ Features

Daily Data Collection: Prompts the user to input study hours for each day, Monday through Sunday.

Robust Input Validation: Ensures that all inputs are valid, non-negative numbers.

Performance Metrics: Calculates and displays total hours, daily average, and identifies the highest and lowest study days.

Qualitative Review: Provides a three-tiered performance review (Poor, Average, Excellent) based on the weekly average study hours.

Data Visualization: Generates a clear and professional bar chart using matplotlib to visually compare daily study efforts.

🛠️ Prerequisites

To run this script, you must have Python 3.x installed on your system.

You also need the matplotlib library for generating the visualization. You can install it using pip:

pip install matplotlib


🚀 How to Run the Script

Save the Code: Save the provided Python code into a file named study_tracker.py.

Run from Terminal: Navigate to the directory where you saved the file and execute the script:

python study_tracker.py


Input Data: The script will prompt you to enter the study hours for each day of the week, starting with Monday.

Enter study hours for Monday: 3.5
Enter study hours for Tuesday: 4
...


View Results: Once all seven days are entered, the script will instantly display the text report in the terminal and open a separate window showing the bar chart visualization.

💻 Example Output (Text Report)

Weekly Study Performance Report
----------------------------------------
Total hours studied: 27.50
Average hours per day: 3.93
Day with most hours: Friday (6.00 hours)
Day with least hours: Sunday (1.00 hours)

Performance Reviews:
1. Average performance: You're hitting a decent average, but there's room for more consistency.
2. Good effort: Keep pushing to reach 5+ hours daily for better results.
3. Balanced approach: Solid foundation; focus on quality over quantity in your studies.


📝 Code Overview

The script is structured into three main phases:

Input Loop: Collects and validates 7 inputs using try-except for numerical parsing and a conditional check for positive values.

Analysis: Standard Python functions (sum(), max(), min(), index()) are used to efficiently calculate the required metrics.

Output: Prints the textual report to the console and generates the bar chart using plt.bar() with customized labels and rotation for optimal display.

💡 Future Enhancements

As noted in the Project Report, several features could be added to enhance this tool:

Data Persistence: Integrate a simple storage mechanism (e.g., JSON or CSV) to save historical records.

Goal Setting: Add functionality to define and track a target weekly study goal.

GUI Development: Port the application to a desktop GUI (e.g., using Tkinter or Streamlit) for a more user-friendly experience.
