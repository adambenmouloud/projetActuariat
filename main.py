import pandas as pd
import numpy as np
from basic_formulas import *
from premiums import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    filepath_france_tf = "./TF 00-02 décalé.csv"
    filepath_france_th = "./TH 00-02 décalé.csv"

    tf_france = get_full_table_data(filepath_france_tf)
    th_france = get_full_table_data(filepath_france_th)
    print(f'Table de mortalité { filepath_france_tf[2:-4]}:\n{tf_france}\n')
    print(f'Table de mortalité {filepath_france_th[2:-4]}:\n{th_france}\n')

    x = 30 # age
    n = 25 # term
    m = 10 # payments
    techRate = 0.05 # technical rate
    benefit = 1000 # amount

    singlepremPE = SinglePremiumPE(x,n,techRate,benefit,tf_france)
    annualpremPE = AnnualPremium(singlepremPE,x,m,techRate,tf_france)

    print(f'Pure Endowment: x={x}, n={n}, m={m}, technical rate={techRate}, benefit={benefit}\nSingle premium: {singlepremPE}\nAnnual premium: {annualpremPE}\n ')

    singlepremComb, end_df = SinglePremiumCombined(x, n, techRate, benefit, th_france, tf_france)

    if end_df == "tf":
        annualpremComb = AnnualPremium(singlepremComb, x, m, techRate,tf_france)
    else:
        annualpremComb = AnnualPremium(singlepremComb, x, m, techRate,th_france)

    print(f'Combined Endowment: x={x}, n={n}, m={m}, technical rate={techRate}, benefit={benefit}\nSingle premium: {singlepremComb}\nAnnual premium: {annualpremComb}\n ')