# Stock Investment Portfolio Pipeline
As an opportunity to combine my passions of Data Science and Finance, this is a collection of scripts to take my stock investment data coupled with 
historical data for said investments as well as the S&P 500 as a benchmark, and present the findings in a public facing dashboard to hold myself 
accountable. If I'm seriously lagging behind the market, then this should remind myself to buy more index funds.

A visualization and breakdown for the ETL Pipeline DAG can be found in the file *Investments Dashboard Pipeline.pdf*. 

## Data Sources
There are two data sources that are required for extraction of the information needed.
* Google Sheet (Extracted through API)
  * History of trades and holdings
* Yahoo Finance (Extracted through API)
  * S&P 500 historical prices
  * Historical prices of current and previous portfolio holdings 
