"""HW8 Question 1

global_academic_retractions_2000_2025.csv (in the data directory) contains the dataset from here: 
https://www.kaggle.com/datasets/abdurrahmanhakanacar/global-academic-retractions-20002025

Retraction is how the scientific community corrects its own record: when a published paper 
is found to contain serious errors, fabricated data, or ethical violations, it can be formally 
withdrawn. Being able to retract a paper is important because flawed research can influence later 
studies, medical decisions, and public policy if it stays in the record unchallenged. Retracted 
papers typically remain visible with a notice explaining why they were withdrawn, which is why a 
dataset like this one exists, and exploring it will let you see how often science catches its own 
mistakes and what kinds of problems it finds.

Write a function called days_to_retraction that takes a DataFrame containing retraction data (like
the one in global_academic_retractions_2000_2025.csv), and returns a new DataFrame with four 
columns: title, journal, primary_subject, and days_to_retraction. The DataFrame should be sorted
by days_to_retraction (ascending order), with ties broken by journal (alphabetical). Don't forget
to reset the index when sorting the DataFrame.

Don't forget to write tests in the tests directory. We recommend making a small Pandas DataFrame
and passing it to the function being tested, rather than relying on the full dataset. We also
recommend checking just the specified columns in the resulting DataFrame, rather than checking
whether the whole DataFrame is matching what's expected.
"""

import pandas as pd
