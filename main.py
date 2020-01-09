from crypto.cryptocur import cap10, volatility, volatility7d, values #DataFrames
from crypto.plot import top10_subplot #Function
import pandas as pd
import matplotlib.pyplot as plt

#10 cryptocurrencies with highest capitalisation
print(cap10)

#24 hour and 7d volatility of cryptocurrencies
print(volatility.head(6))


TOP_CAP_TITLE = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'

fig1, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
ax = cap10.plot.bar(y='market_cap_perc', ax=axes[0])

ax.set_title(TOP_CAP_TITLE)
ax.set_ylabel(TOP_CAP_YLABEL)
ax.set_xlabel('')

# Colors for the bar plot
COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']
# Plotting market_cap_usd as before but adding the colors and scaling the y-axis  
ax = cap10.plot.bar(y='market_cap_usd', color=COLORS, logy=True, ax=axes[1])


ax.set_title(TOP_CAP_TITLE)
ax.set_ylabel("USD")
ax.set_xlabel('')

plt.tight_layout()


### Top losers and winners ####
DTITLE = "24 hours top losers and winners"

# Calling the function above with the 24 hours period series
fig2, ax = top10_subplot(volatility['percent_change_24h'], DTITLE)
plt.tight_layout()

WTITLE = "Weekly top losers and winners"

# Calling the function above with the 7 day period series
fig3, ax = top10_subplot(volatility7d['percent_change_7d'], WTITLE)
plt.tight_layout()


####Categories of capitalisation####
# Labels for the plot
LABELS = ["biggish", "micro", "nano"]
fig4, ax = plt.subplots()
ax.bar(range(len(values)), values, tick_label=LABELS)

plt.show()