import pandas as pd
import glob as glob

'''  Basic Computation: Calculating doctet/duration and averaging that if more than 1 value is available for a window. 
Create data for all the time windows and  save in two files for each week respectively.
This computation is performed for all the three windows( 10 second, 227 second and 5 minutes ) in this program.'''


# # Tasks performed in this program
# # Fetch the datafiles user wise which were created previously by the programs extractData10sec.py, extractData227sec.py and extractData5min.py
# # Check if the file contains the data for the time window. If no data is available then put data '0.0001' for that window
# # If data is available then check if more than one row of data is available for the given time window.
# # if there are more than row then first compute doctet/duration and then calculate the average for all the rows of data.
# # If only one row of data is given for a time window then we will put the calculated doctet/duration as the final final for that window.
# # Here the calculation for 2 weeks will parallel as it was for Data Extraction in the previous step.
# # When data for week1 and week 2 is computed then data will be exported in csv.
# # Number of rows in the csv is equal to the number of time windows in a weak.
# # eg: for 5 min time window, the total number of data rows in the week1-300sec.csv will be 540.
# # Same will be for week2-227sec.csv. It will have 540 rows of data.
# # There is one column for each other which contains the data for that user user for all the time window.
# # So there will be total of 54 columns of user data, each column representing one user.
# # Code for the calculation for all the 3 windows will be in this program only.
# # Total six csv will be created at the end of this program. Two csv files for each time window.


# Array with the starting EPOCH of all the days
time_window_w1 = [1359982800000, 1360069200000, 1360155600000, 1360242000000, 1360328400000]
time_window_w2 = [1360587600000, 1360674000000, 1360760400000, 1360846800000, 1360933200000]

files = glob.glob('.\output\*.csv') # list of all the files of 10 second window
files227 = glob.glob('.\output227\*.csv') # list of all the files of 227 second window
files300 = glob.glob('.\output300\*.csv') # list of all the files of 5 minute window

#************************************************************
# Computing for 10 second window
#************************************************************

## creating 10 sec window
start_w1 = []
end_w1 = []
start_w2 = []
end_w2 = []

for days in range(5):
    start_val1 = time_window_w1[days] # Fetching start epoch for day for week 1
    start_val2 = time_window_w2[days] # Fetching start epoch for day for week 2
    for x in range(3240): # number of windows in a day for 10 second window
        w1_start = start_val1 + x * 10000
        w1_end = start_val1 + (x + 1) * 10000
        w2_start = start_val2 + x * 10000
        w2_end = start_val2 + (x + 1) * 10000
        start_w1.append(w1_start)
        end_w1.append(w1_end)
        start_w2.append(w2_start)
        end_w2.append(w2_end)


data_w1 = {'start': start_w1,
           'end': end_w1}
data_w2 = {'start': start_w2,
           'end': end_w2}

w1_df = pd.DataFrame(data_w1) # adding column start and end in the dataframe for week 1
w2_df = pd.DataFrame(data_w2) # adding column start and end in the dataframe for week 2

# Creating week1 and week2 files for 10 second window
for f in files:
    fname = f.split("\\")[-1].split(".")[0] #fetching username from the filename
    print(fname)
    df = pd.read_csv(f) # read csv for the user
    lst1 = []
    lst2 = []
    for w1, w2 in zip(start_w1, start_w2): # looping through all the windows for week1 and week2. Here loop will execute for 16200 times
        idx1 = -1
        idx1 = df[df['start'] == w1].index # checking if data is available for the window for week1
        if idx1.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx1]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst1.append(val)
        else:
            lst1.append(0.0001) # if data is not available then put the value 0.0001 for that window.
        idx2 = -1
        idx2 = df[df['start'] == w2].index # checking if data is available for the window for week2
        if idx2.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx2]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst2.append(val)
        else:
            lst2.append(0.0001) # if data is not available then put the value 0.0001 for that window.

    w1_df[fname] = lst1 # appending new column for week 1 data user wise.
    w2_df[fname] = lst2 # appending new column for week 2 data user wise.

w1_df.to_csv('.\week1.csv') # exporting the week 1 file for 10 second window
w2_df.to_csv('.\week2.csv') # exporting the week 2 file for 10 second window

#************************************************************
# Computing for 227 second window
#************************************************************

## creating 227 sec window
start_227w1 = []
end_227w1 = []
start_227w2 = []
end_227w2 = []

for days in range(5):
    start_val1 = time_window_w1[days] # Fetching start epoch for day for week 1
    start_val2 = time_window_w2[days] # Fetching start epoch for day for week 2
    for x in range(142): # number of windows in a day for 227 second window
        w1_start = start_val1 + x * 227000
        w1_end = start_val1 + (x + 1) * 227000
        w2_start = start_val2 + x * 227000
        w2_end = start_val2 + (x + 1) * 227000
        start_227w1.append(w1_start)
        end_227w1.append(w1_end)
        start_227w2.append(w2_start)
        end_227w2.append(w2_end)

data_227w1 = {'start': start_227w1,
              'end': end_227w1}
data_227w2 = {'start': start_227w2,
              'end': end_227w2}

w1_227df = pd.DataFrame(data_227w1) # adding column start and end in the dataframe for week 1
w2_227df = pd.DataFrame(data_227w2) # adding column start and end in the dataframe for week 2

# Creating week1 and week2 files for 227 second window
for f in files227:
    fname = f.split("\\")[-1].split(".")[0] #fetching user name from the filename
    print(fname)
    df = pd.read_csv(f) # read csv for the user
    lst1 = []
    lst2 = []
    for w1, w2 in zip(start_227w1, start_227w2): # looping through all the windows for week1 and week2. Here loop will execute for 710 times
        idx1 = -1
        idx1 = df[df['start'] == w1].index # checking if data is available for the window for week1
        if idx1.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx1]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst1.append(val)
        else:
            lst1.append(0.0001) # if data is not available then put the value 0.0001 for that window.
        idx2 = -1
        idx2 = df[df['start'] == w2].index # checking if data is available for the window for week2
        if idx2.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx2]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst2.append(val)
        else:
            lst2.append(0.0001) # if data is not available then put the value 0.0001 for that window.

    w1_227df[fname] = lst1 # appending new column for week 1 data user wise.
    w2_227df[fname] = lst2 # appending new column for week 2 data user wise.

w1_227df.to_csv('.\week1-227sec.csv') # exporting the week 1 file for 227 second window
w2_227df.to_csv('.\week2-227sec.csv') # exporting the week 2 file for 227 second window

#************************************************************
# Computing for 300 second window
#************************************************************

## creating 5 min/ 300 second window
start_300w1 = []
end_300w1 = []
start_300w2 = []
end_300w2 = []

for days in range(5):
    start_val1 = time_window_w1[days] # Fetching start epoch for day for week 1
    start_val2 = time_window_w2[days] # Fetching start epoch for day for week 2
    for x in range(108): # number of windows in a day for 300 second window
        w1_start = start_val1 + x * 300000
        w1_end = start_val1 + (x + 1) * 300000
        w2_start = start_val2 + x * 300000
        w2_end = start_val2 + (x + 1) * 300000
        start_300w1.append(w1_start)
        end_300w1.append(w1_end)
        start_300w2.append(w2_start)
        end_300w2.append(w2_end)

data_300w1 = {'start': start_300w1,
              'end': end_300w1}
data_300w2 = {'start': start_300w2,
              'end': end_300w2}

w1_300df = pd.DataFrame(data_300w1) # adding column start and end in the dataframe for week 1
w2_300df = pd.DataFrame(data_300w2) # adding column start and end in the dataframe for week 2


# Creating week1 and week2 files for 300 sec
for f in files300:
    fname = f.split("\\")[-1].split(".")[0] #fetching user name from the filename
    print(fname)
    df = pd.read_csv(f) # read csv for the user
    lst1 = []
    lst2 = []
    for w1, w2 in zip(start_300w1, start_300w2): # looping through all the windows for week1 and week2. Here loop will execute for 540 times
        idx1 = -1
        idx1 = df[df['start'] == w1].index # checking if data is available for the window for week1
        if idx1.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx1]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst1.append(val)
        else:
            lst1.append(0.0001) # if data is not available then put the value 0.0001 for that window.
        idx2 = -1
        idx2 = df[df['start'] == w2].index # checking if data is available for the window for week2
        if idx2.shape[0] > 0: # checking if data is there for a given window
            temp_df = df.loc[idx2]
            arry = []
            # Taking the average if more than one row of data is available for the window
            for r in temp_df.itertuples():
                arry.append(r[1] / r[3])
            val = sum(arry) / len(arry)
            # print(val)
            lst2.append(val)
        else:
            lst2.append(0.0001) # if data is not available then put the value 0.0001 for that window.

    w1_300df[fname] = lst1 # appending new column for week 1 data user wise.
    w2_300df[fname] = lst2 # appending new column for week 2 data user wise.

w1_300df.to_csv('.\week1-300sec.csv') # exporting the week 1 file for 300 second window
w2_300df.to_csv('.\week2-300sec.csv') # exporting the week 2 file for 300 second window
