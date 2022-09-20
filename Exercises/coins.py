import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        for key,value in kwargs.items():
            setattr(self, key, value)

        self.value = self.original_value * (1.25 if self.is_rare else 1)
        self.colour = self.clean_colour if self.is_clean else self.rusty_colour

    def __del__(self):
        print('Coin spent!')

    def __str__(self):
        if self.original_value>=1.0:
            return '£{} coin'.format(int(self.original_value))
        else:
            return '{}p coin'.format(int(self.original_value*100))
        
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        self.heads = random.choice([True, False])

        
class OnePence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.01,
            'clean_colour': 'bronze',
            'rusty_colour': 'brownish',
            'num_edges': 1,
            'diameter': 20.3, #mm
            'thickness':1.52, #mm
            'mass': 3.56, #gr
        }
        super().__init__(rare, clean, heads, **data)


class TwoPence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.02,
            'clean_colour': 'bronze',
            'rusty_colour': 'brownish',
            'num_edges': 1,
            'diameter': 25.9, #mm
            'thickness':1.85, #mm
            'mass': 7.12, #gr
        }
        super().__init__(rare, clean, heads, **data)


class FivePence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.05,
            'clean_colour': 'silver',
            'rusty_colour': None,
            'num_edges': 1,
            'diameter': 18.0, #mm
            'thickness':1.77, #mm
            'mass': 3.25, #gr
        }
        super().__init__(rare, clean, heads, **data)

    def rust(self):
        self.colour = self.clean_colour


class TenPence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.10,
            'clean_colour': 'silver',
            'rusty_colour': None,
            'num_edges': 1,
            'diameter': 24.5, #mm
            'thickness': 1.85, #mm
            'mass': 6.5, #gr
        }
        super().__init__(rare, clean, heads, **data)

    def rust(self):
        self.colour = self.clean_colour
        
        
class TwentyPence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.20,
            'clean_colour': 'silver',
            'rusty_colour': None,
            'num_edges': 7,
            'diameter': 21.4, #mm
            'thickness': 1.7, #mm
            'mass': 5.0, #gr
        }
        super().__init__(rare, clean, heads, **data)

    def rust(self):
        self.colour = self.clean_colour


class FiftyPence(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 0.50,
            'clean_colour': 'silver',
            'rusty_colour': None,
            'num_edges': 7,
            'diameter': 27.3, #mm
            'thickness': 1.78, #mm
            'mass': 8.0, #gr
        }
        super().__init__(rare, clean, heads, **data)

    def rust(self):
        self.colour = self.clean_colour

        
class OnePound(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 1.00,
            'clean_colour': 'gold',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'diameter': 22.5, #mm
            'thickness': 3.15, #mm
            'mass': 9.5, #gr
        }
        super().__init__(rare, clean, heads, **data)


class TwoPound(Coin):
    def __init__(self, rare=False, clean=True, heads=True):
        data = {
            'original_value': 2.00,
            'clean_colour': 'gold & silver',
            'rusty_colour': 'greenish',
            'num_edges': 1,
            'diameter': 28.4, #mm
            'thickness': 2.5, #mm
            'mass': 12.0, #gr
        }
        super().__init__(rare, clean, heads, **data)


coins = [OnePence(), TwoPence(), FivePence(), TenPence(),
         TwentyPence(), FiftyPence(), OnePound(), TwoPound()]
for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]
    string = '{} - Colour: {}, value: {}, diamater(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}'
    print(string.format(*arguments))
    
