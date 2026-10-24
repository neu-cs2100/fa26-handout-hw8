"""HW8 Question 5

Some journals publish more papers than others, so the raw number of retractions may not be useful.
Let's calculate the retraction rate for each journal, as a fraction of the total number of 
publications from that journal.

The data directory contains another file called journal_titles_with_counts.csv, which contains
the total number of publications overall in each journal between the years 2000 and 2025. It 
was collected using the OpenAlex API (https://help.openalex.org/).

So, using the same dataset as q1-q4, plus this dataset of the total number of publications, 
write a function called retraction_rate_by_journal that takes the two DataFrames (the retraction 
DataFrame and the total publications DataFrame), and returns a new DataFrame with four columns:
journal, retractions, total_publications, and retraction_rate. The retraction_rate is the
fraction of retractions relative to the total number of publications for that journal. Return 
the new DataFrame sorted by retraction_rate in descending order, with ties broken by journal name.
Don't forget to reset the index when sorting the DataFrame.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
