country_names = ['bangladesh','england','america','canada','austrelia']
print(country_names)
print()
add_country = input("Enter a country name: ")
country_names.append(add_country)
print(add_country,'has index number',country_names.index(add_country))