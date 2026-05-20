def rssi_to_distance(filtered_rssi):

    distance = 10 ** ((A - filtered_rssi) / (10 * N))

    return distance



