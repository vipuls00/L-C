adjacent_countries = {
    "IN": ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"],
    "US": ["Canada", "Mexico"],
    "NZ": ["Australia"],
    "GB": ["Ireland"],
    "CA": ["United States"],
    "AU": ["New Zealand"],
    "FR": ["Belgium", "Luxembourg", "Germany", "Switzerland", "Italy", "Monaco", "Andorra", "Spain"],
    "DE": ["Denmark", "Poland", "Czech Republic", "Austria", "Switzerland", "France", "Belgium", "Netherlands", "Luxembourg"],
    "BR": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "CN": ["Russia", "Mongolia", "India", "Nepal", "Pakistan", "Afghanistan", "Tajikistan", "Kyrgyzstan", "Kazakhstan"],
    "RU": ["Norway", "Finland", "Estonia", "Latvia", "Lithuania", "Poland", "Belarus", "Ukraine", "Georgia", "Azerbaijan", "Kazakhstan", "China", "Mongolia", "North Korea"]
}

def get_neighboring_countries(country_code):
    country_code = country_code.upper()
    if country_code in adjacent_countries:
        return adjacent_countries[country_code]
    else:
        return "Invalid country code or no neighboring country data available."

def main():
    country_code = input("Enter a country code (e.g., IN, US, NZ): ").upper()
    
    if len(country_code) == 2:
        neighboring_countries = get_neighboring_countries(country_code)
        print(f"Country Code: {country_code}")
        if isinstance(neighboring_countries, list):
            print(f"Neighboring countries: {', '.join(neighboring_countries)}")
        else:
            print(neighboring_countries)
    else:
        print("Please enter a valid 2-letter country code.")

if __name__ == "__main__":
    main()
