from datetime import datetime
import csv

nowTime = datetime.now().strftime("%H: %M: %S")
nowDate = datetime.now().strftime("%D")


filename = "experiment.csv"


with open(filename, 'a', newline="")as file:
    csvWritter = csv.writer(file)
    while True:
        inp = input("Enter your name: ")
        if inp=="x" or inp=="exit" or len(inp)<4:
            break
        else:
            cell = input("Enter your cell number: ")
            csvWritter.writerow([nowDate, nowTime, inp, cell])


file.close()