import pandas as pd

# CHANGE THIS to your actual file name
input_file = "2020_October_Virtual_Graduation_CEREMONY_2020.pdf_for_PRINTjvc6 (1).xlsx"

df = pd.read_excel(input_file)

# remove empty rows
df = df.dropna(how='all')

# example: if names are in a single column called NAME
# split into last, first, other names
try:
    df[['LASTNAME','FIRSTNAME','OTHER NAMES']] = df['NAME'].str.split(" ", 2, expand=True)
except:
    print("Could not split names because the column is not named 'NAME'.")

df.to_excel("CLEANED_OUTPUT.xlsx", index=False)

print("Cleaning completed.")
 
