"""
13.50 PRACTICE: Functions***: Electric bill

Southern California's electric company uses a "three tier" cost structure for household electric bills. 
As of Jan 2017, for a given month, the first 232 kWh is $0.08291/kWh, the next 696 kWh is $0.16838/kWh, and any additional kWh is $0.23336/kWh. 
Write a function that takes a household month's kWh, and the cutoffs and prices for the tiers, and returns that month's electric cost.

If the input is:
1700.0
232
0.08291
696
0.16838
0.23336

the output is:
$316.58

The output is rounded to the nearest cent.

Hints:
- Think carefully through the logic of calculating the various cost contributions of each tier. We recommend calculating tier 3 first, then tier 2.
- Declare a variable named remaining_KWh. Initialize remaining_KWh with month_KWh. Also declare month_cost, initialized with 0.0. 
    Declare tier_KWh to use for computations.
- Start with an if statement if remaining_KWh > (tier2_cutoff + tier1_cutoff). 
    If yes, compute just the kWh that are part of tier 3, which is remaining_KWh - (tier2_cutoff + tier1_cutoff), and store in tier_KWh. 
    Multiply tier_KWh by tier3_cost, and add that to the month_cost. Then decrease remaining_KWh by tier_KWh.
- Repeat for tier2.

For whatever is left in remaining_KWh, multiply by tier1_cost.
"""

def calculate_month_electric_cost(month_KWh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost):
    if month_KWh == 0:
        return 0.0
    
    if month_KWh <= tier1_cutoff:
        return month_KWh * tier1_cost
    
    elif month_KWh <= (tier1_cutoff + tier2_cutoff):
        tier1_Kwh = tier1_cutoff * tier1_cost
        tier2_Kwh = (month_KWh - tier1_cutoff) * tier2_cost
        return tier1_Kwh + tier2_Kwh
    else:
        tier1_Kwh = tier1_cutoff * tier1_cost
        tier2_Kwh = tier2_cutoff * tier2_cost
        tire3_Kwh = (month_KWh - tier1_cutoff - tier2_cutoff) * tier3_cost
        return tier1_Kwh + tier2_Kwh + tire3_Kwh


month_KWh = float(input())
tier1_cutoff = float(input())
tier1_cost = float(input())
tier2_cutoff = float(input())
tier2_cost = float(input())
tier3_Cost = float(input())
   
month_cost = calculate_month_electric_cost(month_KWh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_Cost)
print("$", round(month_cost, 2), sep = "")