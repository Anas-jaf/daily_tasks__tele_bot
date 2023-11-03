import aladhan

city = 'Amman'
country = 'Jo'

location = aladhan.City(city, country) # Doha, Qatar
client = aladhan.Client(location)

adhans = client.get_today_times()

print(f"Today's Prayer Times for {country} , {city}")
print("======================================")
# for adhan in adhans:
#     print("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))
    
print( [{adhan.get_ar_name() : adhan.readable_timing(show_date=False)} for adhan in adhans])
