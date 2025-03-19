import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Parameters
num_records = 100000
attendance_codes = ['P', 'A']
reasons = ['Sick', 'Personal', 'Unexcused', None]  # None simulates no reason provided

# Generate Attendance Data
attendance_data = {
    'Employee ID': [f"E{str(i).zfill(4)}" for i in range(1, num_records+1)],
    'Employee Name': [fake.name() for _ in range(num_records)],
    'Date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    'Attendance Code': np.random.choice(attendance_codes, num_records, p=[0.9, 0.1]),
    'Reason for Absence': [random.choice(reasons) for _ in range(num_records)]
}
df_attendance = pd.DataFrame(attendance_data)

# Introduce duplicate rows intentionally (simulate 2% duplicates)
df_attendance = df_attendance.append(df_attendance.sample(frac=0.02), ignore_index=True)

# Generate Engagement Data similarly
engagement_types = ['Training', 'Meeting', 'Project']
engagement_data = {
    'Employee ID': [f"E{str(random.randint(1, num_records)).zfill(4)}" for _ in range(num_records)],
    'Employee Name': [fake.name() for _ in range(num_records)],
    'Date': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_records)],
    'Activity Type': np.random.choice(engagement_types, num_records),
    'Engagement Score': np.random.randint(1, 11, num_records)
}
df_engagement = pd.DataFrame(engagement_data)

# Save to CSV
df_attendance.to_csv('Employee_Attendance.csv', index=False)
df_engagement.to_csv('Employee_Engagement.csv', index=False)

print("Datasets generated successfully!")
