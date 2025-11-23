import matplotlib.pyplot as plt

# Define the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# List to store hours for each day
hours = []

# Collect input for each day
for day in days:
    while True:
        try:
            h = float(input(f"Enter study hours for {day}: "))
            if h < 0:
                print("Hours cannot be negative. Please enter a valid number.")
                continue
            hours.append(h)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculate performance metrics
total_hours = sum(hours)
average_hours = total_hours / len(days)
max_hours = max(hours)
min_hours = min(hours)
max_day = days[hours.index(max_hours)]
min_day = days[hours.index(min_hours)]

# Generate and print the weekly performance report
print("\nWeekly Study Performance Report")
print("-" * 40)
print(f"Total hours studied: {total_hours:.2f}")
print(f"Average hours per day: {average_hours:.2f}")
print(f"Day with most hours: {max_day} ({max_hours:.2f} hours)")
print(f"Day with least hours: {min_day} ({min_hours:.2f} hours)")

# Provide three reviews based on average hours per day
print("\nPerformance Reviews:")
if average_hours < 2:
    print("1. Poor performance: You're studying less than 2 hours a day on average. Consider increasing your study time to improve.")
    print("2. Needs improvement: Aim for at least 2-3 hours daily to build better habits.")
    print("3. Low effort: This level may not be sufficient for academic success; review your schedule.")
elif 2 <= average_hours < 5:
    print("1. Average performance: You're hitting a decent average, but there's room for more consistency.")
    print("2. Good effort: Keep pushing to reach 5+ hours daily for better results.")
    print("3. Balanced approach: Solid foundation; focus on quality over quantity in your studies.")
else:
    print("1. Excellent performance: Outstanding average! You're dedicated and on track for success.")
    print("2. High achiever: Maintain this level and consider advanced topics or projects.")
    print("3. Impressive dedication: Your consistency is commendable; keep up the great work!")

# Create a bar graph using matplotlib
plt.bar(days, hours, color='skyblue')
plt.xlabel('Days of the Week')
plt.ylabel('Study Hours')
plt.title('Daily Study Hours for the Week')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
