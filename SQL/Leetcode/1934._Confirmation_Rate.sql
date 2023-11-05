WITH Dataset AS (
SELECT S.user_id, C.action
FROM
Signups S
LEFT JOIN Confirmations C
ON S.user_id = C.user_id
),
A AS (
    SELECT user_id, COUNT(*) AS a_cnt
  FROM Dataset
  GROUP BY user_id
),
B AS
(
  SELECT user_id, COUNT(*) AS b_cnt
  FROM Dataset
  WHERE action = 'confirmed'
  GROUP BY user_id
)

SELECT A.user_id, IFNULL(ROUND((b_cnt/a_cnt),2), 0) AS confirmation_rate
FROM A
LEFT JOIN B
ON A.user_id = B.user_id
;


-- 개선

WITH AggregatedConfirmations AS (
    SELECT 
        S.user_id,
        SUM(CASE WHEN C.action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_count,
        COUNT(C.action) AS total_count
    FROM Signups S
    LEFT JOIN Confirmations C ON S.user_id = C.user_id
    GROUP BY S.user_id
)

SELECT 
    user_id, 
    IFNULL(ROUND(confirmed_count / total_count, 2), 0) AS confirmation_rate
FROM AggregatedConfirmations
ORDER BY user_id;