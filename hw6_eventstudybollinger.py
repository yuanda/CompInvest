'''
Event study of the bollinger band

@author Alicia Wang
@date 5 novembre 2014
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkstudy.EventProfiler as ep

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

# Internal Imports
from GetDataLocal import GetDataLocalYahoo
from hw5_bollingerbands import ComputeBollingerBands

def BollingerEventTest(startd, endd, ls_symbols, lookbackdates):
    
    bolval = ComputeBollingerBands(ls_symbols, startd, endd, lookbackdates)
    ts_market = bolval['SPY']
    
    # Time stamps for the event range
    ldt_timestamps = df_close.index    
    
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN   
    
    ref        = -2.0
    market_ref =  1.0
    
    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            if bolval[s_sym][ldt_timestamps[i-1]] >= ref \
               and bolval[s_sym][ldt_timestamps[i]] <= ref \
               and ts_market[ldt_timestamps[i]] >= 1.0:
                df_event[s_sym][ldt_timestamps[i]] = 1
    
    return df_events

         
#-----------------------------------------------------------
def main():
    '''main function'''
    
    # Construct the two symbol lists SP 500 of 2008 and 2012
    dataobj = da.DataAccess('Yahoo')    
    
    symbols12 = dataobj.get_symbols_from_list("sp5002012")
    symbols12.append('SPY') 
    
    # Set the start and end dates of the analysis
    startd = dt.datetime(2008, 1,  1 )
    endd   = dt.datetime(2009, 12, 31)  
    
    lookbackdates = 20
    
    df_events = BollingerEventTest(startd, endd, symbols12, lookbackdates)
    
    d_data = GetDataLocalYahoo(startd, endd, symbols12)
    
    filename = "BollingerEventStudy12.9.pdf"
    
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                    s_filename = filename, b_market_neutral=True, 
                    b_errorbars = True, s_market_sym='SPY')    


#-----------------------------------------------------------
if __name__ == '__main__':
    main()