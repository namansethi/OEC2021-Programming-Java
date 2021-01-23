from main import *
import pandas as pd
import numpy as np

# Import file with data loading functions

studentRecords = get_student_records()
teacherRecords = get_teacher_records()
taRecords = get_ta_records()
infectedPeople = get_infected_status()


def addInfectionColumn(dataframe):
    dataframe["Infection Rate"] = "0"
    pass


def initializeTransmissionRates():
    studentRecords.dropna()
    infected_student_numbers = studentRecords.loc[studentRecords['Student Number'].isin(infectedPeople['Student ID'])]
    studentRecords['Infection Rate'] = studentRecords['Student Number'].apply(
        lambda x: 100 if x in infected_student_numbers['Student Number'].values else 0)

    infected_ta = taRecords.loc[taRecords['Last Name'].isin(infectedPeople['Last Name'])]
    taRecords['Infection Rate'] = taRecords['Last Name'].apply(
        lambda x: 100 if x in infected_ta['Last Name'].values else 0)

    pass


def assignClassInfectionRates(period, className):


    course_and_period = studentRecords.loc[studentRecords[period] == className]


    infected = course_and_period.loc[course_and_period['Infection Rate'] != 'NaN']

    ta = taRecords.loc[taRecords[period] == className]

    teacher = teacherRecords.loc[teacherRecords['Class'] == className]



    if (ta.empty):
        num = len(course_and_period) + 1

    else:
        num = len(course_and_period) + 2

    grad9 = infected.loc[infected['Grade'] == 9]
    col_one_list = grad9['Infection Rate'].tolist()
    multiplied_list = [(element / 100) * (3 / num) for element in col_one_list]
    grade9infect = calc_infect_rate(multiplied_list)

    grad10 = infected.loc[infected['Grade'] == 10]
    col_one_list = grad10['Infection Rate'].tolist()
    multiplied_list = [(element / 100) * (3 / num) for element in col_one_list]
    grade10infect = calc_infect_rate(multiplied_list )

    grad11 = infected.loc[infected['Grade'] == 11]
    col_one_list = grad11['Infection Rate'].tolist()
    multiplied_list = [(element / 100) * (3 / num) for element in col_one_list]
    grade11infect = calc_infect_rate(multiplied_list)

    grad12 = infected.loc[infected['Grade'] == 12]
    col_one_list = grad12['Infection Rate'].tolist()
    multiplied_list = [(element / 100) * (3 / num) for element in col_one_list]
    grade12infect = calc_infect_rate(multiplied_list)



    if (teacher.empty):
        teachInfect = 0
    else:
        teachInfect = int(teacher['Infection Rate'])/100
    if (ta.empty):
        TaInfect = 0
    else:
        TaInfect = int(ta['Infection Rate'])/100




    for index, row in course_and_period.iterrows():

        grade = row['Grade']
        studNum = row['Student Number']

        healthcondition = row['Health Conditions']
        infection = row['Infection Rate']/100

        if (healthcondition != 'nan'):
            healthcondition = 'true'

        if (infection == 1):
            continue

        if grade == 9:
            if healthcondition:
                list = [grade9infect, grade10infect, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [infection, grade9infect, grade10infect, grade11infect, grade12infect]
                infection = 1 - (1 - infection) * (1-calc_infect_rate(list))

        if grade == 10:
            if healthcondition:
                list = [grade9infect * 1.25, grade10infect, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [grade9infect * 1.25, grade10infect, grade11infect, grade12infect]
                infect = calc_infect_rate(list)

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)

        if grade == 11:
            if healthcondition:
                list = [grade9infect * 1.5, grade10infect * 1.25, grade11infect, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [grade9infect * 1.5, grade10infect * 1.25, grade11infect, grade12infect]
                infect = calc_infect_rate(list)

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)

        if grade == 12:
            if healthcondition:
                list = [grade9infect * 1.75, grade10infect * 1.5, grade11infect * 1.25, grade12infect]
                infect = calc_infect_rate(list)
                infect = infect * 1.7

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)
            else:
                list = [grade9infect * 1.75, grade10infect * 1.5, grade11infect * 1.25, grade12infect]
                infect = calc_infect_rate(list)

                if (infect >= 1):
                    infection = 1
                else:
                    infection = 1 - (1 - infection) * (1 - infect)



        infection = 1 - ((1 - infection) * (1 - 3 / num * teachInfect))*0.80
        infection = 1 - ((1 - infection) * (1 - 3 / num * TaInfect))*0.80
        # note working need to be changed




        studentRecords.loc[studentRecords['Student Number'] == studNum, 'Infection Rate'] = infection*100


    if(teacher.empty):
        infection = 0
    else:
        teaching = teacher['Teacher Number']
        infection = int(teacher['Infection Rate']) / 100
        list = [grade9infect, grade10infect, grade11infect, grade12infect]
        infection = (1- (1-infection)*(1-calc_infect_rate(list))) * 0.2
        infection = 1 - (1 - infection) * (1 - 3 / num * TaInfect )

        teacherRecords.loc[teacherRecords['Teacher Number'] == teaching.iloc[0], 'Infection Rate'] = infection*100

    if(ta.empty):
        infection = 0
    else:
        teaching = ta['First Name']
        infection = int(ta['Infection Rate']) / 100
        list = [grade9infect, grade10infect, grade11infect, grade12infect]
        infection = (1 - (1 - infection) * (1 - calc_infect_rate(list))) * 0.2
        infection = 1 - (1 - infection) * (1 - 3 / num * teachInfect)
        taRecords.loc[taRecords['First Name'] == teaching.iloc[0], 'Infection Rate'] = infection * 100

    #print(infected)
   # print(grad10)

    pass
    #TODO where RHYS's code goes



def calc_infect_rate(list_of_rates):
    intermediate_rate = 1
    for rate in list_of_rates:
        intermediate_rate = intermediate_rate * (1 - rate)

    return 1 - intermediate_rate

def startProgram():
    addInfectionColumn(studentRecords)
    addInfectionColumn(teacherRecords)
    addInfectionColumn(taRecords)
    initializeTransmissionRates()

    for periodNumber in range(1, 5):
        uniqueClasses = studentRecords['Period {} Class'.format(periodNumber)].unique()
        for uniqueClass in uniqueClasses:
            assignClassInfectionRates('Period {} Class'.format(periodNumber), uniqueClass)

    pass


startProgram()
