# ATM Simulator

## What it does
A command-line program that mimics core ATM functions: checking balance, depositing money, and withdrawing money, with validation so you can't withdraw more than the balance or enter negative amounts.

## How it works
1. Show a menu of actions (check balance / deposit / withdraw / exit).
2. Take the user's choice and the relevant amount as input.
3. Validate the input before applying it (block negative numbers, block overdrafts).
4. Update and display the balance after each transaction.
5. Loop back to the menu until the user exits.

## Why I built it
Practice with loops (running the menu until exit), input validation, and keeping state (the balance) consistent across multiple actions.

## Skills used
Variables, loops (`while`), functions, input validation, conditionals.

## Example
```
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose an option: 2
Enter amount: 200
New balance: 200.00
```

*(Replace with your script's actual menu and behavior.)*
