# Financial-Analytics

Obtaining Efficient Frontier:
I extracted data for Walmart and Facebook from 1/1/2014 upto today.
Normalized this data to 100 and calculated the logarithmic returns.
Calculated the Expected Portfolio Return, Variance and Volatility 
Created a loop of 1000 iterations.

Predicting Gross Profit using Monte-Carlo Simulations:
Assumed forecasted revenues of 200 million, expected deviation of 10 million, COGS = 40% of the revenues.
Based on predicted reveues and COGS value the gross profit of the company is estimated
Plotted as a histogram

•	Calculating the Efficient Frontier : 
o	For a group of portfolios composed of two assets; Proctor and Gamble stock and the S&P 500 index.
o	Obtained data from yahoo for the duration of 2014 to 2020, performed 1000 different combinations of the same assets.
o	Obtained a graph that visualizes portfolio return to volatilities.
•	Monte- Carlo Computer Simulations: To project companies future revenue and expenses.
o	Used the values of expected revenue and expected cost of goods sold (COGS) to predict the firm’s future gross profit.
o	Plotted results on a histogram.
•	Asset pricing with Monte- Carlo: To analyze the upside and downsides of an investment.
o	Using scipy.stats module along with pandas and numpy libraries forecasted Microsoft’s stock price for the upcoming 1000 days.
o	Demonstrated the result of 10 possible Microsoft stock prices on a graph.
