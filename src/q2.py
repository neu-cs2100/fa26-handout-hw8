"""HW8 Question 2

Using the same dataset as q1, write a function called retractions_by_reason that takes the 
DataFrame containing retraction data and returns a new DataFrame with two columns: 
retraction_reasons and retractions. The DataFrame should be sorted by `retractions` in descending 
order. Don't forget to reset the index when sorting the DataFrame.

Each entry in the `retraction_reasons` column contains a list of multiple reasons, separated by 
semicolons. For example, a common value in `retraction_reason` is:
    "Euphemisms for Plagiarism;Plagiarism of Text;"
For the purpose of this exercise, you should treat the entire list of retraction_reasons as one
single reason. You do not need to split the string up into reasons using the semicolons.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
