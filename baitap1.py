# Dữ liệu thống kê
player_stats_list = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    """
    Tính chỉ số KDA.
    Có thể phát sinh ZeroDivisionError nếu deaths = 0.
    """
    return (kills + assists) / deaths


def process_player_statistics(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player_stats in player_stats_list:
        player_name = player_stats[0]
        kills = player_stats[1]
        deaths = player_stats[2]
        assists = player_stats[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)

            print(
                f"Tuyển thủ {player_name} có chỉ số KDA là: {kda:.2f}"
            )

        except ZeroDivisionError:
            print(
                f"{player_name}: KDA Hoàn hảo (Perfect Game)!"
            )
            continue

        except ValueError:
            print(
                f"{player_name}: Lỗi dữ liệu không hợp lệ!"
            )
            continue


# Chạy hệ thống
process_player_statistics(player_stats_list)