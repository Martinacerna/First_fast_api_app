"""amount - amount which we want to convert - float
input_currency - input currency - 3 letters name or currency symbol
output_currency - requested/output currency - 3 letters name or currency symbol"""

"if output_currency param is missing, convert to all known currencies"
"""
get input currency
get input amount
conversion 
"""

input_currency = "EUR"
output_currency = "CZK"
amount = 1
eur_czk_rate = 25


"""
Use kiwi rates https://rates-finance.skypicker.com/ endpoint to get the JSON
Deserialize the data from JSON response to your data structure. You could create the pydantic models for this purpose
Serialize the data to your Json format
add classes - for rates? for currencies
pust to staging area and repository
"""


def get_conversion_rate(input_currency: str, output_currency: str) -> float:
    eur_czk_rate = 25
    return eur_czk_rate


def convert_currency(amount: float, input_currency: str, output_currency: str) -> float:
    rate = get_conversion_rate(input_currency, output_currency)
    convert = rate * amount
    return convert
