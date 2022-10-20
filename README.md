# surfs_up Climate Analysis

## Overview
The purpose of the 'surfs-up' analysis is to provide data to prospective investors in a startup company.  The company is to be an ice cream/surf shop based in Hawaii.  Investors are interested in the historical weather patterns to determine if this climate reliant business will be profitable as presented.
### Resources
A SQLite file containing years of Hawaiian weather station data was used by writing SQL queries to retrieve date specific information about temperature.
Pandas data frames were also used to calculate and display summary statistics as required.

## Results
The information gathered targeted the months of June and December and looked at historic temperatures for those months.
### Key takeaways include:
  * Although stable year round temperatures are a Hawaiian hallmark, low temperatures drop by 8 degrees from June to December
  * This has less effect on the mean however which is only a 3.9 degree drop in the same time frame.
  * This is due to a slightly higher standard deviation in December, perhaps indicating some more outlying data dragging numbers farther from the mean

## Summary
In conclusion, accceptable year round temperature is observed in the target location to facilitate warm weather activity.  
One could additionally run queries for precipitation for June and December by running the following:

For June:
```
prec = [Measurement.prcp, Measurement.date]
june_prec = session.query(*prec).filter(func.strftime("%m", Measurement.date) == "06").all()
```
For December:
```
prec = [Measurement.prcp, Measurement.date]
dec_prec = session.query(*prec).filter(func.strftime("%m", Measurement.date) == "12").all()
```
Here, once again the weather is favorable for the proposed business, as avearages of 0.13" and 0.22" of average daily rainfall for June and December are observed respectively.  Although the occasional downpour (max of 6.4" for June and 4.4" for Dec) can happen, the low standard deviations suggest that those numbers are the esception and not the rule. 
