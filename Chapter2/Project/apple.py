price_str = input("Veuillez entrer le prix des pommes： ")
price = float(price_str)
weight_str = input("Veuillez enter le poids des pommes: ")
weight = float(weight_str)
money = price * weight
print("Vous devez payer " + str(money) + " euros.")