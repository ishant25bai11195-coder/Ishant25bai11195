import matplotlib.pyplot as plt
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hours = []
for day in days:
    while True:
        try:
            h = float(input(f"Enter study hours for {day}: "))
            if h < 0:
                print("Hours cannot be negative please Enter a valid number.")
                continue
            hours.append(h)
            break
        except ValueError:
            print("Invalid input please enter a number")
total_hours = sum(hours)
average_hours = total_hours / len(days)
max_hours = max(hours)
min_hours = min(hours)
max_day = days[hours.index(max_hours)]
min_day = days[hours.index(min_hours)]
print("\nWeekly Study Performance Report")
print("-" * 40)
print(f"Total hours studied: {total_hours:.2f}")
print(f"Average hours per day: {average_hours:.2f}")
print(f"Day with most hours: {max_day} ({max_hours:.2f} hours)")
print(f"Day with least hours: {min_day} ({min_hours:.2f} hours)")
print("\nPerformance Reviews:")
if average_hours < 2:
    print("1 Poor performance")
    print("2 STAY CONSISTENTT")
    print("3 STUDY MORE")
elif 2 <= average_hours < 5:
    print("1 AvG performance")
    print("2 Good efforT")
    print("3 YOU ARE GOING GOOD BUT CAN DO BETTER")
else:
    print("1   Excellent performance")
    print("2  JUST STAYY CONSISTENT")
    print(" 3  Impressive")

plt.bar(days, hours, color='skyblue')
plt.xlabel('Days of the Week')
plt.ylabel('Study Hours')
plt.title('Daily Study Hours for the Week')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
