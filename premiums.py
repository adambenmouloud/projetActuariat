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

def SinglePremiumEnd(x,n,techRate,benefit,df) -> float :
    singleTA = SinglePremiumTA(x, n, techRate, benefit,df)
    singlePE = SinglePremiumPE(x, n, techRate, benefit,df)
    return singleTA+singlePE
