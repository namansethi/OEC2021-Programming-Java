import pandas as pd
import numpy as np


def get_student_records():
    student_records_df_raw = pd.readexcel('./Resources/OEC2021-_School_RecordBook.xlsx', sheet_name='Student Records')
    student_records_df_raw = student_records_df_raw.iloc[:580]
    student_records_df_raw['Extracurricular Activities'] = student_records_df_raw['Extracurricular Activities'].apply(lambda x: parse_extracurricular_activities(x))

    student_records_df_ret = student_records_df_raw
    return student_records_df_ret


def parse_extracurricular_activities(activ):
    if activ != 'NaN':
        return str(activ).split(',')[0]
    return activ

def get_teacher_records():
    teacher_records_df_raw = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teacher Records')

    return  teacher_records_df_raw


def get_ta_records():
    ta_records_df_raw = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teaching Assistant Records')

    return ta_records_df_raw


def get_infected_status():
    infected_status_df_raw = pd.read_excel('./Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='ZBY1 Status')

    infected_status_df_raw['Person Type'] = np.nan
    if 'Student ID' in infected_status_df_raw.columns:
        infected_status_df_raw.loc[infected_status_df_raw['Student ID'].notnull(), 'Person Type'] = 'Student'
    if 'Teacher ID' in infected_status_df_raw.columns:
        infected_status_df_raw.loc[infected_status_df_raw['Teacher ID'].notnull(), 'Person Type'] = 'Teacher'

    infected_status_df_raw.loc[infected_status_df_raw['Student ID'].isnull(), 'Person Type'] = 'Teaching Assistant'

    infected_status_df_ret = infected_status_df_raw
    return infected_status_df_ret


if __name__ == '__main__':
    # get the tables
    student_record_table = get_student_records()
    teacher_record_table = get_student_records()
    ta_record_table = get_ta_records()
    infected_status_table = get_infected_status()


    #get the information of the infected students
    infected_students_table = infected_status_table.loc[infected_status_table['Person Type'] == 'Student']
    infected_student_information = student_record_table.loc[ student_record_table['Student Number'].isin(infected_students_table['Student ID']) ]
    print(infected_student_information)
    print(infected_student_information['First Name'])

    #get the lisat of students in Art A
    period_one_artA = student_record_table.loc[student_record_table['Period 1 Class'] == 'Art B']

