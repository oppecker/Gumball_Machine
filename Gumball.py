import collections

#Global vars to cut down on 'magic numbers'.
NICKLE = 5
DIME = 10
QUARTER = 25

class Gumball_Machine():
    def __init__(self):
        self.accepted_input_currency = {
            NICKLE:0,
            DIME:0,
            QUARTER:0,
        }
        self.rejected_input_currency = {}
        self.gumball_output = collections.namedtuple('Gumball_Output', 'gumball rejected_currency')
        self.change_output = collections.namedtuple('Change_Output', 'nickles dimes quarters rejected_currency')

    def input_currency(self, currency):
        '''If the input currency is a nickle, dime, or quarter store it in
        self.accepted_input_currency, otherwise store it in self.rejected_input_currency
        '''
        print(f'Currency Input: {currency}')
        if currency in self.accepted_input_currency:
            self.accepted_input_currency[currency] += 1
        else:
            if currency in self.rejected_input_currency:
                self.rejected_input_currency[currency] += 1
            else:
                self.rejected_input_currency[currency] = 1

    def flush_rejected_currency(self):
        '''Set all values in self.rejected_input_currency to 0.
        Returns what those values used to be.
        '''
        change_to_return = {k:v for k,v in self.rejected_input_currency.items() if v}
        for key, value in self.rejected_input_currency.items():
            self.rejected_input_currency[key] = 0
        return change_to_return

    def flush_currency(self):
        '''Set all values in self.accepted_input_currency to 0.
        Returns what those values used to be.
        '''
        nickles = self.accepted_input_currency[NICKLE]
        dimes = self.accepted_input_currency[DIME]
        quarters = self.accepted_input_currency[QUARTER]
        for key in self.accepted_input_currency:
            self.accepted_input_currency[key] = 0
        return nickles, dimes, quarters

    def red_lever(self):
        '''If enough currency has been input, update self.accepted_input_currency to
        account for payment, then return the gumball and any rejected currency.
        If not enough currency has been input, return no gumball but do return any rejected currency.
        '''
        print('Red Lever Pulled')
        if sum([k*v for k,v in self.accepted_input_currency.items()]) >= NICKLE:
            self._make_internal_change(currency=NICKLE)
            return self.gumball_output('Red Gumball', self.flush_rejected_currency())
        else:
            return self.gumball_output(None, self.flush_rejected_currency())

    def yellow_lever(self):
        '''If enough currency has been input, update self.accepted_input_currency to
        account for payment, then return the gumball and any rejected currency.
        If not enough currency has been input, return no gumball but do return any rejected currency.
        '''
        print('Yellow Lever Pulled')
        if sum([k*v for k,v in self.accepted_input_currency.items()]) >= DIME:
            self._make_internal_change(currency=DIME)
            return self.gumball_output('Yellow Gumball', self.flush_rejected_currency())
        else:
            return self.gumball_output(None, self.flush_rejected_currency())

    def _make_internal_change(self, currency):
        '''Modify self.accepted_input_currency to reflect the user
        being charged a Nickle or a Dime
        '''
        if currency == NICKLE:
            if self.accepted_input_currency[NICKLE]:
                #Remove a Nickle
                self.accepted_input_currency[NICKLE] -= 1
            elif self.accepted_input_currency[DIME]:
                #Remove a Dime and Add a Nickle
                self.accepted_input_currency[DIME] -= 1
                self.accepted_input_currency[NICKLE] += 1
            elif self.accepted_input_currency[QUARTER]:
                #Remove a Quarter and Add Two Dimes
                self.accepted_input_currency[QUARTER] -= 1
                self.accepted_input_currency[DIME] += 2
        elif currency == DIME:
            if self.accepted_input_currency[NICKLE] >= 2:
                #Remove two Nickles
                self.accepted_input_currency[NICKLE] -= 2
            elif self.accepted_input_currency[DIME]:
                #Remove a Dime
                self.accepted_input_currency[DIME] -= 1
            elif self.accepted_input_currency[QUARTER]:
                #Remove a Quarter and Add a Nickle and a Dime
                self.accepted_input_currency[QUARTER] -= 1
                self.accepted_input_currency[NICKLE] += 1
                self.accepted_input_currency[DIME] += 1

    def return_change_lever(self):
        '''Flush self.accepted_input_currency and self.rejected_input_currency
        and return what their values used to be.
        '''
        print('Return Change Lever Pulled')
        nickles, dimes, quarters = self.flush_currency()
        return self.change_output(nickles, dimes, quarters, self.flush_rejected_currency())
