# Write your MySQL query statement below
Select date_id, make_name,
Count(Distinct lead_id) as unique_leads,
Count(Distinct partner_id) as unique_partners
from DailySales
Group by date_id, make_name