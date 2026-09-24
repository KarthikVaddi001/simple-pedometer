print("🚶 SIMPLE PEDOMETER")

steps = int(input("Enter today's steps: "))
goal = 10000

progress = (steps / goal) * 100
remaining = max(goal - steps, 0)

print("\n--- Today's Report ---")
print(f"Steps: {steps}")
print(f"Daily Goal: {goal}")
print(f"Progress: {progress:.1f}%")

if steps >= goal:
    print("🎉 Congratulations! You reached your goal!")
else:
    print(f"Keep going! You need {remaining} more steps.")