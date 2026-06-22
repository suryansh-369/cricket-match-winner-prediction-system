import pandas as pd

df = pd.read_csv('data/processed/matches_clean.csv')

def create_features(input_data):

    team1 = input_data["team1"]
    team2 = input_data["team2"]
    venue = input_data["venue"]

    previous_matches = df

    def get_team_stats(team ,venue, previous_matches):
    
        team_matches = previous_matches[(previous_matches["team1"] == team) | (previous_matches["team2"] == team)]
    
        matches_played = len(team_matches)

        wins = (team_matches["winner"] == team).sum()

        if matches_played == 0:
            win_rate = 0
        else:
            win_rate = wins / matches_played

        last5 = team_matches.tail(5)

        team_form = (last5["winner"] == team).sum()

        team_venue_matches = previous_matches[
        (
            (previous_matches["team1"] == team) |
            (previous_matches["team2"] == team)
        )
        &
        (previous_matches["venue"] == venue)
        ]
        venue_matches_played = len(team_venue_matches)

        wins = (team_venue_matches["winner"] == team).sum()

        if venue_matches_played == 0:
            venue_win_rate = 0
        else:
            venue_win_rate = wins / venue_matches_played

        if matches_played == 0:
            return{
            "matches_played": matches_played,
            "wins": wins,
            "win_rate": win_rate,
            "form_5": team_form,
            "venue_matches": 0,
            "venue_win_rate": 0
        }

        return {
        "matches_played": matches_played,
        "wins": wins,
        "win_rate": win_rate,
        "form_5": team_form,
        "venue_matches": venue_matches_played,
        "venue_win_rate" : venue_win_rate
        }


    def h2h_match_stats(team1, team2, previous_matches):

        h2h_match = previous_matches[
        ((previous_matches["team1"] == team1) & (previous_matches["team2"] == team2)) |
        ((previous_matches["team1"] == team2) & (previous_matches["team2"] == team1))
        ]

        h2h_t1_wins = (h2h_match["winner"] == team1).sum()
        h2h_t2_wins = (h2h_match["winner"] == team2).sum()
        return {
            "team1_h2h_wins": h2h_t1_wins,
            "team2_h2h_wins": h2h_t2_wins,
        }


    def toss_features(input_data):

        if input_data["toss_winner"] == input_data["team1"]:
            team1_won_toss = 1
        else:
            team1_won_toss = 0

        if input_data["toss_winner"] == input_data["team2"]:
            team2_won_toss = 1
        else:
            team2_won_toss = 0

        return{
            "team1_won_toss": team1_won_toss,
            "team2_won_toss": team2_won_toss
        }

    team1_stats = get_team_stats(team1, venue, previous_matches)
    team2_stats = get_team_stats(team2, venue, previous_matches)
    h2h_stats = h2h_match_stats(team1, team2, previous_matches)
    toss_stats = toss_features(input_data)

    features = {

    "team1": team1,
    "team2": team2,
    "venue": venue,

    "toss_winner": input_data["toss_winner"],
    "toss_decision": input_data["toss_decision"],

    "team1_matches_played":
        team1_stats["matches_played"],

    "team1_win_rate":
        team1_stats["win_rate"],

    "team1_form_5":
        team1_stats["form_5"],

    "team2_matches_played":
        team2_stats["matches_played"],

    "team2_win_rate":
        team2_stats["win_rate"],

    "team2_form_5":
        team2_stats["form_5"],

    "team1_venue_matches":
        team1_stats["venue_matches"],

    "team1_venue_win_rate":
        team1_stats["venue_win_rate"],

    "team2_venue_matches":
        team2_stats["venue_matches"],

    "team2_venue_win_rate":
        team2_stats["venue_win_rate"],

    **h2h_stats,
    **toss_stats
    }

    features_df = pd.DataFrame([features])

    return features_df

  

sample = {
    "team1":"India",
    "team2":"Australia",
    "venue":"Dubai",
    "toss_winner":"India",
    "toss_decision":"bat"
}

result = create_features(sample)

print(result.shape)
print(result)





