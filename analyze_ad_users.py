import pandas as pd

# 1. Load the CSV (same folder, so no full path needed)
df = pd.read_csv("AD_Users_Export.csv")

# 2. Show basic structure
print("Columns found in CSV:")
print(df.columns)

print("\nPreview of data:")
print(df.head())

# 3. Basic validation
print("\nTotal number of users:", len(df))

# 4. Account status analysis
print("\nAccount status breakdown:")
print(df["Enabled"].value_counts())

# 5. Percentage of enabled vs disabled users
status_percent = df["Enabled"].value_counts(normalize=True) * 100
print("\nAccount status percentages:")
print(status_percent.round(2))

# 6. Find disabled accounts
disabled_users = df[df["Enabled"] == False]
print("\nDisabled accounts:")
print(disabled_users[["Name", "SamAccountName"]])

# 7. Simple risk insight
if len(disabled_users) > 0:
    print(f"\n⚠️ There are {len(disabled_users)} disabled accounts. Review for security and cleanup.")
else:
    print("\n✅ No disabled accounts found.")
