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
    # TODO where RHYS's code goes

    pass


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

            group['Infection Rate'] = group.apply(
                lambda x: x['Infection Rate']*calculatedBaseRate, axis=1)

            #Apply health conditions
            #group = group.apply( lambda x: x['Infection Rate']*1.7 if x['Health Conditions'] is not np.NaN else x['Infection Rate']*1,axis=1)

pass


def startProgram():
    addInfectionColumn(studentRecords)
    addInfectionColumn(teacherRecords)
    addInfectionColumn(taRecords)
    initializeTransmissionRates()

    for periodNumber in range(1, numPeriods + 1):
        if periodNumber is 3:
            assignLunchInfectionRates()
        uniqueClasses = studentRecords['Period {} Class'.format(periodNumber)].unique()
        for uniqueClass in uniqueClasses:
            assignClassInfectionRates(periodNumber, uniqueClass)

    pass


startProgram()
