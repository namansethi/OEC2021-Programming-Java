import pandas as pd
import numpy as np

# Import file with data loading functions

studentRecords = pd.read_excel('../Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Student Records')
teacherRecords = pd.read_excel('../Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teacher Records')
taRecords = pd.read_excel('../Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='Teaching Assistant Records')
infectedStudents = pd.read_excel('../Resources/OEC2021_-_School_Record_Book_.xlsx', sheet_name='ZBY1 Status')


def addInfectionColumn(dataframe):
    dataframe["Infection Rate"] = "0"
    pass


def initializeTransmissionRates():
    studentRecords.dropna()
    infected_student_numbers = studentRecords.loc[studentRecords['Student Number'].isin(infectedStudents['Student ID'])]
    studentRecords['Infection Rate'] = studentRecords['Student Number'].apply(lambda x: 100 if x in infected_student_numbers['Student Number'].values else 0)
    print(studentRecords.to_string())
    pass


def startProgram():
    addInfectionColumn(studentRecords)
    initializeTransmissionRates()
    pass


startProgram()