# Initialize empty lists to store roll, pitch, and yaw rates
roll_rates = []
pitch_rates = []
yaw_rates = []

# Split the input data into lines
lines = """
Roll rate degree = 0.12 Pitch rate degree = 0.10 Yaw Rate degree = -0.00
Roll rate degree = 0.06 Pitch rate degree = -0.03 Yaw Rate degree = -0.00
Roll rate degree = -0.00 Pitch rate degree = 0.16 Yaw Rate degree = -0.06
Roll rate degree = 0.36 Pitch rate degree = 0.03 Yaw Rate degree = -0.12
Roll rate degree = -0.12 Pitch rate degree = -0.15 Yaw Rate degree = -0.00
Roll rate degree = 0.12 Pitch rate degree = 0.22 Yaw Rate degree = -0.12
Roll rate degree = 0.18 Pitch rate degree = 0.10 Yaw Rate degree = 0.06
Roll rate degree = -0.06 Pitch rate degree = 0.03 Yaw Rate degree = 0.12
Roll rate degree = -0.06 Pitch rate degree = 0.22 Yaw Rate degree = -0.00
Roll rate degree = -0.00 Pitch rate degree = 0.10 Yaw Rate degree = 0.06
Roll rate degree = -0.37 Pitch rate degree = -0.27 Yaw Rate degree = 0.18
Roll rate degree = 0.12 Pitch rate degree = 0.34 Yaw Rate degree = -0.06
Roll rate degree = 1.40 Pitch rate degree = -3.08 Yaw Rate degree = -0.00
Roll rate degree = 0.06 Pitch rate degree = -1.06 Yaw Rate degree = 12.58
Roll rate degree = -0.55 Pitch rate degree = 0.71 Yaw Rate degree = -0.18
Roll rate degree = 0.61 Pitch rate degree = -2.22 Yaw Rate degree = 0.30
Roll rate degree = 0.30 Pitch rate degree = -0.21 Yaw Rate degree = 0.24
Roll rate degree = -0.73 Pitch rate degree = 1.13 Yaw Rate degree = 3.05
Roll rate degree = 0.18 Pitch rate degree = 0.28 Yaw Rate degree = -24.92
""".strip().split('\n')

# Iterate through each line
for line in lines:
    # Extract the roll, pitch, and yaw rates from the line
    parts = line.split('Pitch rate degree = ')
    roll_part = parts[0].split('Roll rate degree = ')[1].strip()
    pitch_part, yaw_part = parts[1].split(' Yaw Rate degree = ')
    
    # Convert the rates to float and append them to the corresponding lists
    roll_rates.append(float(roll_part))
    pitch_rates.append(float(pitch_part.strip()))
    yaw_rates.append(float(yaw_part.strip()))

# Create a Pandas DataFrame to display the data in tabular format
import pandas as pd
df = pd.DataFrame({'Roll rate degree': roll_rates, 'Pitch rate degree': pitch_rates, 'Yaw Rate degree': yaw_rates})
print(df)

df.info()
