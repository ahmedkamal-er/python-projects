# Bank Account Manager

## What it does
An object-oriented program that manages bank accounts — creating accounts, handling deposits and withdrawals, and tracking balances per account.

## How it works
1. Define a `BankAccount` class with attributes like owner name and balance.
2. Use methods (`deposit`, `withdraw`, `get_balance`) to change and check account state.
3. Create one or more account objects and interact with them through those methods.
4. Validate transactions so withdrawals can't exceed the balance.

## Why I built it
First real project using classes — `__init__`, `self`, and encapsulating account data and behavior inside one object instead of loose variables and functions.

## Skills used
Object-oriented programming (classes, `__init__`, `self`), encapsulation, methods, input validation.

## Example
```
account = BankAccount("Ahmed", 500)
account.deposit(200)
account.withdraw(100)
print(account.get_balance())  # 600
```

*(Replace with your script's actual class structure and method names.)*
