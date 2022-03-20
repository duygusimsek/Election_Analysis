# Election_Analysis

## Overview

### History of the Project

In the previous project, the election audit analysis of a recent local congressional election had been completed.  To analyze the election data programmatically Python programming language (Python 3.10.2) and  Visual Studio development environment (Visual Studio Code, 1.65.2) had used and with the created code:

* The total number of votes cast was calculated.
* A complete list of the candidate for the election was created.
* The total number of votes that each candidate received was calculated.
* For each candidate, the percentage distribution of votes was calculated.
* Based on the highest vote the winner of the election was determined. 

### Purpose of this Analyze  

For this project, the analysis of election data had been extended by determining the voting information for each county:

* For each county, the voter turnout was calculated.
* Out of the total count of votes, each county’s votes of percentages were calculated. 
* The highest turnout county was determined. 

## Results

### Election-Audit Results

* Folders were navigated on the computer by using the command line to perform the task.
* The dependencies had been imported to use the Python modules that were needed.
* To be able to open and read the election data from the CSV file, paths were created.
* To count the total votes, the variable was created and the counter was set the zero.
* For making the list of the candidate name, the candidate_options list was written, and to hold the votes of each candidate candidate_votes dictionary was created. 
* To track the winning candidate’s name, vote, and percentage the variables were written. 
* With the “with open” statement and the paths that were created, the election data file had opened and read. 
* The “for loop” was nested under the “with open” statement for each row in the CSV file and an accumulator was written in order to increment by 1 as each row of the file was read.
* Because the candidate column is the third row in the dataset, the second index had been used to get the candidate from each list when the for loop iterate through the row.
* To be able to catch the unique names in the candidates_option list, the “if” statement with the “not in” operator was used to see if a candidate had been added to the list.
* Inside the “if” statement, a key from the unique candidates was created and set to zero to begin tracking the candidates’ votes. Then outside the statement, an accumulator was added 
* For saving the election results to the text file “with open” statement had used and “w” 







## Summary

The analysis of the election shows that:

- There were “x” votes cast in the election 
- The candidates were:
    * Candidate 1
    * Candidate 2
    * Candidate 3
- The candidate results were:
    * Candidate 1 received “x%” of the vote and “y” number of votes.
    * Candidate 2 received “x%” of the vote and “y” number of votes.
    * Candidate 3 received “x%” of the vote and “y” number of votes.
- The winner of the election was:
    * Candidate  (1,2, or 3), who received “x%” of the vote and “y” number of votes.

## Challenge Overview

## Challenge Summary

## Resources 

- Data Source: Election_results.csv
- Software: Python 3.10.2, Visual Studio Code, 1.65.2
