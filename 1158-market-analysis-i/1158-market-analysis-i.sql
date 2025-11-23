# Write your MySQL query statement below
Select u.user_id as buyer_id, join_date, count(o.order_id) as orders_in_2019
from Users u
Left Join Orders o on u.user_id = o.buyer_id and Year(o.order_date) = '2019'
Group by 
    u.user_id
Order by 
    u.user_id