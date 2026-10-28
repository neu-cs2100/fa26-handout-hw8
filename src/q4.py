"""HW8 Question 4

Using the same dataset as q1-q3, write a function called scale_authors_and_days that takes the 
DataFrame containing retraction data and returns a new DataFrame with two new columns: a scaled
version of the author_count (scaled to the range between 0 and 1) and a scaled version of the 
days_to_retraction (scaled to the range between 0 and 1). The new columns should be named 
author_count_scaled and days_to_retraction_scaled, respectively. The new DataFrame should be
sorted by author_count_scaled in descending order, with ties broken by days_to_retraction_scaled,
in descending order. Don't forget to reset the index when sorting the DataFrame.

You can refer to 
https://neu-pdi.github.io/cs2100-public-resources/lecture-notes/l19-design-data1
/#scaling-and-normalizing-data
for information on scaling data. You do not need to consider the case where all values are equal
(so the min and max are the same, making the denominator zero).

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
