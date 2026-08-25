# Write your MySQL query statement below
-- select visit.customer_id, count(visits.visit_ id) As count_no_trans
-- from visit
-- left join transaction
-- on visit.visit_id = transaction.visit_id
-- where transaction.tansaction_id is null 
-- group by visit.customer_id;

SELECT Visits.customer_id, COUNT(Visits.visit_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id;