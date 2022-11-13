import pandas as pd
import numpy as np
from basic_formulas import *
from premiums import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    filepath = "./TH 00-02 décalé.csv"

    mortality_table = get_full_table_data(filepath)
    print(f'{mortality_table}\n')

    x = 30 # age
    n = 25 # term
    m = 10 # payments
    techRate = 0.02 # technical rate
    benefit = 1000 # amount

    singleprem = SinglePremiumPE(x,n,techRate,benefit,mortality_table)
    annualprem = AnnualPremium(singleprem,x,m,techRate,mortality_table)

    print(f'Pure Endowment: x={x}, n={n}, m={m}, technical rate={techRate}, benefit={benefit}\n\nSingle premium: {singleprem}\nAnnual premium: {annualprem}\n ')
