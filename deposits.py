# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 09:24:06 2019

@author: ethan
"""

import pandas as pd

df = pd.read_csv('All_Reports_20190331_Assets and Liabilities.csv', 
                 usecols = ['name','asset','liabeq', 'liab','dep','iddepinr']) 
                #theres a lot of shit here, these are the columns 
                #that looks kinda useful
"""   
From the documentation:
liaeq = Total liabilities, limited-life preferred stock and equity capital.
iddepinr = Estimated amount of insured deposits as a percent of total deposit liabilities before exclusions (gross) as defined in section 3(l) of the Federal Deposit Insurance Act and FDIC regulations.<br><br>Available in the FDIC Institution Directory beginning in March 2009. <br><br>NOTE: Although standard FDIC insurance coverage was temporarily raised from $100,000 to $250,000 in October 2008, institutions are required to report the source elements for this estimate based on the $100,000 coverage limit through June 2009. Beginning with the September 30, 2009 reporting period, institutions are required to report based on the $250,000 coverage limit. <br><br>RIS definition: IDDEPINR = (DEPINS / DEPBEFEX) *100"
dep = The sum of all deposits including demand deposits, money market deposits, other savings deposits, time deposits and deposits in foreign offices.

"""
df['insuredDeposits'] = df['dep'] * df['iddepinr']/100
print('Total Insured Deposits:', df['insuredDeposits'].sum())
print('Percentage of funding:', df['insuredDeposits'].sum()/df['liabeq'].sum( ))