import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Reading in current data from coinmarketcap.com ---> 100 rows
current = pd.read_json("https://api.coinmarketcap.com/v1/ticker/")

# Selecting the 'id' and the 'market_cap_usd' columns
market_cap_raw = current[['id', 'market_cap_usd']]

# Counting the number of values
cou = market_cap_raw.count()

# Filtering out rows without a market capitalization
cap = market_cap_raw.query('market_cap_usd > 0')
# Selecting the first 10 rows and setting the index
cap10 = cap.set_index('id').head(10)

# Calculating market_cap_perc
total = int(cap10.sum())
cap10 = cap10.assign(market_cap_perc = lambda x: x.market_cap_usd / total * 100)


# Selecting the id, percent_change_24h and percent_change_7d columns
volatility = current[['id', 'percent_change_24h', 'percent_change_7d']]

# Setting the index to 'id' and dropping all NaN rows
volatility = volatility.set_index('id').dropna()

# Sorting the DataFrame by percent_change_24h in ascending order
volatility = volatility.sort_values(by=['percent_change_24h'])





# Sorting in ascending order
volatility7d = volatility.sort_values(by=['percent_change_7d'])



###Large Cap####

# Selecting everything bigger than 10 billion 
largecaps = cap.query('market_cap_usd > 1e+10')



###Categoriey###

def capcount(query_string):
    return cap.query(query_string).count().id


# Using capcount count the biggish cryptos
biggish = capcount('market_cap_usd >= 1e+10')

# Same as above for micro ...
micro = capcount('market_cap_usd >= 5e+7 & market_cap_usd <=3e+8')

# ... and for nano
nano =  capcount('market_cap_usd < 5e+7')

# Making a list with the 3 counts
values = [biggish, micro, nano]


