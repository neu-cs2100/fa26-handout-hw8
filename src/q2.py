"""HW8 Question 2

Using the same dataset as q1, write a function called retractions_by_journal that takes the 
DataFrame containing retraction data and returns a new DataFrame with two columns: journal 
and retractions. The DataFrame should be sorted by retractions in descending order. Don't
forget to reset the index when sorting the DataFrame.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
