


eco_list = []

house_price = float(input('Enter a number [from 17200 to 344000] for median home price: '))
eco_list.append(house_price)
gold_price = float(input('Enter a number [from 34.9 to 1800] for gold price: '))
eco_list.append(gold_price)
dow = float(input('Enter a number [from 607 to 27000] for dow industrial index: '))
eco_list.append(dow)
gdp = float(input('Enter a number for GDP [from -4 to 9] '))
eco_list.append(gdp)
fed_rate = float(input('Enter a number [from 0.04 to 22] for Fed interest rate: '))
eco_list.append(fed_rate)
treasury_13wk = float(input('Enter a number [from 0 to 15.6] for 13 week treasury bill: '))
eco_list.append(treasury_13wk)
treasury_5yr = float(input('Enter a number [from 0.59 to 1.43] for 5 year treasury bill: '))
eco_list.append(treasury_5yr)
treasury_10yr = float(input('Enter a number [from 1.43 to 15.75] for 10 year treasury bill: '))
eco_list.append(treasury_10yr)
unemployment = float(input('Enter a number [from 3.4 to 10.8] for unemployment rate: '))
eco_list.append(unemployment)
earnings = float(input('Enter a number [from -805 to 1150] for change in household earnings: '))
eco_list.append(earnings)
cpi = float(input('Enter a number [from 30 to 257] for consumer price index: '))
eco_list.append(cpi)
inflation = float(input('Enter a number [from -2 to 2] for inflation: '))
eco_list.append(inflation)
housing_starts = float(input('Enter a number [from 475 to 2500] for new housing construction: '))
eco_list.append(housing_starts)


print(eco_list)
