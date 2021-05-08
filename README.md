# NYSE Stocks & Covid-19
![1140x500_pandemic_stocks](https://user-images.githubusercontent.com/78886087/117244187-36587f80-adfe-11eb-8f46-ffd4cc64798c.jpg)
Source | © shutterstock.com

### Overview

-------------------------------------------------------------------------------------------------------------------------------------
- **Objective**
     * To Analyze the effect of COVID-19 on the stock market. Specifically, we look at the S&P 500 indexes by economic sectors and companies.
     *  Which sectors have had a better/worse performance during the pandemic?
     *  Which companies in each sector have had a better/worse performance during the pandemic?
- **Data**
     * [Stocks prices](https://www.alphavantage.co/#about): Alpha Vantage Inc. stock APIs 
     * [Index S&P 500](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf)
     * [Symbols by sector and industry](https://www.ssga.com/library-content/products/fund-docs/etfs/us/information-schedules/spdr-etf-listing.pdf)
     * [Symbols by company](https://stockmarketmba.com/stocksinthesp500.php)
     * [4 pandemic relevant events](https://www.ajmc.com/view/a-timeline-of-covid19-developments-in-2020)
       * 30/01/2020: The W.H.O. declared a global health emergency
       * 11/03/2020: WHO Declares COVID-19 a Pandemic
       * 21/07/2020: Phase I/II vaccines' promise results
       * 08/12/2020: First coronavirus vaccine approved for use in the U.K.


- **Methodology**
     * Simple Graphic Analysis using Matplotlib 
- **Libraries used**
     * Numpy, json, requests, pandas, matplotlib, scipy, os, datetime, time

### Repository structure
___________

``` bash
│   .gitignore                                    # ignore sensitive files
│   config.py                                     # paste api key inside this file
|   covid19_by_country.csv                        # csv with covid-19 data, not uploaded, file too big for GitHUB
│   energy_analysis.ipynb                         # energy sector analysis
│   project_outline.md                            # first project draft (deprecated)
│   README.md                                     # readme file 
│   sector_breakdown.ipynb                        # piechart by economic sector
│   Stocks & COVID-19.pdf                         # presentation pdf
│   stock_+.ipynb                                 # analysis by economic sector
│   summary.pdf                                   # project summary and results
│   tickers.py                                    # tickers list to pull from
│   XLE Ticker Price During Covid-19.png          # XLE index graph
│   XLk Ticker Price During Covid-19.png          # XLK index graph
|
├───energy_analysis                               # energy sector analysis folder
│   │
│   ├───app_screenshots                           # app screenshots folder
│   │       percentage_price_change.png
│   │       percentage_price_stats.png
│   │
│   └───plot_images                               # saved plots from the notebook
│           bar_chart.png
│           line_chart.png
│
├───resources                                     # csv general resources
│       stocks by company.csv
│       stocks by industry.csv
│       stocks by sector.csv
│
├───tech_analysis                                 # tech sector analysis folder
│   │   tech_analysis.ipynb                       # tech sector notebook
│   │
│   └───plot_images                               # saved plots from the notebook
│           bar_chart.png
│           line_chart.png

````
### Application Breakdown
-------------------------------------------------------------------------------------------------------------------------------------
- API calls to AlphaVantage
   * The resultant json contains 10+ years of data
   * While loop to retrieve year of study (2020)
 
- We use Pandas to:
   *  Retrieve and save the data from json format
   *  Drop rows with no values (no stocks operations) and keep available data
   *  Describe our data
   *  Estimate stocks performance (changes in prices at the begging and end of the year)
   
- We use Matplotlib to analyze sector and companies stock prices performance during 2020. 
  *  Bar and line charts
  
- Results

