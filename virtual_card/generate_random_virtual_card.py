import pandas,random
def generate_card_number():
    card_number=""
    ##I assume that the card number is composed by 16 number (if it is not  your case change number 16)
    for number in range(16):
        card_number+=str(random.randint(0,9))
    return card_number
def generate_expiry_date():
    months=["01","02","03","04","05","06","07","08","09","10","11","12"]
    expiry_month=random.choice(months)
    days=["31","28","31","30","31","30","31","31","30","31","30","31"]
    expiry_day=str(random.randint(1,int(days[months.index(expiry_month)])))
    if int(expiry_day)<10:
        expiry_day=f"0{expiry_day}"
    expiry_date=f"{expiry_day}/{expiry_month}"
    return expiry_date
def generate_cvv():
    CVV=""
    for number in range(3):
        CVV+=str(random.randint(0,9))
    return CVV
def add_cvv_to_csv_file():
    card_number=generate_card_number()
    expiry_date=generate_expiry_date()
    CVV=generate_cvv()
    row=[card_number,expiry_date,CVV]
    df = pandas.DataFrame([row])
    df.to_csv('virtual Cards.csv', mode='a',index=False, header=False)
def read_input():
    virtual_cards_number=input("how many virtual cards do you want to be created ? \n")
    return virtual_cards_number
def get_input():
    wrong_input=True
    while wrong_input:
        try:
            virtual_cards_number=int(read_input())
        except ValueError:
            print("please entre an integer")
        else:
            return virtual_cards_number
def start_programm():
            virtual_cards_number=get_input()
            for number in range(virtual_cards_number):
                add_cvv_to_csv_file()
start_programm()