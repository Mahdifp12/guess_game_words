STAR = 10 * "*"

print(f"""
{STAR}

if your profit percentage is 2

for example, enter 0.2

{STAR}
# """)
user_profit = float(input("Enter profit percentage: "))

user_money = int(input("Enter your amonut money: "))

user_year = int(input("Enter your year for profit percentage: "))

def calc_bank_profit_percentage(year_num, profit_percentage, money_num):
    """This is function for "calculate profit percentage" and inputs are as follows :    
    
    
    year_num = Number of years for profit
         profit_percentage = percentage number for profit
            money_num = amount of money
    
    """

    result_money = money_num

    for _ in range(year_num):
        result_money = result_money * (1 + profit_percentage)

    return result_money

money_with_profit = calc_bank_profit_percentage(year_num= user_year, money_num= user_money, profit_percentage= user_profit)

print(f"your money with profit: {money_with_profit}")