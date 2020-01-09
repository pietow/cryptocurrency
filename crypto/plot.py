import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec




#Defining a function with 2 parameters, the series to plot and the title
def top10_subplot(volatility_series, title):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    
    # Plotting with pandas the barchart for the top 10 losers
    ax = (volatility_series[:10].plot.bar( color='darkred', ax=axes[0]))
    
    fig.suptitle(title)
    ax.set_ylabel('% change')
    ax.set_xlabel('')
    
    # Same as above, but for the top 10 winners
    ax = (volatility_series[-10:].plot.bar(color='darkblue', ax=axes[1]))
    ax.set_xlabel('')
    return fig, ax
