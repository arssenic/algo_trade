
def run_backtest(df, symbol):
    capital = 100000
    position = 0
    log = []
    for i in range(1, len(df)):
        if bool(df['Buy'].iloc[i]) and position == 0:
            entry = df['Close'].iloc[i]
            position = capital / entry
            log.append({'Date': df.index[i], 'Action': 'BUY', 'Price': entry})
        
        # Lowering the RSI from 70 to 65 to make selling more likely.
        elif position > 0 and float(df['RSI'].iloc[i]) > 65:
            exit = df['Close'].iloc[i]
            capital = position * exit
            position = 0
            log.append({'Date': df.index[i], 'Action': 'SELL', 'Price': exit})
            
    pnl = capital - 100000
    return {"log": log, "final_pnl": pnl}