"""HW8 Question 3

Using the same dataset as q1 and q2, write a function called misconduct_with_many_authors that takes 
the DataFrame containing retraction data and returns a new DataFrame with records where 
is_misconduct is true and author_count is at least n (where n is another argument to the 
function, default 5). Return the dataset with the selected records, sorted by author_count. Don't
forget to reset the index when sorting the DataFrame.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
