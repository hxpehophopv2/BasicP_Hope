d = int(input("Distance (km): "))

if d >= 500:
    print("Your shipment cost is ฿45.")
elif d >= 301:
    print("Your shipment cost is ฿35.")
elif d >= 100:
    print("Your shipment cost is ฿25.")
elif d >= 51:
    print("Your shipment cost is ฿15.")
elif d >= 5:
    print("Your shipment cost is ฿10.")
else:
    print("We do not accept shipment at this distance.")
