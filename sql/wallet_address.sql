wallet table
| wallet_id | wallet_address |
| --------- | -------------- |
| 1         | 0xA123         |
| 2         | 0xB456         |
| 3         | 0xC789         |
| 4         | 0xD012         |

transaction table
| txn_id | wallet_id | amount | txn_date   |
| ------ | --------- | ------ | ---------- |
| 101    | 1         | 250.00 | 2026-01-01 |
| 102    | 2         | 100.00 | 2026-01-05 |
| 103    | 1         | 75.00  | 2026-01-10 |
| 104    | 3         | 300.00 | 2026-01-12 |


-- write a query to list all wallet addresses that have one or more transactions recorded.
-- The output should display the wallet addresses in alphabetical order, including only those wallets whose IDs appear in the transactions table

SELECT DISTINCT w.wallet_address
FROM wallets w
INNER JOIN transactions t
    ON w.wallet_id = t.wallet_id
ORDER BY w.wallet_address ASC;