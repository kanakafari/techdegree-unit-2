import constants
import copy

def clean_data():
    players_cleaned = copy.deepcopy(constants.PLAYERS)
    for dic in players_cleaned:
        height_cleaned, inches = (dic['height'].split(" ", 1))
        dic['height'] = int(height_cleaned)
        guardians_cleaned = dic['guardians'].split("and ",1)
        dic['guardians'] = guardians_cleaned
        if dic['experience'] == 'YES':
            dic['experience'] = True
        elif dic['experience'] == 'NO':
            dic['experience'] = False
    return players_cleaned

def team_assign(*args):
    team_var = []
    for arg in args:
        team_var.append(arg)
    return team_var

def balance_teams(*args):
    assigned_teams = copy.deepcopy(constants.TEAMS)
    exp_players = []
    unexp_players = []
    for dic in players_cleaned:
        if dic['experience'] == True:
            exp_players.append(dic)
        else:
            unexp_players.append(dic)
    exp_per_team = int(len(exp_players) / len(constants.TEAMS))
    unexp_per_team = int(len(unexp_players) / len(constants.TEAMS))
    team1 = team_assign(assigned_teams[0], exp_players[0:3], unexp_players[0:3])
    team2 = team_assign(assigned_teams[1], exp_players[3:6], unexp_players[3:6])
    team3 = team_assign(assigned_teams[2], exp_players[6:], unexp_players[6:])
    return team1, team2, team3

def final_formatting(team_names, team_names_formatted, team_height, team_guardians, team_guardians_formatted):
    for lists in team_names:
        for dic in lists:
            team_names_formatted.append(dic['name'])
            team_height.append(dic['height'])
            team_guardians.append(dic['guardians'])
    for list in team_guardians:
        for parent in list:
            team_guardians_formatted.append(parent)

def team_stat_display(team_number, team_name_formatted, team_height_avg, team_guardians_formatted):
    print("\nTeam: {} Stats".format(team_number[0]))
    print("-" * 20)
    print("Total Players: {}".format(len(team_name_formatted)))
    print("Total experienced: {}".format(len(team_number[1])))
    print("Total inexperienced: {}".format(len(team_number[2])))
    print("Average Height: {}".format(team_height_avg))
    print("\nPlayers on Team:")
    print(", ".join(team_name_formatted))
    print("\nGuardians:")
    print(", ".join(team_guardians_formatted))
    input("\nPress Enter to Continue\n")

def run_tool():    
    while True:
        print("BASKETBALL TEAM STATS TOOL\n")
        print("---- MENU ----\n")
        print("Here are your choices:")
        team1_names, team2_names, team3_names = team1[1:3], team2[1:3], team3[1:3]
        team1_names_formatted, team2_names_formatted, team3_names_formatted = [], [], []
        team1_height, team2_height, team3_height = [], [], []
        team1_height_avg, team2_height_avg, team3_height_avg = [], [], []
        team1_guardians, team2_guardians, team3_guardians = [], [], []
        team1_guardians_formatted, team2_guardians_formatted, team3_guardians_formatted = [], [], []
        final_formatting(team1_names, team1_names_formatted, team1_height, team1_guardians, team1_guardians_formatted)
        final_formatting(team2_names, team2_names_formatted, team2_height, team2_guardians, team2_guardians_formatted)
        final_formatting(team3_names, team3_names_formatted, team3_height, team3_guardians, team3_guardians_formatted)
        team1_height_avg = sum(team1_height) / len(team1_names_formatted)
        team2_height_avg = sum(team2_height) / len(team2_names_formatted)
        team3_height_avg = sum(team3_height) / len(team3_names_formatted)
        try:
            choice = int(input("1) Display Team Stats\n2) Quit\n\nEnter an Option > "))
            if choice not in range(1,3):
                raise ValueError
        except ValueError:
            print("Oh no! Please select a valid number.")
            continue
        if choice == 1:
            try:
                team_choice = int(input("1) Panthers\n2) Bandits\n3) Warrirors\n\nEnter an option> "))
                if team_choice not in range(1, 4):
                    raise ValueError
            except ValueError:
                    print("Oh no! Please Select a valid number.")
                    continue
            if team_choice == 1:
                team_stat_display(team1, team1_names_formatted, team1_height_avg, team1_guardians_formatted)
            elif team_choice == 2:
                team_stat_display(team2, team2_names_formatted, team2_height_avg, team2_guardians_formatted)
            elif team_choice == 3:
                team_stat_display(team3, team3_names_formatted, team3_height_avg, team3_guardians_formatted)
        elif choice == 2:
            print("\nThank You. Come Again")
            break
            
            
if __name__ == '__main__':
    
    players_cleaned = clean_data()

    team1, team2, team3 = balance_teams()
    
    run_tool()
