Personal finance management with MongoDB and metabase for visualization.

## Dabatase(psql)

Account:
- Account Type: string (alipay account, cash, Citibank, ...)
- Account ID: string (unique identifier like jc-cash, jc-alipay-1...)
- Money Type: string (dollar, RMB...)
- Money Array: array of [date, int] (e.g., [2024/7/1, 100], [2024/7/4, 200]...)
- Description: string (other details about the account)
- Exp (optional): Date (expiring date)

Transactions:
- Date: date
- Description: string
- Amount: int
- Account ID: string (which account this transaction belongs to)
- Category: string (Subscription, Utility, Rent, etc. Default: Other)
- Tags (optional): array of strings
- Is Transfer: boolean (to indicate if this is a transfer between accounts)
- Transfer To/From Account ID (optional): string (the ID of the other account involved in a transfer)
