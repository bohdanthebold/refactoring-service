from math import ceil, floor


class MathService:
    def round(self, number, to_ceil):
        return ceil(number) if to_ceil else floor(number)

    def multiply(self, first_number, second_number):
        return first_number * second_number
