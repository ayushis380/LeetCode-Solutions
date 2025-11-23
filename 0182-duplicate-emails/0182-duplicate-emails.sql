# Write your MySQL query statement below
Select email from 
(Select email, Count(email) as num
from Person
Group by email 
) as query
where num > 1