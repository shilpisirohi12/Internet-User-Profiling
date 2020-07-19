import pandas as pd
import math

'''Calculating Z-value and P-value based on the values of Spearman Rank coefficient computed in previous step ( StatisticalComputations.py)
and it will create two files for each time window; one for z-Values and one for p-Values'''

# # Tasks performed in the program
# # method z_and_p() takes  input: total  number of windows in the time window, file names for spearman rank coefficient and output filenames
# # It is fairly simple method. It is calculating the Z-values based on the steps given in the project document.
# # It then called pFun() method to calculate p-Values
# # method pFun() is the straightforward Python implementation of the program given in the project document.
# # Separate file of z-Values and p-Values are created and stored in the folder 'stats


#************************************************************
# Computing pValues
#************************************************************
def pFun(z):
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429

    if z < 0.0:
        sign =  -1
    else:
        sign = 1

    x = abs(z) / math.sqrt(2.0)
    t = 1.0/(1.0 + p*x)
    erf = 1.0 - (((((a5*t + a4)*t)+a3)*t+a2)*t+a1)*t*math.exp(-x*x)
    res = 0.5*(1.0+ sign*erf)
    return res

#************************************************************
# Computing zValues
#************************************************************

def z_and_p(N,z,p,f1,f2,f3):
    print('.\stats\\'+f1+ '.csv')
    spearman_df1 = pd.read_csv('.\stats\\'+f1+ '.csv')
    spearman_df2 = pd.read_csv('.\stats\\'+f2+ '.csv')
    spearman_df3 = pd.read_csv('.\stats\\'+f3+ '.csv')

    user_lst = spearman_df1['user']
    z_df = pd.DataFrame({'user': user_lst})
    p_df = pd.DataFrame({'user': user_lst})
    print(z_df)

    for x in range(54): # there are 54 users that's why there are 54 iterations.
        lst=[]
        plst=[]
        for y in range(54): # there are 54 users that's why there are 54 iterations.
            rm2 = (spearman_df1.iloc[x][y+1]*spearman_df1.iloc[x][y+1] + spearman_df2.iloc[x][y+1]*spearman_df2.iloc[x][y+1])/2
            f= (1 - spearman_df3.iloc[x][y+1])/(2*(1-rm2))
            h = (1-(f*rm2))/(1-rm2)
            Z1a2a=(math.log((1+spearman_df1.iloc[x][y+1])/(1-spearman_df1.iloc[x][y+1])))/2
            Z1a2b=(math.log((1+spearman_df2.iloc[x][y+1])/(1-spearman_df2.iloc[x][y+1])))/2
            print(spearman_df3.iloc[x][y+1],'   ',1-spearman_df3.iloc[x][y+1])
            Z = (Z1a2a-Z1a2b)*(math.sqrt(N*5-3)/(2*(1-spearman_df3.iloc[x][y+1])*h))
            lst.append(Z)
            plst.append(pFun(Z))
        z_df[user_lst[x]] = lst
        p_df[user_lst[x]] = plst

    z_df.to_csv('.\stats\\'+z+'.csv',index=False) # exporting z-Val csv
    p_df.to_csv('.\stats\\'+p+'.csv',index=False) # exporting p-Val csv


if __name__ == '__main__':
    print("hello world")
    #Calculations for 10 second window
    N = 3240 # number of windows in a day for 10 second windows
    z_and_p(N,z='zValues',p='pValues',f1='r1a2a',f2='r1a2b',f3='r2a2b') # Calling the function for 10 second window

    #Calculations for 227 second window
    N = 142 # number of windows in a day for 227 second windows
    z_and_p(N,z='zValues-227',p='pValues-227',f1='r1a2a-227',f2='r1a2b-227',f3='r2a2b-227') # Calling the function for 227 second window

    #Calculations for 300 second window
    N = 108 # number of windows in a day for 300 second windows
    z_and_p(N,z='zValues-300',p='pValues-300',f1='r1a2a-300',f2='r1a2b-300',f3='r2a2b-300') # Calling the function for 300 second window




