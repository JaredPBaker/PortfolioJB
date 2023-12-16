import random
class BaseballTeam:
   def __init__(self, name):
       self.name = name
       self.batting_average = round(random.uniform(0.200, 0.350), 3)
       self.pitching_strength = round(random.uniform(3.00, 5.00), 2)
       self.fielding_ability = random.randint(1, 10)
       self.runs = 0
def display_team_stats(team):
   print(f"{team.name} - Batting Average: {team.batting_average}, Pitching Strength: {team.pitching_strength}, Fielding Ability: {team.fielding_ability}")
def bat(team, swing):
   if swing == 'contact':
       return random.uniform(0, team.batting_average)
   elif swing == 'power':
       return random.uniform(team.batting_average, 1)
def pitch(team, pitch_type):
   if pitch_type == 'fastball':
       return random.uniform(0, team.pitching_strength)
   elif pitch_type == 'curveball':
       return random.uniform(0, team.pitching_strength * 0.8)
   elif pitch_type == 'slider':
       return random.uniform(0, team.pitching_strength * 0.9)
def play_half_inning(user_team, cpu_team, inning_half):
   print(f"\n{user_team.name} (Batters) vs {cpu_team.name} (Pitchers) - {inning_half} inning")
   runs_scored = 0
   for _ in range(3):  # Minimum of 3 batters per half inning
       print("\nSelect your swing (contact or power):")
       user_swing = input().lower()
       cpu_pitch = random.choice(['fastball', 'curveball', 'slider'])
       print(f"The CPU throws a {cpu_pitch}!")
       batter_score = bat(user_team, user_swing)
       pitcher_score = pitch(cpu_team, cpu_pitch)
       if batter_score > pitcher_score:
           runs_scored += 1
           print(f"\n{user_team.name} scores a run!")
       else:
           print(f"\n{cpu_team.name} makes the out!")
   return runs_scored
def play_game(user_team, cpu_team):
   innings = 9  # Number of innings in a baseball game
   for inning in range(1, innings + 1):
       if inning % 2 != 0:  # User team bats in odd innings
           runs = play_half_inning(user_team, cpu_team, "Top of")
           cpu_team.runs += runs
       else:  # User team pitches in even innings
           runs = play_half_inning(cpu_team, user_team, "Bottom of")
           user_team.runs += runs
   print("\nGame Over - Final Score:")
   print(f"{user_team.name}: {user_team.runs} runs")
   print(f"{cpu_team.name}: {cpu_team.runs} runs")
user_team = BaseballTeam("User Team")
cpu_team = BaseballTeam("CPU Team")
# Randomly decide who starts as the home or away team
if random.choice([True, False]):
   print("You're the Home Team!")
   user_is_home = True
else:
   print("You're the Away Team!")
   user_is_home = False
print("\nUser Team Stats:")
display_team_stats(user_team)
print("\nCPU Team Stats:")
display_team_stats(cpu_team)
play_game(user_team, cpu_team)