import numpy as np
import pandas as pd
from basic_formulas import *

def AnnualPremium(SinglePremium,x,m,techRate,df) -> float:
    return SinglePremium/AnnuityFactor(x,m,techRate,df)

def SinglePremiumPE(x,n,techRate,benefit,df) -> float :
    return nEx(x,n,techRate,df)*benefit

