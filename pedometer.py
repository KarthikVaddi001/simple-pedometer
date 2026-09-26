print("================================")
print("       🚶 SIMPLE PEDOMETER")
print("================================")

# Daily step goal
goal = 10000

# Get today's steps
steps = int(input("Enter today's steps: "))

# Calculate progress
progress = (steps / goal) * 100

# Calculate remaining steps
remaining = max(goal - steps, 0)

# Estimate distance
# Average step length = 0.75 meters
distance = (steps * 0.75) / 1000

# Estimate calories
# Simple estimate: 0.04 calories per step
calories = steps * 0.04

# Display report
print("\n========== DAILY REPORT ==========")
print(f"Steps       : {steps}")
print(f"Goal        : {goal}")
print(f"Progress    : {progress:.1f}%")
print(f"Distance    : {distance:.2f} km")
print(f"Calories    : {calories:.0f} kcal")

# Activity message
print("\n========== ACTIVITY ==========")

if steps >= goal:
    print("🎉 Excellent! You reached your daily goal!")
elif steps >= 7000:
    print("🔥 Great job! You are very active today.")
elif steps >= 3000:
    print("👍 Good progress! Keep walking.")
else:
    print("🚶 Try to walk a little more today.")

# Remaining steps
if remaining > 0:
    print(f"You need {remaining} more steps to reach your goal.")
else:
    print("You have completed your goal!")

print("\n================================")