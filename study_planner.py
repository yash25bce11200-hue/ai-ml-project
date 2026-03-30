import numpy as np

# Sample Data
subjects = ["Math", "Physics", "Chemistry", "English"]
marks = np.array([60, 70, 50, 80])
difficulty = np.array([5, 4, 3, 2])
study_hours = 6

# Normalize marks (lower marks = higher priority)
priority = (100 - marks) + (difficulty * 10)

# Calculate total priority
total_priority = sum(priority)

# Allocate time
time_allocated = (priority / total_priority) * study_hours

# Display schedule
print("📅 Study Plan:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {round(time_allocated[i], 2)} hours")
