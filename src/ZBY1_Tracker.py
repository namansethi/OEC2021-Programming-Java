from main import *
import pandas as pd
import numpy as np

# Import file with data loading functions

studentRecords = get_student_records()
teacherRecords = get_teacher_records()
taRecords = get_ta_records()
infectedStudents = get_infected_status()


def addInfectionColumn(dataframe):
    dataframe["Infection Rate"] = "0"
    pass


def initializeTransmissionRates():
    studentRecords.dropna()
    infected_student_numbers = studentRecords.loc[studentRecords['Student Number'].isin(infectedStudents['Student ID'])]
    studentRecords['Infection Rate'] = studentRecords['Student Number'].apply(
        lambda x: 100 if x in infected_student_numbers['Student Number'].values else 0)
    pass


def assignClassInfectionRates(period, classname):

    #TODO where RHYS's code goes

    pass


def startProgram():
    addInfectionColumn(studentRecords)
    addInfectionColumn(teacherRecords)
    addInfectionColumn(taRecords)
    initializeTransmissionRates()

    for x in range(1, 5):
        uniqueClasses = studentRecords['Period {} Class'.format(x)].unique()
        for y in uniqueClasses:
            assignClassInfectionRates(x, y)

    pass


startProgram()
