counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

for keys,value in counties_dict.items():
    print(keys, "county has",value,"registered voters")

voting_data=[{'county': 'Arapahoe', 'registered_voters': 424829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)
         