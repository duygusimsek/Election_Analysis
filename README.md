# Election_Analysis

## Overview

### History of the Project

In the previous project, the election audit analysis of a recent local congressional election had been completed.  To analyze the election data programmatically Python programming language (Python 3.10.2) and  Visual Studio development environment (Visual Studio Code, 1.65.2) had used and with the created code:

* The total number of votes cast was calculated.
* A complete list of the candidate for the election was created.
* The total number of votes that each candidate received was calculated.
* For each candidate, the percentage distribution of votes was calculated.
* Based on the highest vote the winner of the election was determined. 

### Purpose of this Analysis  

For this project, the analysis of election data had been extended by determining the voting information for each county:

* For each county, the voter turnout was calculated.
* Out of the total count of votes, each county’s votes of percentages were calculated. 
* The highest turnout county was determined. 

## Coding

### Election-Audit Code Explanation

* Folders were navigated on the computer by using the command line to perform the task.
* The dependencies had been imported to use the Python modules that were needed.
* To be able to open and read the election data from the CSV file, paths were created.
* To count the total votes, the variable was created and the counter was set the zero.
* For making the list of the candidate name, the "candidate_options" list was written, and to hold the votes of each candidate "candidate_votes" dictionary was created. 
* To track the winning candidate’s name, vote, and percentage the variables were written. 
* With the “with open” statement and the paths that were created, the election data file had opened and read. 
* The “for loop” was nested under the “with open” statement for each row in the CSV file and an accumulator was written in order to increment by 1 as each row of the file was read.
* Because the candidate column is the third row in the dataset, the second index had been used to get the candidate from each list when the for loop iterate through the row.
* To be able to catch the unique names in the candidates_option list, the “if” statement with the “not in” operator was used to see if a candidate had been added to the list.
* Inside the “if” statement, a key from the unique candidates was created and set to zero to begin tracking the candidates’ votes. Then outside the statement, an accumulator was added 
* For saving the election results to the text file “with open” statement had been used and “w” mode was added to write data to the file. 
* Votes percentages for candidates were calculated and printed to the terminal. 
* For the winning candidate summary, the winner candidate, the winner’s vote, and the percentage were analyzed and printed on the terminal. 
* The winning candidate’s summary was saved to the text file. 

### Election-Audit-County Code Explaination
* To analyze the election results by the counties, new lines were added to the previous code.
* For making list for counties, the “county_names” list; to hold the counties’ vote information “county_votes” dictionary was created. 
* To track the largest county turnout variables were written. 
* In order to extract the county names from each row from the dataset, the first index had been used and place inside the “for loop”.

* Inside the “if” statement, a key from the unique county was created and set to zero to begin tracking the county names. Then outside the statement, an accumulator was added.

* County vote counts and percentages of votes were calculated and printed to the terminal. 

* For the largest county turnout summary, the county’s name was printed on the terminal. 

* The largest county turnout was written to the text file. 

## Election-Audit Results (Candidates and Counties)

The analysis of the election shows that:

- There were 369,771 votes cast in the election between 3 counties.

- The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane

- The candidate results were:
    * Charles Casper Stockham received 23.0% of the vote and 85,213 votes.

    * Diana DeGette received 73.8% of the vote and  272,892 votes.

    * Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

- The winner of the election was:
    * Diana DeGette received 73.8% of the vote and  272,892 votes.

- The counties and county results were:
    * Denver county had  82.8% of the total vote and 306,055 ballots submitted. 
           
    * Jefferson county had 10.5% of the total vote with 38,855 ballots submitted. 
   
    * Arapahoe county had 6.7% of the total vote with 24,801 ballots submitted. (add the election result screen shot)

- The largest county turnover is Denver county with 306,055 ballots submitted. 

## Election Audit Summary

The code that was written for this election analysis, can be modified and used for any election analysis in the future. With additional code lines, vote counts and vote percentages for each candidate, in each district can be determined. 

Voter registration methods can change the participation of voters and that affects the vote turnouts. With additional datasets and lines to code, analyzing how the voters use their vote, can be added to voter turnout results and help to get us a deeper understanding of the election results. 

## Resources 

- Data Source: Election_results.csv
- Software: Python 3.10.2, Visual Studio Code, 1.65.2
