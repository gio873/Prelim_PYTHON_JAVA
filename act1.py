usd_to_eur_rate = 0.92

prices_usd = []
prices_eur = []

print("Please enter the prices for 6 products:")

for i in range(1, 7):
    price_usd = float(input(f"Enter price for Product {i} in USD$: "))
    
    price_eur = round(price_usd * usd_to_eur_rate, 2)
    
    prices_usd.append(price_usd)
    prices_eur.append(price_eur)

print("\n--- Summary ---")
print("Prices in USD:", prices_usd)
print("Prices in EUR:", prices_eur)