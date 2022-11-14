import pandas as pd
import numpy as np

def get_full_table_data(filepath) -> pd.DataFrame :

    df = pd.read_csv( filepath, sep=',', header=0)
    cohort_size = 100000
    # df['qx'] = df['qx'].apply(lambda x: np.round(x*cohort_size) )
    # df['qx'] = df['qx'].astype(int)
    df['lx'] = np.ndarray.astype( np.zeros(len(df.Age)) + cohort_size, int )
    # df['lx'][0] =

    for i in range(1,len(df.Age) ) :
        df.at[i, 'lx'] = np.round( df['lx'][i-1]*(1-df['qx'][i-1]) )

    df['dx'] = np.ndarray.astype( np.zeros(len(df.Age)), int )

    for i in range(0,len(df.Age) ) :
        df.at[i,'dx'] = np.round( df['lx'][i]*df['qx'][i])

    return df

def lx(x,df) -> int :
    return df.loc[ df['Age'] == x, 'lx'].item()

def qx(x,df) -> float :
    return df.loc[ df['Age'] == x, 'qx'].item()

def n_lqx(x,n,df) -> float :
    return (lx(x + n,df) - lx(x + n + 1,df)) / lx(x,df)

def n_1qx(x,n,df) -> float :
    return (lx(x + n,df) - lx(x + n + 1,df)) / lx(x,df)

def npx(x,n,df) -> int :
    return lx(x+n,df)/lx(x,df)

def nEx(x,n,techRate,df) -> float :
    return npx(x,n,df) * techDF(n,techRate)

def nAx(x,n,techRate,df) -> float :
    ActSum = 0
    for h in range(n):
        ActSum += n_lqx(x,n,df)*techDF(h+1,techRate)
    return ActSum

def techDF(h, techRate) ->  float :
    return 1/( (1+techRate)**h )

def AnnuityFactor(x,m,techRate,df) -> float :
    ActSum = 0
    for h in range(m):
        ActSum += nEx(x,h,techRate,df)
    return ActSum

