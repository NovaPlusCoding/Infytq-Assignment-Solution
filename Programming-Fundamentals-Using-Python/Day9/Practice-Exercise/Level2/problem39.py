# PF-Prac-39
def max_populated_state(cities_dict, state):
    l, l1 = [], []
    for i in cities_dict:
        if i['State'] == state:
            l.append(i)
    for i in l:
        l1.append(i['Population'])
    m = max(l1)
    if l1.count(m) == 1:
        for i in l:
            if m == i['Population']:
                return i
    else:
        max_list = [x['Name'] for x in l if m == x['Population']]
        return sorted(max_list)

cities_dict = [
    {'Name': 'Vancouver', 'State': 'WA', 'Population': 161791},
    {'Name': 'Salem', 'State': 'OR', 'Population': 154637},
    {'Name': 'Seattle', 'State': 'WA', 'Population': 80885},
    {'Name': 'Bellingham', 'State': 'WA', 'Population': 608660},
    {'Name': 'Spokane', 'State': 'WA', 'Population': 208916},
    {'Name': 'Bellevue', 'State': 'WA', 'Population': 608660},
    {'Name': 'Portland', 'State': 'OR', 'Population': 583776}
]
state = "WA"
print("The city details are:", cities_dict)
print("State:", state)
output = max_populated_state(cities_dict, state)
print("The highest populated city in the given state is:", output)
