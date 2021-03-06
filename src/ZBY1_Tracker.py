from main import *
import pandas as pd
import numpy as np
import random

# Import file with data loading functions

studentRecords = get_student_records()
teacherRecords = get_teacher_records()
taRecords = get_ta_records()
infectedPeople = get_infected_status()
numPeriods = 4
youngestGrade = 9
oldestGrade = 12
studentsInGroup = 5


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

        if isinstance(healthcondition, str):
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




        studentRecords.loc[studentRecords['Student Number'] == studNum, 'Infection Rate'] = infection


    if(teacher.empty):
        infection = 0
    else:
        teaching = teacher['Teacher Number']
        infection = int(teacher['Infection Rate']) / 100
        list = [grade9infect, grade10infect, grade11infect, grade12infect]
        infection = (1- (1-infection)*(1-calc_infect_rate(list))) * 0.2
        infection = 1 - (1 - infection) * (1 - 3 / num * TaInfect )

        teacherRecords.loc[teacherRecords['Teacher Number'] == teaching.iloc[0], 'Infection Rate'] = infection

    if(ta.empty):
        infection = 0
    else:
        teaching = ta['First Name']
        infection = int(ta['Infection Rate']) / 100
        list = [grade9infect, grade10infect, grade11infect, grade12infect]
        infection = (1 - (1 - infection) * (1 - calc_infect_rate(list))) * 0.2
        infection = 1 - (1 - infection) * (1 - 3 / num * teachInfect)
        taRecords.loc[taRecords['First Name'] == teaching.iloc[0], 'Infection Rate'] = infection

    #print(infected)
   # print(grad10)

    pass
    #TODO where RHYS's code goes


def calculateBaseRateInfection(list_of_rates):
    intermediate_rate = 1
    for rate in list_of_rates:
        intermediate_rate = intermediate_rate * (1 - rate)

    calculatedInfectionPercentage = (1 - intermediate_rate) * 100

    return calculatedInfectionPercentage


def assignLunchInfectionRates():
    global studentRecords
    for gradeNumber in range(youngestGrade, oldestGrade + 1):
        gradeStudents = studentRecords.loc[studentRecords['Grade'] == gradeNumber]
        shuffled = gradeStudents.sample(frac=1)
        groupings = [shuffled.iloc[i:i + studentsInGroup] for i in range(0, len(shuffled) - studentsInGroup + 1, studentsInGroup)]
        for group in groupings:
            infection_rates = group['Infection Rate'].values.tolist()
            percentageCorrected = []
            for percentage in infection_rates:
                percentageCorrected.append(percentage/100)
            calculatedBaseRate = calculateBaseRateInfection(percentageCorrected)

            for index, row in group.iterrows():
                Id = row['Student Number']
                healthcondition = row['Health Conditions']

                infection = row['Infection Rate']/100




                if isinstance(healthcondition, str):


                    healthcondition = 'true'

                if(healthcondition):
                    calculatedBaseRate = calculatedBaseRate*1.7/100
                    if(calculatedBaseRate >= 1):
                        infection = 1
                    else:
                        infection = 1 - (1 - infection)*(1-calculatedBaseRate/100)
                else:
                    infection = 1 - (1 - infection)*(1-calculatedBaseRate/100)

                studentRecords.loc[studentRecords['Student Number'] == Id, 'Infection Rate'] = infection*100

           # group['Infection Rate'] = group['Infection Rate'].apply(
             #   lambda x: x['Infection Rate']*calculatedBaseRate, axis=1)

            #Apply health conditions
            #group = group.apply( lambda x: x['Infection Rate']*1.7 if x['Health Conditions'] is not np.NaN else x['Infection Rate']*1,axis=1)

pass

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

    for periodNumber in range(1, numPeriods + 1):
        if periodNumber == 3:
            assignLunchInfectionRates()
        uniqueClasses = studentRecords['Period {} Class'.format(periodNumber)].unique()
        for uniqueClass in uniqueClasses:
            assignClassInfectionRates('Period {} Class'.format(periodNumber), uniqueClass)
    print(studentRecords.to_string())
    studentRecords.to_excel("./Resources/StudentRecordsWithInfections.xlsx")
    teacherRecords.to_excel("./Resources/TeacherRecordsWithInfections.xlsx")
    taRecords.to_excel("./Resources/TARecordsWithInfections.xlsx")
    pass


startProgram()
