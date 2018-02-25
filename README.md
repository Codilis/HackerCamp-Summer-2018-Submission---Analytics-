# HackerCamp-Summer-2018-Submission---Analytics-
It contains the source code for the Data Analytics problem of HackerCamp organised by innovaccer.


To run the code the code given you will required following modules:
1. pandas
    Installation : pip install pandas
2. fuzzywuzzy 
    Installation : https://pypi.python.org/pypi/fuzzywuzzy#downloads

Pandas is used to handle dataset, to convert csv file to DataFrame
Fuzzywuzzy is use to find similar names in the dataset provided.
It uses Levenshtein Distance algorithm to find similar strings
Code consist of a fit() function that takes data and ratio as an arguments.
    Data argument takes input in DataFrame or dictionary format
    Ratio should be an int. It defines how much strict algorithm must be while comparing strings. High value of ratio tells higher             strictness while searching for similar string
    fit() function initially checks for same ‘dob’ and same ‘gen’,  if it founds one, it will then check if they are similar first name       and last name as there are already in clust dictionary by checking their ratio of similarity if it is greater then provided, then         that data is skipped, else it is added to clust dictionary.
    This function then returns that clust dictionary.
Code also consist of predict() function that takes data as an argument.
    This function checks the similarity between every element of data provided to that is already in clust dictionary using fuzzywuzzy’s        ratio() function.
    Then it takes the mean of that result and returns the list of values with maximum mean.
