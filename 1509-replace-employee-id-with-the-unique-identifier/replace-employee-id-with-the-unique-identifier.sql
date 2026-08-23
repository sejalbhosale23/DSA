# Write your MySQL query statement below
select EmployeeUNI.unique_id,Employees.name from Employees
left join EmployeeUNI
on Employees.id = EmployeeUNI.id;

-- SELECT EmployeeUNI.unique_id,Employees.name
-- FROM Employees
-- LEFT JOIN EmployeeUNI
-- ON Employees.id = EmployeeUNI.id;