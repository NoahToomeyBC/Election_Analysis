counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county, voters in counties_dict.items():
    print(county, "county has",  voters, "registered voters")
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353},
                {"county":"Jefferson", "registered voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])
