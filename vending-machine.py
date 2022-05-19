import time

class VendingMachine:

    def bankNotes(self):
        return [1, 5, 10, 20, 50, 100]

    def drinks(self):
        return [
            {
                'name': 'Coca-cola',
                'price': 2.00,
            },
            {
                'name': 'Pepsi',
                'price': 2.00,
            },
            {
                'name': 'Spritzer',
                'price': 1.00,
            }
        ]

    def changes(self, paid, amount):
        balance = paid-amount
        for notes in reversed(self.bankNotes()):
            count = balance//notes
            if count > 0:
                numeral = 'piece' if count == 1 else 'pieces'
                print('Changes: '+str(round(count))+' '+numeral+' of RM'+str(notes))
            else:
                continue

            time.sleep(2)
            balance = balance%notes
        
        return True

    def success(self):
        print('Enjoy!')   

    def run(self):
        items = self.drinks()
        print('\n')
        print('\n')
        print('\n')
        print('Welcome, please select your drinks')

        # display items
        i = 0
        for drinks in self.drinks():
            i+=1
            print(str(i)+'. '+drinks['name']+': RM'+str('{:.2f}'.format(drinks['price'])))

        item = int(input('Your choice:'))
        amount = items[item-1]['price']

        print('Total amount: RM'+str('{:.2f}'.format(amount)))
        print('We only accept RM1, RM5, RM10, RM20, RM50, RM100')

        while True:
            balance = amount
            print('Balance: RM '+str('{:.2f}'.format(balance)))
            paid = int(input('Please insert your banknotes (key in digits):'))
            
            if paid not in self.bankNotes():
                print('Incorrect bank notes')
            elif paid < amount:
                amount = amount-paid
            elif paid > amount:
                result = self.changes(paid, amount)
                if result == True:
                    self.success()
                    break
            elif paid == amount:
                self.success()
                break


vending = VendingMachine()

while True:
    vending.run()
