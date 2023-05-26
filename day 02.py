# Toooo ezzzzzz

def solve(meal_cost, tip_percent, tax_percent):
    cost = meal_cost + (meal_cost*tip_percent/100) + (meal_cost*tax_percent/100) 
    print(round(cost))