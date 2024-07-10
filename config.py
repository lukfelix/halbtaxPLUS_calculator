"""
This contains all the variables that can be adjusted for the script to calculate how much money you'll be giving SBB in the near future.
Follow the instructions attached to each parameter in order to minimize the hole SBB will leave in your wallet.
"""

halbtax_price = 190. # 190/170 depending on if you're returning

discount = 0.5 # set this to 1. if you only want to consider non-halbtax for some reason

halbtax_plus_options = [1000., 2000., 3000.] # change if new prices
halbtax_plus_prices = [800., 1500., 2100.]
# critical values are the costs where bonus of higher tier lets you benefit again
# e.g. at 2600.- you have used 500.- of bonus, which you also have in mid-tier
halbtax_plus_crit = [1700., 2600.]


"""
This is the important section: think about your weekly and annual use seperately,
which trips do you take every/most weeks and which are better quantified on a yearly basis?
"""

# replace this with prices (SFr) and routes you are taking:
routes = {
    'Buchsi-BE-ZH-Buchsi':(20.80 + (58.40 + 51.80)/2. + 41.15)*discount,     # Be-ZH with IC vs IR, assume 50/50
    'Buchsi-BE-Buchsi':2*20.80*discount, # factor 2 for roundtrip
    'Buchsi-ZH-Buchsi':2*41.15*discount,
    'Daytrip':2*25.*discount,
}


# replace this with corresponding expected frequencies (per week),
# use the format [min, max, average expected]
weekly_expected = {
    'Buchsi-BE-Buchsi':[0, 4, 2.5]
}
n_weeks = 52 # adjust if needed, used as number of weeks that weekly schedule is true


# same as above but for trips that you are not doing on a weekly basis
yearly_expected = {
    'Buchsi-BE-ZH-Buchsi':[0, 10, 5],
    'Buchsi-BE-Buchsi':[0, 10, 5],
    'Buchsi-ZH-Buchsi':[2*14, 38, 33],
    'Daytrip':[0, 10, 5],
}