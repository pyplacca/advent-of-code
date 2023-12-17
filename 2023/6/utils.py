def find_ways_to_win(time_limit, record_distance, speed_per_millisecond=1):
    hold_duration = 0  # in milliseconds
    result = 0

    while hold_duration <= time_limit:
        distance = hold_duration * speed_per_millisecond * (time_limit - hold_duration)
        result += distance > record_distance
        hold_duration += 1

    return result
