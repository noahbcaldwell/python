# Noah Caldwell
# 06/11/2022
# CSCI 5015 - Python for Data Science
# Project 2

filename = "data/bls-unemployment-level.csv"

# Intialize Lists
year = []
level = []

def openFile():
    with open(filename) as file:
        i = 0
        for line in file:
            if i >= 1:
                parts = line.split(",")
                ayear = int(parts[1])
                alevel = int(parts[4])
                year.append(ayear)
                level.append(alevel)
            i += 1

# Get the unemployment levels for a given year
def getLevelsByYear(yearToFind, year, level):
    levelsForYear = []
    for i in range(len(year)):
        if year[i] == yearToFind:
            levelsForYear.append(level[i])
    return levelsForYear

# Get the mean unemployment for a given year
def getMean(items):
    assert len(items) > 0
    total = sum(items)
    length = len(items)
    return total / length

# Get the standard deviation for a given year 
def getStandardDeviation(mean, data):
    deviations = [(i - mean) ** 2 for i in data]
    variance = sum(deviations) / len(data)
    return variance ** 0.5

# Load the file
openFile()

# Store the unemployment level for a given year in a variable
levelsFor2020 = getLevelsByYear(2020, year, level)
levelsFor2021 = getLevelsByYear(2021, year, level)
levelsFor2022 = getLevelsByYear(2022, year, level)

# Store the mean unemployment level for a given year in a variable
mean2020 = getMean(levelsFor2020)
mean2021 = getMean(levelsFor2021)
mean2022 = getMean(levelsFor2022)

# Store the standard deviation for a given year in a variable
standardDeviation2020 = getStandardDeviation(mean2020, levelsFor2020)
standardDeviation2021 = getStandardDeviation(mean2021, levelsFor2021)
standardDeviation2022 = getStandardDeviation(mean2022, levelsFor2022)

# Create a text string with the mean and standard deviation of a given year
res2020 = "Year 2020. Mean: " + str(round(mean2020, 2)) + ", Standard Deviation: " + str(round(standardDeviation2020, 2)) 
res2021 = "Year 2021. Mean: " + str(round(mean2021, 2)) + ", Standard Deviation: " + str(round(standardDeviation2021, 2)) 
res2022 = "Year 2022. Mean: " + str(round(mean2022, 2)) + ", Standard Deviation: " + str(round(standardDeviation2022, 2))

# Print the results
print(res2020)
print(res2021)
print(res2022)