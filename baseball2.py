import random
class BaseballTeam:
   def __init__(self, name):
       self.name = name
       self.runs = 0
def display_team_stats(team):
   print(f"{team.name} - Runs Scored: {team.runs}")
def bat(team, swing):
   if swing == 'contact':
       return random.uniform(0, 0.65)
   elif swing == 'power':
       return random.uniform(0.55, 1)
def pitch(team, pitch_type):
   if pitch_type == 'fastball':
       return random.uniform(0, 0.6)
   elif pitch_type == 'curveball':
       return random.uniform(0, 0.5)
   elif pitch_type == 'slider':
       return random.uniform(0, 0.55)
def user_bat(user_team, cpu_team):
   outs = 0
   while outs < 3:
       balls = 0
       strikes = 0
       runners_on_base = 0
       while True:
           print(f"\nYour team is batting - Balls: {balls}, Strikes: {strikes}, Outs: {outs}")
           user_swing = input("\nSelect your swing (contact or power): ").lower()
           if user_swing not in ['contact', 'power']:
               print("Please choose 'contact' or 'power'.")
               continue
           cpu_pitch = random.choice(['fastball', 'curveball', 'slider'])
           batter_score = bat(user_team, user_swing)
           pitcher_score = pitch(cpu_team, cpu_pitch)
           if batter_score > pitcher_score:
               if batter_score >= 0.8:  # Home Run
                   if runners_on_base > 0:
                       print(f"\n{user_team.name} scores {runners_on_base + 1} runs!")
                       user_team.runs += runners_on_base + 1
                   else:
                       user_team.runs += 1
                       print(f"\n{user_team.name} scores a run! It's a Home Run!")
                   runners_on_base = 0
               elif batter_score >= 0.6:  # Triple
                   print(f"\n{user_team.name} hits a Triple!")
                   runners_on_base += 1
               elif batter_score >= 0.4:  # Double
                   print(f"\n{user_team.name} hits a Double!")
                   runners_on_base += 1
               elif batter_score >= 0.2:  # Single
                   print(f"\n{user_team.name} hits a Single!")
                   runners_on_base += 1
           else:
               print(f"\n{cpu_team.name} strikes out the batter!")
               outs += 1
           if outs == 3:
               break
           if balls == 4:
               print(f"\nBatter walks to first base!")
               runners_on_base += 1
               break
           if strikes == 3:
               print(f"\nBatter strikes out!")
               outs += 1
               break
def user_pitch(user_team, cpu_team):
   outs = 0
   while outs < 3:
       balls = 0
       strikes = 0
       while True:
           print(f"\nYour team is pitching - Balls: {balls}, Strikes: {strikes}, Outs: {outs}")
           user_pitch_type = input("\nSelect your pitch (fastball, curveball, slider): ").lower()
           if user_pitch_type not in ['fastball', 'curveball', 'slider']:
               print("Please choose 'fastball', 'curveball', or 'slider'.")
               continue
           cpu_swing = random.choice(['contact', 'power'])
           pitcher_score = pitch(user_team, user_pitch_type)
           batter_score = bat(cpu_team, cpu_swing)
           if pitcher_score > batter_score:
               print(f"\n{user_team.name} strikes out the batter!")
               outs += 1
           else:
               if batter_score >= 0.8:  # Home Run
                   cpu_team.runs += 1
                   print(f"\n{cpu_team.name} scores a run! It's a Home Run!")
               elif batter_score >= 0.6:  # Triple
                   print(f"\n{cpu_team.name} hits a Triple!")
               elif batter_score >= 0.4:  # Double
                   print(f"\n{cpu_team.name} hits a Double!")
               elif batter_score >= 0.2:  # Single
                   print(f"\n{cpu_team.name} hits a Single!")
           if outs == 3:
               break
def play_game(user_team, cpu_team):
   innings = 9  # Number of innings in a baseball game
   for inning in range(1, innings + 1):
       if inning % 2 != 0:  # User team bats in odd innings
           user_bat(user_team, cpu_team)
       else:  # User team pitches in even innings
           user_pitch(user_team, cpu_team)
       print("\nCurrent Score:")
       display_team_stats(user_team)
       display_team_stats(cpu_team)
   print("\nGame Over - Final Score:")
   display_team_stats(user_team)
   display_team_stats(cpu_team)
user_team = BaseballTeam("User Team")
cpu_team = BaseballTeam("CPU Team")
print("\nUser Team Stats:")
display_team_stats(user_team)
print("\nCPU Team Stats:")
display_team_stats(cpu_team)
play_game(user_team, cpu_team)