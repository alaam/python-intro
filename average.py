def getAverage(name, grades):
    print name

    sum = 0
    for grade in grades:
        sum = sum + grades[grade]

    average = sum / len(grades)

    print average


getAverage("Alaa", {"Math": 10,
                    "Science": 20,
                    "Gym": 25,
                    "ELA": 5,
                    "Social": 25})
getAverage("Amal", {"Math": 0,
                    "Science": 0,
                    "Gym": 5,
                    "ELA": 5,
                    "Social": 5})
