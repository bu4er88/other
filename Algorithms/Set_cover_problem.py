def best_stations_search(states_needed, stations):
    final_stations = []
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = list(set(states_needed) & set(states))
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = set(covered)
        states_needed = list(set(states_needed) - states_covered)
        final_stations.append(best_station)
    print(final_stations)


states_needed = ['A', 'B', 'C', 'D', 'E', 'F']
stations = {
    '1': ['A', 'B', 'C'],
    '2': ['C', 'E'],
    '3': ['D', 'E', 'F'],
    '4': ['B', 'D', 'E', 'F']
}
best_stations_search(states_needed, stations)
"""
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
c = a & b
print(c)"""