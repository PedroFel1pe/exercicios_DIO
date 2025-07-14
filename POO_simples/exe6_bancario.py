#Crie uma classe ContaBancaria que tem:Atributos: titular, saldo.Métodos: depositar, sacar (não permitir sacar valor maior que o saldo), mostrar saldo
class Bank_account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    def _bank_balance(self, new_balance):
        self.balance = new_balance
    def check_balance(self):
        return f"Current balance: R${self.balance:.2f}"
    def deposit(self, amount_deposited):
        if amount_deposited > 0:
            self.balance += amount_deposited
            return f"Deposited R${amount_deposited:.2f}.\nNew balance: R${self.balance:.2f}"
        else:
            return f"Invalid amount. Please enter a value greater than 0"
    def withdraw(self, amount_withdraw):
        if amount_withdraw > self.balance:
            return f"Insufficient balance"
        else:
            self.balance -= amount_withdraw
            return f"Withdraw R${amount_withdraw:.2f}. \nNew balance: R${self.balance:.2f}"
    
balance = 0.0
holder = input("Cardholder name: ")
bank_account = Bank_account(holder, balance)
while True:
    print("\n" + "-//-" * 10)
    print(f"Hello,{holder}! What would you like to do?")
    print("Select 1 to DEPOSIT")
    print("Select 2 to WITHDRAW")
    print("Select 3 to CHECK BALANCE")
    print("Select 4 to CLOSE")
    print("-//-" * 10)
    number = int(input("Type your option here: "))

    if number == 1:
        amount = float(input("Enter amount to deposit: R$"))
        print(bank_account.deposit(amount))
    elif number == 2:
        amount = float(input("Enter amount to withdraw: R$"))
        print(bank_account.withdraw(amount))
    elif number == 3:
        print(bank_account.check_balance())
    elif number == 4:
        print("Session closed. Thank you!")
        break
    else:
        print("Option not available yet.")