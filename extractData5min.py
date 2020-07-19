import pandas as pd
import glob

'''Data Cleansing: Filtering out the required data from the datafiles.
This code will read all the datafiles provided for this project. 
It then fetch the data available for 5 minutes or 300 second windows for 2 weeks starting from Feb 4,2013 for the time window of 8am to 5pm for all the users.
It will create new file for each user which only contains the required data. These new files will be saved in the folder "output" '''

# # # Tasks performed in the function create_time_slice()
# # get all the data from the csv to a dataframe.
# # Extracting the columns from the file which is required for the analysis.
# # Converting duration into second.
# # changing the datatype to reduce the size.
# # Dropping all the rows which has duration value 0.
# # For fast processing, create two dataframes week 1 and week 2. This way the program will be fetching the data for 2 weeks simultaneously.
# # eg:- Week 1 monday data and Week 2 monday data will be fetched in the same loop.
# # There are 108 windows of 300 seconds created per day. So the above optimization reduced 5 * 108 loops.
# # When the data is fetched for week1 and week2 then code will combine both weeks data into one dataframe.
# # A csv file will be created per user which only contains the required data.



def create_time_slice(files,fname):
    # Array with the starting EPOCH of all the days
    time_window_start = [1359982800000, 1360069200000, 1360155600000, 1360242000000, 1360328400000, 1360587600000, 1360674000000, 1360760400000,
                   1360846800000, 1360933200000]


    df=pd.read_excel(files)
    df=df[['doctets', 'Real First Packet', 'Duration']]
    df['Duration']=df['Duration'].div(1000)
    df['Duration'] = df['Duration'].astype('float32')
    df['doctets'] = df['doctets'].astype('uint32')
    df.drop(df[df['Duration'] == 0].index, inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1,inplace=True)
    print(df.head())
    print(df.info())
    week1_df = pd.DataFrame(columns=['doctets', 'Real First Packet', 'Duration','start', 'end'])
    week2_df = pd.DataFrame(columns=['doctets', 'Real First Packet', 'Duration','start', 'end'])
    for t in range(5): # There are 5 days in a week
        start_val1=time_window_start[t] # start epoch for week 1
        start_val2=time_window_start[t+5] # start epoch for week 2
        first_df = pd.DataFrame(columns=['doctets', 'Real First Packet', 'Duration','start', 'end'])
        second_df = pd.DataFrame(columns=['doctets', 'Real First Packet', 'Duration','start', 'end'])
        for x in range(108): # there are 108 5 minute windows in a day
            first1=start_val1+x*300000 # adding 5 minutes
            second1=start_val1+(x+1)*300000 # adding 5 minutes
            first2=start_val2+x*227000 # adding 5 minutes
            second2=start_val2+(x+1)*300000 # adding 5 minutes
            # print(first1,second1)
            new_df=df.loc[(df['Real First Packet']>=first1) & (df['Real First Packet']<second1)] # checking if "Real First Packet" falls into the window for week 1
            new_df['start']=first1
            new_df['end']=second1
            first_df=first_df.append(new_df)

            new_df1=df.loc[(df['Real First Packet']>=first2) & (df['Real First Packet']<second2)] # checking if "Real First Packet" falls into the window for week 2
            new_df1['start']=first2
            new_df1['end']=second2
            second_df=second_df.append(new_df1)
            #print(new_df1.shape)
            #print(second_df.shape)

        week1_df=week1_df.append(first_df) #adding the consolidated data of the day to the dataframe for week 1
        week2_df=week2_df.append(second_df) #adding the consolidated data of the day to the dataframe for week 2
    #print(week2_df.shape)
    week1_df=week1_df.append(week2_df) # appending week 2 data to week 1 data
    path='.\output300\\'+fname+".csv"
    week1_df.to_csv(path,index=False) # exporting the complete data for a user in a csv

if __name__ == '__main__':
    filepath = 'D:\\USF Spring semester 2020\information security\project\Information Security _ Privacy Material\\'
    files_list = glob.glob(filepath + "*.xlsx") #contains the list of all the files provided for this assignment
    for x in files_list:
        filename=x.split("\\")[-1]
        print(x,filename.split(".")[0])
        create_time_slice(x,filename.split(".")[0]) # calling the function to fetch the required data from the given data
