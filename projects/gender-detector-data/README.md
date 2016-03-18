##City employee Base and Overtime Salary for Calendar Year 2014

#Preliminary findings

More women than men overall as employees: 375 women and 262 men.
More women than men in every salary level, from 50,000 to 250,000.
The salary gap between men and women is smaller when salaries range from 125,001 to 250,000.

#fetch_gender_data.py

Downloads the latest batch of baby name data from the Social Security Administration and dumps it into the tempdata/babynames folder

#wrangle_gender_data.py

Reads a few files from tempdata/babynames and creates a new data file in babynames/wrangledbabynames.json, which is used by gender.detect_gender() to classify the gender of a name.

#fetch_payroll_data.py

Downloads two data files TK

#wrangle_payroll_data.py

Since the above file is huge and unweldly, this script wrangles it down to those people who work in the office of the mayor--almost 700 of them.

#gender.py

This script goes through each employee's first name guessing wheter they are male or female.

#classify.py

Reads through the two salary files and appends new columns to them

#analyze.py

Breaks down the number of female and male employees in each salary in eaach salary bracket in the mayor's office.