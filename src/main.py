#Got to Read an Excel file
import numpy as np
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

student_records_df['infection'] = np.nan




def infection_rate(period,course):

    course_and_period = student_records_df.loc[student_records_df[period]==course]
    print(course_and_period)

    infected = course_and_period.loc[course_and_period['infection']!='NaN']

    ta = ta_records_df.loc[ta_records_df[period]==course]

    teacher = teacher_records_df.loc[teacher_records_df['Class']==course]

    print(ta)

    if (ta.empty):
        num = len(course_and_period)+1
        print(num)
    else:
        num = len(course_and_period)+2
        if (ta.loc[ta['infection']!='NaN'] != "NaN"):
            TAInfect = 'true'
        else:
            TAInfect = 'false'

    grad9 = infected.loc[infected['Grade']==9]
    col_one_list = grad9['infection'].tolist()
    multiplied_list = [element/100 * (3/num) for element in col_one_list]
    grade9infect = calc_infect_rate(col_one_list)

    grad10 = infected.loc[infected['Grade']==10]
    col_one_list = grad10['infection'].tolist()
    multiplied_list = [element/100 * (3 / num) for element in col_one_list]
    grade10infect = calc_infect_rate(col_one_list)

    grad11 = infected.loc[infected['Grade']==11]
    col_one_list = grad11['infection'].tolist()
    multiplied_list = [element/100 * (3 / num) for element in col_one_list]
    grade11infect = calc_infect_rate(col_one_list)

    grad12 = infected.loc[infected['Grade']==12]
    col_one_list = grad12['infection'].tolist()
    multiplied_list = [element/100 * (3 / num) for element in col_one_list]
    grade12infect = calc_infect_rate(col_one_list)



    isteacherInfected = 'true'
    isClassRoomInfected = 'true'

    infectRate = 0.5

    for index, row in course_and_period.iterrows():
        print(row)
        grade = row['Grade']
        print(grade)
        healthcondition = row['Health Conditions']
        #infection = row.['infection']

        print(healthcondition)

        if(healthcondition != 'nan'):
            healthcondition = 'true'

        if (infection == 1):
            continue

        if grade == 9:
            if healthcondition:
                list = [grade9infect,grade10infect,grade11infect,grade12infect]
                infect = calc_infect_rate(list)
                infect = infect*1.7
                if(infect >= 1):
                    infection = 1
                else:
                    infection = 1-(1-infection)*(1-infect)
            else:
                list = [infection,grade9infect, grade10infect, grade11infect, grade12infect]
                infection = calc_infect_rate(list)

        if grade == 10:
            if healthcondition:
                list = [grade9infect*1.25,grade10infect,grade11infect,grade12infect]
                infect = calc_infect_rate(list)
                infect = infect*1.7
                if(infect >= 1):
                    infection = 1
                else:
                    infection = 1-(1-infection)*(1-infect)
            else:
                list = [grade9infect * 1.25, grade10infect, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)

        if grade == 11:
            if healthcondition:
                list = [grade9infect * 1.5, grade10infect*1.25, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7
                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [grade9infect * 1.5, grade10infect*1.25, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)

        if grade == 12:
            if healthcondition:
                list = [grade9infect * 1.75, grade10infect*1.5, grade11infect*1.25, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7
                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [grade9infect * 1.75, grade10infect*1.5, grade11infect*1.25, grade12infect]
                infect = calc_infect_rate(list)
                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)

        if isteacherInfected:
            infection = 1-(1-infection)*(1-3/num*0.2)
        if TAInfect:
            infection = 1-(1-infection)*(1-3/num*0.2)
        #note working need to be changed
        if isClassRoomInfected:
            infection = infection + 3/num*infectRate




    print(infected)
    print(grad10)

    pass

infection_rate('Period 1 Class', 'Art A');
