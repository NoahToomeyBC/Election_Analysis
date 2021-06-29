# PyPoll Election Analysis

## Overview of Project

### Purpose

In this project, we were asked by a client to gather voting data from multiple counties to audit the results and metrics of a state-wide election. Using Python, we were able to complete this audit by automating the processes that are usually done by hand. By using Python, we were able to verify the data and present our findings in an easily readable list that showed the following: total votes, votes by county, votes per candidate, winning candidate, and county that had the largest turn out of voters. 

### What the data shows us.

* How many votes were cast?
  * In total, 369,711 votes were cast in the election.
* Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * Denver had the highest voter turn out, accounting for 82.8% of the total vote count.
    * 306,055 votes
  * Jefferson voters accounted for 10.5% of the total vote count.
    * 38,855 votes
  * Arapahoe only accounted for 6.7% of the total vote count.
    * 24,801 votes
* Breakdown of the number of votes and the percentage of the total votes each candidate received
  * The winner of this election was Diana Degette with 73.8% of the vote
    * 272,892 votes
  * The runner-up for this election was Charles Casper Stockham with 23% of the vote
    * 85,213 votes
  * In last was Raymon Antyhony Doane with only 3.1% of the vote
    * 11,606 votes

##### Election Results List
<p align="center">
![Election_Results](https://user-images.githubusercontent.com/85508764/123827986-b6630900-d8c6-11eb-87c8-4262f6a83873.png)
</p>

### Election-Audit Summary

Throughout this project, we worked with the intention of keeping this code modular so that it can be scaled up to large national elections or down to local elections. With this code, you can simply change the csv file that the code is pointing to in this line `file_to_load = os.path.join("Resources", "election_results.csv")` which will allow any properly formatted csv file to be plugged in and have the analysis run the same way. In addition small could be made to the formatting of the print outs to allow for the information to be applicable to larger or smaller elections. For example in a national election this block of code would only require the person working with the data set to change "County Votes:\n" to "State Votes:\n" or whatever is required for the audit :

<p align="center">
![Election_Code](https://user-images.githubusercontent.com/85508764/123827361-2b820e80-d8c6-11eb-9374-4b814439114d.png)
</p>

With the proper instruction and training this can be accomplished by almost anyone with very little hassle.