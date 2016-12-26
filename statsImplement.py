import stats

stats.init()
stats.event_occured("meal_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("diet_started")
stats.event_occured("meal_eaten")
stats.event_occured("meal_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("meal_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("diet_abandoned")
stats.event_occured("snack_eaten")
stats.event_occured("meal_eaten")
stats.event_occured("snack_eaten")
stats.event_occured("meal_eaten")
stats.event_occured("snack_eaten")

for event, num_times in stats.get_stats():
    print("{} occured {} times".format(event, num_times))
