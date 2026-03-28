import pandas as pd

df = pd.read_csv("gsearch_jobs.csv")

print("Loaded successfully")

print(df.shape)
print(df.head())

print(df['salary_standardized'].isna().sum())

import pandas as pd

df = pd.read_csv("gsearch_jobs.csv")

print(df.shape)
print(df['salary_standardized'].isna().sum())

import ast

# Remove useless columns
df = df.drop(columns=['Unnamed: 0', 'index'])

# Convert tokens from string to list
df['description_tokens'] = df['description_tokens'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else []
)

skills = ['sql', 'python', 'excel', 'power_bi', 'tableau']

for skill in skills:
    df[skill] = df['description_tokens'].apply(lambda x: 1 if skill in x else 0)

skill_counts = df[skills].sum().sort_values(ascending=False)
print(skill_counts)

salary_df = df[df['salary_standardized'].notna()]

print(salary_df.shape)

for skill in skills:
    avg_salary = salary_df[salary_df[skill] == 1]['salary_standardized'].mean()
    print(skill, avg_salary)

top_companies = df['company_name'].value_counts().head(10)
print(top_companies)

remote_percentage = df['work_from_home'].mean() * 100
print(remote_percentage)

df.to_csv("cleaned_jobs.csv", index=False)

print("CSV file created successfully!")

salary_df.to_csv("salary_jobs.csv", index=False)

print("\n--- KEY INSIGHTS ---")

total_jobs = len(df)
print(f"Total job postings analyzed: {total_jobs}")

top_skill = skill_counts.idxmax()
print(f"Most in-demand skill: {top_skill}")

highest_paying_skill = ""
highest_salary = 0

for skill in skills:
    avg_salary = salary_df[salary_df[skill] == 1]['salary_standardized'].mean()
    if avg_salary > highest_salary:
        highest_salary = avg_salary
        highest_paying_skill = skill

print(f"Highest paying skill: {highest_paying_skill} with avg salary {highest_salary:.2f}")

print(f"Remote jobs percentage: {remote_percentage:.2f}%")


import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")

df_small = df[[
    'title',
    'company_name',
    'location',
    'salary_standardized',
    'sql',
    'python',
    'excel',
    'power_bi',
    'tableau',
    'work_from_home'
]]

df_small.to_csv("jobs_sql.csv", index=False)

print("New CSV created successfully!")
