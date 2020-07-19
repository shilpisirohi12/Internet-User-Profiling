import pandas as pd
import glob

''' This file is computing Spearman Rank Coefficient ( r1a2a, r1a2b, r2a2b ) for all the three windows.
Then generating three output files which contains computed Spearman's Rank Coefficient for each time window respectively
There will be total nine files created three for each time windows'''

# # Tasks performed in the program
# # Read the week 1 and week 2 file created in previous step ( computation.py ) for each window( 10 second, 227 second and 300 second).
# # Calculate three Spearman Rank  coefficient for each time window
# # Save the file for each Spearman Rank Coefficient in the stats.

#************************************************************
# Computing Spearman Rank Coefficient for 10 sec window
#************************************************************

w1=pd.read_csv('.\week1.csv') # reading the week 1 file for 10 second window
w2=pd.read_csv('.\week2.csv') # reading the week 2 file for 10 second window

#fetching the user name
files=glob.glob('.\output\*.csv')
users=[]
for f in files:
    users.append(f.split("\\")[-1].split(".")[0])

print(users)

data={'user':users}


#Calculating r1a2a
spearman_df1=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res=w1[f].corr(w2[f],method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df1[f]=coeff
print("***************spearman 1**********")
print(spearman_df1.head())
print(spearman_df1.shape)


#Calculating r1a2b
spearman_df2=pd.DataFrame(data) # creating data which has first column which contains name of each user
#print(spearman_df)
for f in users:
    coeff=[]
    for u in users:
        res = w1[f].corr(w2[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df2[f]=coeff
print("***************spearman 2**********")
print(spearman_df2.head())
print(spearman_df2.shape)

#Calculating r2a2b
spearman_df3=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res = w2[f].corr(w2[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df3[f]=coeff
print("***************spearman3**********")
print(spearman_df3.head())
print(spearman_df3.shape)

# Filling all NAN with 0
spearman_df1.fillna(0,inplace=True)
spearman_df2.fillna(0,inplace=True)
spearman_df3.fillna(0,inplace=True)

#Replacing 1 with 0.9999
spearman_df1.replace(1.000000 ,0.9999, inplace=True)
spearman_df2.replace(1.000000 ,0.9999, inplace=True)
spearman_df3.replace(1.000000 ,0.9999, inplace=True)

#Replacing -1 with -0.9999
spearman_df1.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df2.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df3.replace(-1.000000 ,-0.9999, inplace=True)

spearman_df1.to_csv('.\stats\\r1a2a.csv',index=False) # exporting r1a2a data for 10 second window
spearman_df2.to_csv('.\stats\\r1a2b.csv',index=False) # exporting r1a2b data for 10 second window
spearman_df3.to_csv('.\stats\\r2a2b.csv',index=False) # exporting r2a2b data for 10 second window

#************************************************************
#Computing Spearman's Rank Coefficient for 227 sec window
#************************************************************

w3=pd.read_csv('.\week1-227sec.csv') # reading the week 1 file for 227 second window
w4=pd.read_csv('.\week2-227sec.csv') # reading the week 2 file for 227 second window

#fetching the user name
files=glob.glob('.\output227\*.csv')
users=[]
for f in files:
    users.append(f.split("\\")[-1].split(".")[0])

print(users)

data={'user':users}


#Calculating r1a2a
spearman_df4=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res=w3[f].corr(w4[f],method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df4[f]=coeff
print("***************spearman 1**********")
print(spearman_df4.head())
print(spearman_df4.shape)


#Calculating r1a2b
spearman_df5=pd.DataFrame(data) # creating data which has first column which contains name of each user
#print(spearman_df)
for f in users:
    coeff=[]
    for u in users:
        res = w3[f].corr(w4[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df5[f]=coeff
print("***************spearman 2**********")
print(spearman_df5.head())
print(spearman_df5.shape)

#Calculating r2a2b
spearman_df6=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res = w4[f].corr(w4[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df6[f]=coeff
print("***************spearman3**********")
print(spearman_df6.head())
print(spearman_df6.shape)

# Filling all NAN with 0
spearman_df4.fillna(0,inplace=True)
spearman_df5.fillna(0,inplace=True)
spearman_df6.fillna(0,inplace=True)

#Replacing 1 with 0.9999
spearman_df4.replace(1.000000 ,0.9999, inplace=True)
spearman_df5.replace(1.000000 ,0.9999, inplace=True)
spearman_df6.replace(1.000000 ,0.9999, inplace=True)

#Replacing -1 with -0.9999
spearman_df4.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df5.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df6.replace(-1.000000 ,-0.9999, inplace=True)

spearman_df4.to_csv('.\stats\\r1a2a-227.csv',index=False) # exporting r1a2a data for 227 second window
spearman_df5.to_csv('.\stats\\r1a2b-227.csv',index=False) # exporting r1a2b data for 227 second window
spearman_df6.to_csv('.\stats\\r2a2b-227.csv',index=False) # exporting r2a2b data for 227 second window


#**************************************************************
# Computing Spearman's Rank coefficient for 300 second window
#**************************************************************

w5=pd.read_csv('.\week1-300sec.csv') # reading the week 1 file for 300 second window
w6=pd.read_csv('.\week2-300sec.csv') # reading the week 2 file for 300 second window

#fetching the user name
files=glob.glob('.\output300\*.csv')
users=[]
for f in files:
    users.append(f.split("\\")[-1].split(".")[0])

print(users)

data={'user':users}


#Calculating r1a2a
spearman_df7=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res=w5[f].corr(w6[f],method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df7[f]=coeff
print("***************spearman 1**********")
print(spearman_df7.head())
print(spearman_df7.shape)


#Calculating r1a2b
spearman_df8=pd.DataFrame(data) # creating data which has first column which contains name of each user
#print(spearman_df)
for f in users:
    coeff=[]
    for u in users:
        res = w5[f].corr(w6[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df8[f]=coeff
print("***************spearman 2**********")
print(spearman_df8.head())
print(spearman_df8.shape)

#Calculating r2a2b
spearman_df9=pd.DataFrame(data) # creating data which has first column which contains name of each user
for f in users:
    coeff=[]
    for u in users:
        res = w6[f].corr(w6[u], method='spearman') #calculating Spearman rank coefficient using the method from Pandas library
        coeff.append(res)
    spearman_df9[f]=coeff
print("***************spearman3**********")
print(spearman_df9.head())
print(spearman_df9.shape)

# Filling all NAN with 0
spearman_df7.fillna(0,inplace=True)
spearman_df8.fillna(0,inplace=True)
spearman_df9.fillna(0,inplace=True)

#Replacing 1 with 0.9999
spearman_df7.replace(1.000000 ,0.9999, inplace=True)
spearman_df8.replace(1.000000 ,0.9999, inplace=True)
spearman_df9.replace(1.000000 ,0.9999, inplace=True)

#Replacing -1 with -0.9999
spearman_df7.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df8.replace(-1.000000 ,-0.9999, inplace=True)
spearman_df9.replace(-1.000000 ,-0.9999, inplace=True)

spearman_df7.to_csv('.\stats\\r1a2a-300.csv',index=False) # exporting r1a2a data for 300 second window
spearman_df8.to_csv('.\stats\\r1a2b-300.csv',index=False) # exporting r1a2b data for 300 second window
spearman_df9.to_csv('.\stats\\r2a2b-300.csv',index=False) # exporting r2a2b data for 300 second window

