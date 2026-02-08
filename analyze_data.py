import pandas as pd

# Path to your big dataset
file_path = "datasets/AI_Human.csv"

print("Reading dataset... please wait, it's a big one!")

# We read only the 'generated' column to save memory
# 0.0 is Human, 1.0 is AI
try:
    # Reading the file in chunks or just specific columns
    df = pd.read_csv(file_path, usecols=['generated'])
    
    total_rows = len(df)
    ai_count = df['generated'].sum()
    human_count = total_rows - ai_count
    
    print("-" * 30)
    print(f"Total texts in file: {total_rows:,}")
    print(f"Human written: {int(human_count):,}")
    print(f"AI generated: {int(ai_count):,}")
    print("-" * 30)
    print("Success! Data is ready for training.")

except Exception as e:
    print(f"Error reading file: {e}")
