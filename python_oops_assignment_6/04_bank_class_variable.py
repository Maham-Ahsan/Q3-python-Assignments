class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def change_bank_name(cLs, name):
        cLs.bank_name = name

b1 = Bank()
print(b1.bank_name)
Bank.change_bank_name("Meezan Bank")
print(b1.bank_name)