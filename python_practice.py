counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353},
                {"county":"Jefferson", "registered voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])

for county_dict in voting_data:
  for value in county_dict.values():
    print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
  print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
  f"You recieved {candidate_votes} number of votes."
  f"The total number of votes in the election was {total_votes}. "
  f"You recieved {candidate_votes / total_votes * 100}% of the total votes!")
print(message_to_candidate)  