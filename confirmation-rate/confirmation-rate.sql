# Write your MySQL query statement below



-- SELECT *
-- FROM
-- Signups s1
-- LEFT JOIN (
--     SELECT c2.user_id, (*) as total
--     FROM Confirmations c2
--     GROUP BY c2.user_id
--     LEFT JOIN
    
-- )

# FIRST I WILL MAKE A TABLE USER_ID, TOTAL_ATTEMPS, SUCCESFULL

SELECT s1.user_id, ROUND(COALESCE(f.success, 0) / COALESCE(f.total, 1), 2) as confirmation_rate
FROM Signups s1
LEFT JOIN
(


SELECT c1.user_id, COUNT(*) as total, COALESCE(c3.success, 0) as success
FROM Confirmations c1
LEFT JOIN
(
    SELECT c2.user_id, COUNT(*) as success
    FROM Confirmations c2
    WHERE c2.action = 'confirmed'
    GROUP BY c2.user_id
) as c3
ON c1.user_id = c3.user_id
GROUP BY c1.user_id
) AS f
ON f.user_id = s1.user_id
