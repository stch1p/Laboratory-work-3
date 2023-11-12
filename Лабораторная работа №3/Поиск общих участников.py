def find_common_participants(first_group, second_group, separator=','):
    participants_first = set(first_group.split(separator))
    participants_second = set(second_group.split(separator))

    common_partical = sorted(list(set(participants_first).intersection(participants_second)))
    return common_partical

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(f"Общие участники {find_common_participants(participants_first_group, participants_second_group, separator='|')}")
