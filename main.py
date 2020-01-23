exitCmd = 'exit'
dts = None
while dts != exitCmd:
    dts = input("Enter a datetime like YYYY-MM-DD HH:MM:SS\n")
    if dts != exitCmd:
        print(dts)
