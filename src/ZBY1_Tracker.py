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

    #TODO where RHYS's code goes

    pass


def startProgram():
    addInfectionColumn(studentRecords)
    addInfectionColumn(teacherRecords)
    addInfectionColumn(taRecords)
    initializeTransmissionRates()

    for periodNumber in range(1, 5):
        uniqueClasses = studentRecords['Period {} Class'.format(periodNumber)].unique()
        for uniqueClass in uniqueClasses:
            assignClassInfectionRates(periodNumber, uniqueClass)

    pass


startProgram()
