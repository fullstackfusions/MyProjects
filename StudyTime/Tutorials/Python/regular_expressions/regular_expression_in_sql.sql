--regular expression in queries
SELECT id, comments
FROM customers
WHERE comments ~* '\b[A-Za-z0-9._%+-]+@example\.com\b';