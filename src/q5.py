"""HW8 Question 5

Some years have more publications than others, possibly due to changes in publication practices or
urgent need (e.g., early pandemic needs). Which years have unusually high or low retraction rates,
taking the total number of publications into account?

Please write a function called retraction_rate_per_year which takes two DataFrames: one for 
the total number of publications (in the format of publications_per_year.csv) and one for the 
retractions dataset we've been working with. It should take these two DataFrames and return a 
new DataFrame with two columns: year and retraction_rate.

It should calculate the retraction rate for each year by dividing the number of retractions by 
the total number of publications for that year. It should find the year for each retracted 
publication using the 'original_paper_date' column in the retractions DataFrame. The resulting
DataFrame should be sorted by year, in ascending order.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
