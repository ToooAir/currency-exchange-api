from decimal import Decimal, ROUND_HALF_UP

def round_v3(num, decimal):
    str_deci = 1
    for _ in range(decimal):
        str_deci = str_deci / 10
    str_deci = str(str_deci)
    result = Decimal(str(num)).quantize(Decimal(str_deci), rounding=ROUND_HALF_UP)
    result = float(result)
    print(result)
    return result

class CurrencyExchangeService:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, source, target, amount):
        if source not in self.rates or target not in self.rates[source]:
            raise ValueError("Unsupported currency")
        try:
            amount = float(amount.replace(',', ''))
        except ValueError:
            raise ValueError("Invalid amount")
        amount = round_v3(amount,2)
        converted_amount = amount * self.rates[source][target]
        return f"{round_v3(converted_amount,2):,.2f}"
