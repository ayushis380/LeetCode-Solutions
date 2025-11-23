# Write your MySQL query statement below
Select customer_id, count(*) as count_no_trans
from visits as v
Left Join transactions t on v.visit_id = t.visit_id
where t.visit_id is Null
Group By customer_id
