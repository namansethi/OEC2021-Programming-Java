#Got to Read an Excel file
import pandas as pd

student_records_df = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Student Records')
print(student_records_df)
teacher_records_df = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teacher Records')
print(teacher_records_df)
ta_records_df = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teaching Assistant Records')
print(ta_records_df)
infected_student_list = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='ZBY1 Status')
print(infected_student_list)

infected_student_information = student_records_df.loc[student_records_df['Student Number'].isin(infected_student_list['Student ID'])]

print(infected_student_information)
