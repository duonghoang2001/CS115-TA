# Lab 11 Key
# Author:  Duong Hoang
# Email:  duong.hoang@uky.edu
# Section: 003

'''
    Purpose: process patient temperatures
    Pre-cond: a patient number (str), 3 temperature readings (Fahrenheit, floats)
    Post-cond: a list in which each entry is a 2-element list, the patient number (str)
                and the average of the 3 temperatures (float, 2 decimal place),
                reports number of patients processed, diagnosis, and fever and 
                low temperature percentages (floats, 1 decimal places) when there
                are some patients processed
'''

def main():
    # print prompts
    print("Enter patient number and three temperature readings")
    print("Enter blank line to stop entering data")
    # initialize 
    patient_list = []
    fever_ct = 0
    chill_ct = 0
    # get inputs until user enters a blank line
    entry = input("Enter patient: ")
    while entry != "":
        # replace commas with spaces then split data on whitespace
        data = entry.replace(",", " ").split()
        # calculate average temperature
        avg_temp = (float(data[1]) + float(data[2]) + float(data[3])) / 3
        # add patient number and average temperature to the list
        patient_list.append([data[0], avg_temp])
        # get next user input
        entry = input("Enter patient: ")
    # print report header
    print("\nPT\t  AVG\t\tDiagnosis")
    # print each patient's report along with diagnosis
    for i in range(len(patient_list)):
        # get patient's average temperature
        temp = patient_list[i][1]
        # initialize diagnosis to empty
        # assuming the temperature is inside the range 95.0 to 98.7
        diagnosis = ""
        # if the temperature average is higher than 98.7
        if temp > 98.7:
            # the diagnosis is "fever"
            diagnosis = "fever"
            fever_ct += 1
        # if the temperature is less than 95.0,
        elif temp < 95.0:
            # the diagnosis is "chilled"
            diagnosis = "chilled"
            chill_ct += 1
        
        # print report
        print("{}\t{:>6.2f}\t\t{}".format(patient_list[i][0], temp, diagnosis))
    # print number of patients processed
    print("There were", len(patient_list), "patients processed")
    # calculate stats about fever and low temperature if there were patients processed
    if len(patient_list) > 0:
        fever_percentage = fever_ct / len(patient_list) * 100
        chill_percentage = chill_ct / len(patient_list) * 100
        # print stats about number and percentage of fever and chilled patients
        print()
        print("{} had a fever ({:.1f}%)".format(fever_ct, fever_percentage))
        print("{} had a low temperature ({:.1f}%)".format(chill_ct, chill_percentage))

main()

'''
Test case: 2 patients
A patient has the same temperature three times, with an average that is a fever;
The other has the same temperature three times, with an average that is a chill.
>> 98765, 99.0, 99.0, 99.0
>> 45667  95.1  94.2, 93.9
>>
Output:
    PT        AVG           Diagnosis
    98765    99.00          fever
    45667    94.40          chilled
    There were 2 patients processed

    1 had a fever (50.0%)
    1 had a low temperature (50.0%)
'''



