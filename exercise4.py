USSD = input('Enter *544#')
print("0:Nyakua Bonus"
          "1:Data Deals"
          "2:Weekly Bundles"
          "3:Weekly Bundles"
          "4:GO MONTHLY"
          "5:No expiry"
          "7:Okoa Data"
          "8:Lipa Mdogo"
          "9:Data Plus NEW"
          "10:Hot Minutes"
          "98:More")



code = int(input("Enter any number from 0 to 10 or enter number 98"))
if code == 0:
    print("Nyakua Bonus")
elif code == 1:
    print('Data Deals')
elif code == 2:
    print("Daily Bundles")
elif code == 3:
    print('Weekly Bundles')
elif code == 4:
    print('GO MONTHLY')
elif code == 5:
    print('No Expiry')
elif code == 6:
    print("Video Bundles")
elif code == 7:
    print("Okoa Data")
elif code == 8:
    print("Lipa Mdogo")
elif code == 9:
    print('Data Plus New')
elif code == 10:
    print('Hot minutes')
elif code == 98:
    print("More")
else:
    print("character entered is invalid")