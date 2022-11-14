import numpy as np
import pandas as pd
from basic_formulas import *

def AnnualPremium(SinglePremium,x,m,techRate,df) -> float:
    return SinglePremium/AnnuityFactor(x,m,techRate,df)

def SinglePremiumPE(x,n,techRate,benefit,df) -> float :
    return nEx(x,n,techRate,df)*benefit

def SinglePremiumTA(x,n,techRate,benefit,df) -> float :
    return nAx(x,n,techRate,df)*benefit

def SinglePremiumEndow(x,n,techRate,benefit,df) -> float :
    return (nAx(x,n,techRate,df)+nEx(x,n,techRate,df))*benefit

def SinglePremiumWL(x,techRate,benefit,df) -> float :
    Somme=0
    for k in range(df[-1]-x):
        Somme=Somme+n_1qx(x,k,df)*techDF(k+1,techRate)
    return Somme*benefit
def SinglePremiumCombined(x,n,techRate,benefit,df_th, df_tf) -> float :
    singleTH = SinglePremiumEndow(x, n, techRate, benefit,df_th)
    singleTF = SinglePremiumEndow(x, n, techRate, benefit,df_tf)
    if singleTF > singleTH :
        return singleTF, "tf"
    else :
        return singleTH, "th"