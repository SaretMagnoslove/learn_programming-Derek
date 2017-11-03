import threading
import time


class BankAccount(threading.Thread):
    accountBalance = 100

    def __init__(self, name, MoneyRequested):
        threading.Thread.__init__(self)

        self.name = name
        self.MoneyRequested = MoneyRequested

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(costumer):
        print('{} tries to withdraw ${} at {}'.format(costumer.name, costumer.MoneyRequested,
                                                      time.strftime('%H:%M:%S', time.gmtime())))
        if BankAccount.accountBalance - costumer.MoneyRequested > 0:
            BankAccount.accountBalance -= costumer.MoneyRequested
            print('New account balance is: ${}'.format(
                BankAccount.accountBalance))
        else:
            print('Not enough money')
            print('Acount balance is: ', BankAccount.accountBalance)
        time.sleep(3)


threadLock = threading.Lock()

doug = BankAccount('Doug',1)
paul = BankAccount('Paul',100)
sally = BankAccount('Sally',50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print('Execution ends')


