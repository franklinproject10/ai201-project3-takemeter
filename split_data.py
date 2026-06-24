import pandas as pd
from sklearn.model_selection import train_test_split

# load the full dataset
df = pd.read_csv('data/raw/dataset.csv')
print(f"Full dataset: {len(df)} rows")
print(df['label'].value_counts())
print()

# first split: 70% train, 30% temp (which becomes val + test)
train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    random_state=42,
    stratify=df['label']
)

# second split: split the 30% temp evenly into 15% val and 15% test
val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42,
    stratify=temp_df['label']
)

# save the three splits
train_df.to_csv('data/train.csv', index=False)
val_df.to_csv('data/val.csv', index=False)
test_df.to_csv('data/test.csv', index=False)

# confirm the splits
print(f"Train: {len(train_df)} rows")
print(train_df['label'].value_counts())
print()
print(f"Validation: {len(val_df)} rows")
print(val_df['label'].value_counts())
print()
print(f"Test: {len(test_df)} rows")
print(test_df['label'].value_counts())
print()
print("Split complete. Files saved to data/")