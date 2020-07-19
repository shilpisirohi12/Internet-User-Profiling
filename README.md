# Internet-User-Profiling

## Analysis
### P-Value Analysis
When we compute P-Values and measure how user’s usage is statistically similar to each other. We can see that for small time windows, the usage pattern is similar but as we increase the size of the window, count of the usage data which is statistically similar for different users is more. Below is the graphical representation where trend line is confirming the analysis which is derived by counting yes and no in the table for different time windows that was shown is previous section ( 02 ).
 

When we see the count of users who are statistically indistinguishable from other users for different time window. We can see that it is less for smaller windows but as the size of the time window increases, the number of users who has statistically similar internet usage profile increases. Below graph shows the count of users which are similar to rest of 53 users based on p-Values. 
 
### Spearman Rank Correlation Coefficient for the same user for different time frame(r1a2a): 
Below is the analysis of  r1a2a for different time window. 

**For 10 second window:** It shows that most of the user’s week 1 and week 2 data has positive correlation. The Coefficient lies between -0.03028 and 0.385.
 There are 34 users who have positive correlation, 10 users have no correlation and 10 users have negative correlation for the internet usage of week 1 and week 2. 
We can say that 63% of the users has similar profile for week 1 and week 2.
Below is the graphical representation.

 




**For 227 second window:** It shows that most of the user’s week 1 and week 2 data has positive correlation. The Coefficient lies between -0.098 and 0.586.
 There are 38 users who have positive correlation, 10 users have no correlation and 6 users have negative correlation for the internet usage of week 1 and week 2. 
We can say that 70% of the users has similar profile for week 1 and week 2.
Below is the graphical representation.
 


**For 300 second window:** It shows that most of the user’s week 1 and week 2 data has no correlation. The Coefficient lies between -0.084 and 0.034.
 There are 7 users have positive correlation, 33 users have no correlation and 14 users have negative correlation for the internet usage of week 1 and week 2. 
We can say that merely 12% of the users has similar profile for week 1 and week 2.
Below is the graphical representation.
 
This shows that we cannot conclude something based on Spearman’s Correlation Coefficient. We need to do more statistical computation to get some meaningful conclusion from this. That’s why we have to compute z-Value and p-Value. Also, the earlier sections of the report show that p-Value is helpful in finding the trend.

### Conclusion
This project shows that it is possible to create different user profiles based on different roles like student, DBA, Network admin. Comparing the earlier created profiles with the new profiles can help in detecting anomalies. Profiling can be useful in various field like advertisement, resource management. Based on the profile, advertising company can target the users with specific profile. Same goes for resource management. Currently, everything is on cloud. Based on the user profiles, cloud providing companies can allocate different resources for different profiles. This could be a useful study.
