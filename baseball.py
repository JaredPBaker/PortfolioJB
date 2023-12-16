import random
class BaseballTeam:
   def __init__(self, name):
       self.name = name
       self.batting_average = round(random.uniform(0.200, 0.350), 3)
       self.pitching_strength = round(random.uniform(3.00, 5.00), 2)
       self.fielding_ability = random.randint(1, 10)
       self.runs = 0
def generate_teams(num_teams):
   teams = []
   for i in range(num_teams):
       team = BaseballTeam(f'Team {i+1}')
       teams.append(team)
   return teams
def challenge_teams(team1, team2, stat):
   stat_values = {
       'batting_average': team1.batting_average - team2.batting_average,
       'pitching_strength': team1.pitching_strength - team2.pitching_strength,
       'fielding_ability': team1.fielding_ability - team2.fielding_ability
   }
   if stat_values[stat] > 0:
       team1.runs += 1
       print(f"{team1.name} wins this round!")
   elif stat_values[stat] < 0:
       team2.runs += 1
       print(f"{team2.name} wins this round!")
   else:
       print("It's a tie for this round!")
def display_teams(teams):
   for team in teams:
       print(f"{team.name}: Runs - {team.runs}")
num_teams = 4  # Change this to have a different number of teams
teams = generate_teams(num_teams)
print("Initial Teams:")
display_teams(teams)
print("")
stats = ['batting_average', 'pitching_strength', 'fielding_ability']
for i in range(num_teams):
   for j in range(i + 1, num_teams):
       print(f"\n{teams[i].name} vs {teams[j].name}")
       random_stat = random.choice(stats)
       print(f"Stat for comparison: {random_stat}")
       challenge_teams(teams[i], teams[j], random_stat)
print("\nFinal Results:")
display_teams(teams)