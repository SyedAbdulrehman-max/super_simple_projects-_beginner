print('===== Resume Builder ====')

fullname = input('Full Name: ')

jobtital = input('Job Tital: ')

Email = input('Email: ')

PhoneNumber = input('Phone Number: ')

Location = input('Location: ')

summary = input('Summary (Keep it clean 2-3 lines)')

#Education

education = input('Degree ,Institution ,Year: ')


# Work Experience

print('===== Work Experience ====')

print("If you don't work in any company you can skip by press 'ENTER'")

experience = input('Company Name ,Role/job ,Years (Start – End):  ')
skills = input('Skills: ')

Languages = input("List of languages you can speak/write (e.g., English, Urdu, Arabic):")


resume = f"""


============================================================
{fullname}
{jobtital}
Email: {Email} | Phone: {PhoneNumber} | Location: {Location}
============================================================

Summary
-------
{summary}

Education
---------
{education}

Experience
----------
{experience}

Skills
------
{skills}

Language
--------
{Languages}
"""

with open("resume.txt", "w", encoding="utf-8") as f:
    f.write(resume)


print('\n====YOUR RESUME ====\n')
print(resume)
print('Save to resume.txt')



