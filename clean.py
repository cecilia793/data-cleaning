import pandas as pd
import re

# -----------------------------
# CONFIG
# -----------------------------
INPUT_FILE = "2020_October_Virtual_Graduation_CEREMONY_2020.pdf_for_PRINTjvc6 (1).xlsx"     # GitHub will upload this file
OUTPUT_FILE = "cleaned_output.xlsx"

# Common headings / noise to remove
HEADINGS = [
    "LIST OF GRADUANDS",
    "SCHOOL OF",
    "FACULTY OF",
    "DEPARTMENT OF",
    "DIPLOMA IN",
    "BACHELOR OF",
    "MASTER OF",
    "PROGRAMME",
    "WITH MERIT",
    "WITH CREDIT",
    "WITH DISTINCTION"
]

# Titles to remove
TITLES = [
    "mr", "mrs", "ms", "miss", "dr", "prof", "rev", "sir"
]

# -----------------------------
# LOAD FILE
# -----------------------------
df = pd.read_excel(INPUT_FILE, header=None)

cleaned_rows = []
current_program = None

# -----------------------------
# PROCESS EACH ROW
# -----------------------------
for index, row in df.iterrows():
    text = " ".join(str(x) for x in row if pd.notna(x)).strip()
    text_lower = text.lower()

    # Skip empty rows
    if text.strip() == "":
        continue

    # Detect Programmes (e.g., DIPLOMA…, BACHELOR…)
    if any(key.lower() in text_lower for key in ["diploma", "bachelor", "master"]):
        current_program = text.strip()
        continue

    # Skip headings + noise
    if any(h.lower() in text_lower for h in HEADINGS):
        continue

    # Skip rows that are not names
    if len(text.split()) < 2:
        continue

    # Remove titles
    parts = text.split()
    parts = [p for p in parts if p.lower() not in TITLES]
    name = " ".join(parts)

    # Store only real names with current programme
    if current_program is not None:
        cleaned_rows.append([current_program, name])

# -----------------------------
# SAVE FINAL CLEAN FILE
# -----------------------------
output_df = pd.DataFrame(cleaned_rows, columns=["PROGRAMME", "STUDENT NAME"])
output_df.to_excel(OUTPUT_FILE, index=False)

print("Cleaning completed successfully!")
print("Saved as:", OUTPUT_FILE)

 
