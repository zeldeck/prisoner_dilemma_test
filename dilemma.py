import random

def run_auto_simulation_full(rounds=10_000):
    print("В данной программе я хочу проверить теорию дилеммы заключённого")
    print('Если двоих преуступников поймали и рассадили по камерам, им выгоднее молчать или сдать?')
    print('Для проверки есть три условия - хороший, плохой и случайный в зависимости от поведения.')
    print('Количество эпизодов: 10_000')
    print('Как будете готовы к тесту нажмите любую клавишу')
    input('')

    good_cop_years = 0
    robot_vs_good_years = 0

    bad_cop_years = 0
    robot_vs_bad_years = 0

    random_player_years = 0
    robot_vs_random_years = 0

    for _ in range(rounds):

        robot_move = random.randint(0, 1)

        if robot_move == 0:
            good_cop_years += 0
            robot_vs_good_years += 0
        else:
            good_cop_years += 5
            robot_vs_good_years += 0

        if robot_move == 0:
            bad_cop_years += 0
            robot_vs_bad_years += 5
        else:
            bad_cop_years += 3
            robot_vs_bad_years += 3

        player_random_move = random.randint(0, 1)
        if player_random_move == 0 and robot_move == 0:
            random_player_years += 0
            robot_vs_random_years += 0
        elif player_random_move == 1 and robot_move == 1:
            random_player_years += 3
            robot_vs_random_years += 3
        elif player_random_move == 1 and robot_move == 0:
            random_player_years += 0
            robot_vs_random_years += 5
        else:  # 0 и 1
            random_player_years += 5
            robot_vs_random_years += 0

    print(f"Тест на {rounds} раундов")
    print(
        f"'Хороший коп': Вы отсидели {good_cop_years} лет. Робот отсидел {robot_vs_good_years} лет."
    )
    print(
        f"'Плохой коп': Вы отсидели {bad_cop_years} лет. Робот отсидел {robot_vs_bad_years} лет."
    )
    print(
        f"'Чисто наугад': Вы отсидели {random_player_years} лет. Робот отсидел {robot_vs_random_years} лет."
    )


run_auto_simulation_full(10_000)
