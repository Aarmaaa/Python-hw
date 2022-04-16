class Atm(object):
    def __init__(self , user_name ,contact ,card_number , card_pin, money ):
        self.user_name = user_name
        self.contact = contact
        self.card_number = card_number
        self.pin = card_pin
        self.money = money

    def balance(self):
        input("please enter your card number: ") 
        print("Your blance is $100")

    def withDrawl(self):
        drawl = int(input("the amount you want to withdrawl: "))
        # print(self.money - drawl)
        print("now your blance is : $" + str((self.money - drawl)))

    def addMoney(self):
        add = int(input("the amount of money you want to add: "))
        print("now your blance is : $" + str((self.money + add)))


person1 = Atm("aarmaan", 924358302 , 159349, 2000, 500 )
person1.balance()
person1.withDrawl()
person1.addMoney()
