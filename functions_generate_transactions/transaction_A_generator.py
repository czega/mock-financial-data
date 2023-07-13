import random

def generate_transactions(transactions, num_transactions):
    for _ in range(num_transactions):
        amount = random.randint(-1000, 1000)
        if amount > 0:
            transaction = {
                "amount": amount,
                "date": random.randint(0, 30),
                "description": random.choice(["Direct deposit from employer", "received payment from X"]),
                "type": "deposit",
                "currency": "USD"
            }
        else:
            if amount == 0:
                amount -=1
            transaction = {
                    "amount": amount,
                    "date": random.randint(0,30),
                    "description": random.choice(["payment to X", "cash withdrawal"]),
                    "type": "withdrawal",
                    "currency": "USD"
                    }
        transactions.append(transaction)
    
    return transactions

# Given array
transactions = [
    {
        "amount": 1500,
        "date": 0,
        "description": "Direct deposit from employer",
        "type": "deposit",
        "currency": "USD"
    },
    {
        "amount": -1000,
        "date": 5,
        "description": "Monthly rent payment",
        "type": "withdrawal",
        "currency": "USD"
    },
    {
        "amount": -75,
        "date": 5,
        "description": "Online bill payment for utility services",
        "type": "withdrawal",
        "currency": "USD"
    },
    {
        "amount": -200,
        "date": 5,
        "description": "Check payment to John Doe",
        "type": "withdrawal",
        "currency": "USD"
    },
    {
        "amount": -50,
        "date": 10,
        "description": "ATM cash withdrawal",
        "type": "withdrawal",
        "currency": "USD"
    }
]

# Generate 295 additional transactions
new_transactions = generate_transactions(transactions, 295)

# Print the combined array
print(new_transactions)

