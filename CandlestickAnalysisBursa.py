import pandas as pd
import talib
import os
pd.set_option('expand_frame_repr', False)

pattern_name = ['CDL2CROWS','CDL3BLACKCROWS','CDL3INSIDE','CDL3LINESTRIKE','CDL3OUTSIDE',
                'CDL3STARSINSOUTH','CDL3WHITESOLDIERS','CDLABANDONEDBABY','CDLADVANCEBLOCK',
                'CDLBELTHOLD','CDLBREAKAWAY','CDLCLOSINGMARUBOZU','CDLCONCEALBABYSWALL',
                'CDLCOUNTERATTACK','CDLDARKCLOUDCOVER','CDLDOJI','CDLDOJISTAR',
                'CDLDRAGONFLYDOJI','CDLENGULFING','CDLEVENINGDOJISTAR','CDLEVENINGSTAR',
                'CDLGAPSIDESIDEWHITE','CDLGRAVESTONEDOJI','CDLHAMMER','CDLHANGINGMAN',
                'CDLHARAMI','CDLHARAMICROSS','CDLHIGHWAVE','CDLHIKKAKE','CDLHIKKAKEMOD',
                'CDLHOMINGPIGEON','CDLIDENTICAL3CROWS','CDLINNECK','CDLINVERTEDHAMMER','CDLKICKING',
                'CDLKICKING','CDLKICKINGBYLENGTH','CDLLADDERBOTTOM','CDLLONGLEGGEDDOJI',
                'CDLLONGLINE','CDLMARUBOZU','CDLMATCHINGLOW','CDLMATHOLD','CDLMORNINGDOJISTAR',
                'CDLMORNINGSTAR','CDLONNECK','CDLPIERCING','CDLRICKSHAWMAN','CDLRISEFALL3METHODS'
                'CDLSEPARATINGLINES','CDLSHOOTINGSTAR','CDLSHORTLINE','CDLSPINNINGTOP',
                'CDLSTALLEDPATTERN','CDLSTICKSANDWICH','CDLTAKURI','CDLTASUKIGAP','CDLTHRUSTING',
                'CDLTRISTAR','CDLUNIQUE3RIVER','CDLUPSIDEGAP2CROWS','CDLXSIDEGAP3METHODS']

days = [1,5,10,30]

path = os.getcwd()
print('current working directory:',path)
stock_code_list = []
for root, dirs, files in os.walk(path):
    if files:
        for f in files:
            if '.csv' in f:
                stock_code_list.append(f.split('.csv')[0])

output = pd.DataFrame()
final_output = pd.DataFrame(columns=['Pattern', 'Win Rate (1 Day)', 'Win Rate (5 Days)','Win Rate (10 Days)',
                                     'Win Rate (30 Days)'])

for pattern in pattern_name:
    for code in stock_code_list:
        df = pd.read_csv(code + '.csv', parse_dates=[1])

        for i in days:
            df['Gains after ' + str(i) + ' days'] = df['Close'].shift(-i)/df['Close'] - 1

        df[pattern] = getattr(talib, pattern)(df['Open'].astype(float).values, df['High'].astype(float).values,
                                                        df['Low'].astype(float).values,df['Close'].astype(float).values)

        pattern_df = df[df[pattern] != 0]
        output = output.append(pattern_df)

    try:
        bullish_output = output[output[pattern]>0]
        OneDayWinRate = len(bullish_output.loc[bullish_output['Gains after 1 days'] > 0]) /\
                        len(bullish_output['Gains after 1 days'])
        FiveDaysWinRate = len(bullish_output.loc[bullish_output['Gains after 5 days'] > 0]) /\
                          len(bullish_output['Gains after 5 days'])
        TenDaysWinRate = len(bullish_output.loc[bullish_output['Gains after 10 days'] > 0]) /\
                         len(bullish_output['Gains after 10 days'])
        ThirtyDaysWinRate = len(bullish_output.loc[bullish_output['Gains after 30 days'] > 0]) /\
                            len(bullish_output['Gains after 30 days'])
        final_output = final_output.append({'Pattern': 'Bullish ' + pattern,
                                            'Win Rate (1 Day)': OneDayWinRate,
                                            'Win Rate (5 Days)': FiveDaysWinRate,
                                            'Win Rate (10 Days)': TenDaysWinRate,
                                            'Win Rate (30 Days)': ThirtyDaysWinRate}, ignore_index=True)
    except Exception as e:
        print("No bullish pattern")

    try:
        bearish_output = output[output[pattern] < 0]
        OneDayWinRate = len(bearish_output.loc[bearish_output['Gains after 1 days'] > 0]) / \
                        len(bearish_output['Gains after 1 days'])
        FiveDaysWinRate = len(bearish_output.loc[bearish_output['Gains after 5 days'] > 0]) / \
                          len(bearish_output['Gains after 5 days'])
        TenDaysWinRate = len(bearish_output.loc[bearish_output['Gains after 10 days'] > 0]) / \
                         len(bearish_output['Gains after 10 days'])
        ThirtyDaysWinRate = len(bearish_output.loc[bearish_output['Gains after 30 days'] > 0]) / \
                            len(bearish_output['Gains after 30 days'])
        final_output = final_output.append({'Pattern': 'Bearish ' + pattern,
                                            'Win Rate (1 Day)': OneDayWinRate,
                                            'Win Rate (5 Days)': FiveDaysWinRate,
                                            'Win Rate (10 Days)': TenDaysWinRate,
                                            'Win Rate (30 Days)': ThirtyDaysWinRate}, ignore_index=True)
    except Exception as e:
        print("No bearish pattern")

    print('Done analysis on ' + pattern)

print(final_output)
final_output.to_csv('candlestick_analysis.csv',index=False)
