# joshua fernandez - 6/14/2024
# this program is a baseball stat calculator that predicts a pitcher's strikeout rate against a specific team

import statsapi

# mlb api
mlb = statsapi.MLB()


def get_player_id(fullname):
    player_ids = mlb.get_people_id(fullname=fullname)
    if player_ids:
        return player_ids[0]
    else:
        raise ValueError("Player not found.")


def get_player_stats(person_id, season):
    stats = ["season"]
    groups = ["pitching"]
    params = {"season": season}
    return mlb.get_player_stats(
        person_id=person_id, stats=stats, groups=groups, **params
    )


def get_team_id(abbreviation):
    teams = mlb.get_teams()
    for team in teams:
        if team.abbreviation == abbreviation:
            return team.id
    raise ValueError("Team not found.")


def get_oTeam_career_stats(team_id, season):
    stats = ["season"]
    groups = ["hitting"]
    params = {"season": season}
    return mlb.get_team_stats(team_id=team_id, stats=stats, groups=groups, **params)


# main func
if __name__ == "__main__":
    # gets player info
    player_name = input("Enter the player's name: ")
    player_id = get_player_id(player_name)
    player_career_stats = get_player_stats(player_id, "2025")

    # grab thier stats then convert it into a float
    TI = float(player_career_stats["pitching"]["season"].splits[0].stat.inningspitched)
    GS = float(player_career_stats["pitching"]["season"].splits[0].stat.gamesstarted)
    AS = float(
        player_career_stats["pitching"]["season"].splits[0].stat.strikeoutsper9inn
    )

    # average innings pitched per game started (IP)
    IP = TI / GS

    # player's average strikeouts per game (PG)
    PG = AS * (IP / 9)

    # benchmark
    B = float(input("Enter the benchmark for pitcher strikeouts: "))

    # abbrevation of opp team
    opposing_team_abbr = input("Enter the opposing team's abbreviation: ")
    team_id = get_team_id(opposing_team_abbr)
    team_career_stats = get_oTeam_career_stats(team_id, "2025")

    # grab their stats then convert to a float
    team_hits = float(team_career_stats["hitting"]["season"].splits[0].stat.strikeouts)
    team_atBats = float(
        team_career_stats["hitting"]["season"].splits[0].stat.plateappearances
    )

    # opposing team's average strikeout rate (SO)
    SO = team_hits / team_atBats

    # player's average strikeout per IP (E) and against opposing team (R
    E = PG * SO
    R = E * IP

    # output
    print(f"Player's average strikeouts per 9 innings: {AS:.2f}")
    print(f"Player's total innings pitched (TI): {TI:.2f}")
    print(f"Player's games started (GS): {GS:.2f}")
    print(f"Player's average innings pitched per game started (IP): {IP:.2f}")
    print(f"Player's average strikeouts per game (PG): {PG:.2f}")
    print(f"Opposing team's average strikeout rate (SO): {SO:.3f}")
    print(f"Player's average strikeout per IP against opposing team (R): {R:.2f}")

    # Compare benchmark
    if R > B:
        print(
            f"The player is expected to go over the benchmark with an average of {R:.2f} strikeouts per IP against {opposing_team_abbr}."
        )
    else:
        print(
            f"The player is expected to be under the benchmark with an average of {R:.2f} strikeouts per IP against {opposing_team_abbr}."
        )
