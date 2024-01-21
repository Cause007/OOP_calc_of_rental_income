class ROI:
        
    def __init__(self):
        import math
        print('\nRETURN ON INVESTMENT CALCULATOR\n')
        print('Please fill in the following form:')
        print('\nPROPERTY AND MARKET CHARACTERISTICS\n')
        self.units = int(input('Total rental units: '))
        self.vacant_units_actual = int(input('\nCurrent number of vacant units: '))
        self.vacancy_actual = self.vacant_units_actual / self.units
        print("It is important to compare your property's current vacancy to that typical in the local market.")
        print(f'In a healthy, in-demand market, 5% is commonly expected from investors to compensate for unforeseen risk.')
        print('In a down market or at a less-desirable location, higher vacancy may be anticipated.')
        self.vacancy_proforma = int(input('Please enter your best estimate of anticipated, stabilized vacancy (as a whole number e.g. 5 = 5%, 10 = 10%): ')) / 100
        if self.vacancy_proforma < self.vacancy_actual:
            self.vacant_units_difference = self.vacant_units_actual - int(self.vacancy_proforma*self.units) 
            print(f'\nNOTE: Current occupancy is low by {self.vacant_units_difference} unit(s). How many months do you anticipate to lease-up to stabilized occupancy?')
            self.lease_up = int(input('(In a healthy market, anticipate 5 or more units per month; anticipate a slower rate if a down market or less desirable property): '))
        print('\nThank you. Lets move on to purchase and financing questions.\n')
        ROI.purchase_n_mortgage(self)

    def purchase_n_mortgage(self):
        self.purchase_price = int(input('Purchase price: '))
        self.down_pmt = int(input('Down Payment (if paid in cash, input full purchase amount): '))
        if self.down_pmt != self.purchase_price:
            print('\nMORTGAGE FINANCING\n')
            self.mortgage_pmt = int(input('Monthly mortgage payment: '))
        print('\nThank you. Lets discuss sources of income.')
        ROI.income(self)

    def income(self):
        print('\nINCOME')
        while True:
            self.rent_monthly = int(input('Total monthly rental income (RUBS or other reimbursables or fees are covered later): '))
            self.avg_rent_monthly = int((self.rent_monthly) / (self.units - self.vacant_units_actual))
            self.stabilized_rent_annual = int(self.avg_rent_monthly*self.units*12*(1-self.vacancy_proforma))
            self.temp = input(f'Based on your current vacancy, average rent per unit is approximately {self.avg_rent_monthly}.\nIs this accurate? ')
            if self.temp.lower() != 'no' or self.temp.lower() != 'n':
                break
        self.reimbursables = int(input('Total monthly reimbursables (e.g. utilities, RUBS): '))*12
        self.other_income = 0
        self.temp = input('Any other sources of income (laundry, parking, miscellaneous)?')
        while True:
            if self.temp.lower() == '' or self.temp.lower() == 'n' or 'no' in self.temp.lower():
                    break
            else:
                self.other_income += int(input('Monthly laundry income: ') or 0)
                self.other_income += int(input('Monthly parking income: ') or 0)
                self.other_income += int(input('Monthly pet fees income: ') or 0)
                self.other_income += int(input('Monthly other income: ') or 0)
                break
        self.egi = self.stabilized_rent_annual + self.reimbursables + self.other_income
        print('\nThat should cover income sources. Now lets move on to property expenses.')
        print(f'Your ANNUAL Income, at stabilized occupancy (Effective Gross Income, or EGI) is ${self.egi:,.0f}')
        ROI.expenses(self)

    def expenses(self):
        print('\nEXPENSES\n')
        self.taxes = int(input('ANNUAL Real Estate Taxes: '))
        self.insurance = int(input('ANNUAL liability insurance (include flood insurance if applicable): '))
        self.utilities = int(input('ANNUAL total utilities (electric, gas, water, sewer, trash): '))
        self.repairs = int(input('ANNUAL repairs & maintenance (exclude capital improvements): '))
        print(f'ANNUAL property managment fees (if not management by 3rd party, allocate a salary for owner-managed; typical 3-6% of income):')
        self.management = int(input(f'or between ${int(self.egi*0.03)} and ${int(self.egi*0.06)}: '))
        print('Finally, estimate annual reserves for capital improvements. Reserves account for non-reoccurring repairs or replacements to the property,')
        print('such as a roof replacement, exterior paint, etc. Reserves generally fall between $250 and $350 per unit, depending on age/condition.')
        self.reserves = int(input(f' Your property would warrant reserves between ${250*self.units} and ${350*self.units}, annually.): '))
        self.expenses_annual = self.taxes + self.insurance + self.utilities +self.repairs + self.management + self.reserves
        print(f'\nTotal Annual Expenses: ${self.expenses_annual:,.0f}')
        if self.mortgage_pmt:
            self.expenses_annual += self.mortgage_pmt
            print(f'adding your annual mortgage payment of ${self.mortgage_pmt} adjusts your expense total to ${self.expenses_annual}.')
        ROI.calc_NOI(self)

    def calc_NOI(self):
        self.NOI = self.egi - self.expenses_annual
        print('\nANNUAL NET OPERATING INCOME (NOI)\n')
        print('EGI - Expenses = NOI')
        print(f'${self.egi:,.0f} - ${self.expenses_annual:,.0f} = NOI of ${self.NOI:,.0f}')
        input('\nPress ENTER when ready to continue...')
        ROI.calc_ROI(self)

    def calc_ROI(self):
        print('\nRETURN ON INVESTMENT CONCLUSION\n')
        print('Based on your inputs, the estimated Return on Investment (ROI) for your property is as follows:')
        print(f'NOI ${self.NOI:,.0f} / cash invested ${self.down_pmt:,.0f} = ROI {round(self.NOI/self.down_pmt,3):.1%}')

ROI()
