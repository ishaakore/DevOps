import numpy as np

def nearest_neighbor_tsp(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = []
    total_distance = 0

   
    current_city = 0
    visited[current_city] = True
    tour.append(current_city)

    for _ in range(n - 1):
        
        nearest_city = None
        min_distance = float('inf')

        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                nearest_city = city
                min_distance = distance_matrix[current_city][city]

            
        visited[nearest_city] = True
        tour.append(nearest_city)
        total_distance += min_distance
        current_city = nearest_city

    
    total_distance += distance_matrix[current_city][tour[0]]
    tour.append(tour[0])

    return tour, total_distance


if __name__ == "__main__":
    distance_matrix = np.array([
        [0, 10, 15, 20],
        [10, 0, 36, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])

    tour, total_distance = nearest_neighbor_tsp(distance_matrix)
    print("Name: Isha Kore")
    print("Student Id: 242191010")
    print("Batch: A")
    print("Tour:", tour)
    print("Total Distance:", total_distance)