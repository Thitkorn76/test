import heapq

def display_menu():
    print("---Location selection menu---")
    print("1 นครนายก")
    print("2 รังสิต")
    print("3 โคราช")
    print("4 รามอินทรา")
    print("5 บางแสน")
    print("6 บางนา")
    print("7 บางพลัด")
    print("8 The Fourth")
    print("9 พระราม 2")
    print("10 me")
    print("11 exit")

def get_source_and_destination():
    display_menu()
    selection = input("Select source location (1-10), or '11' to exit: ")
    if selection == '11':
        return None, None
    start_point = selection
    end_point = input("Select destination location (1-10): ")
    places = {"1": "นครนายก", "2": "รังสิต", "3": "โคราช", "4": "รามอินทรา","5": "บางแสน", "6": "บางนา", "7": 
        "บางพลัด", "8": "The Fourth", "9": "พระราม 2","10": "me"}
    start = places.get(start_point)
    end = places.get(end_point)

    if start is None or end is None:
        print("Invalid location selection")
        return None, None

    return start, end

def find_shortest_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  
    queue = [(0, start)]
    previous_nodes = {}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance 
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    path = []
    current = end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)
    return path, distances[end]

def main():
    while True:
        start, end = get_source_and_destination()
        if start is None or end is None:
            break
        routes = {
            "นครนายก": {"me":1.82, "โคราช":17.4, "รังสิต":9.22, "บางแสน":15.4,},
            "โคราช": {"me":16.6,"นครนายก":17.4,},
            "รังสิต": {"me":10.9,"นครนายก":9.22,"รามอินทรา":2.26,},
            "รามอินทรา": {"รังสิต":2.26,"บางแสน":10.5,"บางนา":3.53,"The Fourth": 4.63,"บางพลัด": 2.06},
            "บางพลัด": {"รามอินทรา":2.06,"The Fourth":2.19,"พระราม 2":2.12,"บางนา":3.01},
            "The Fourth": {"รามอินทรา":4.63,"พระราม 2":2.05,"บางพลัด":2.19},
            "พระราม 2": {"The Fourth":2.05,"บางพลัด":2.12,"บางนา":3.53},
            "บางนา": {"บางแสน":7.63,"พระราม 2":3.53,"บางพลัด":3.01,"รามอินทรา":3.53},
            "บางแสน": {"บางนา":7.63,"รามอินทรา":10.5,"นครนายก":15.4,"me":15.6},
            "me": {"โคราช":16.6,"นครนายก":1.82,"บางแสน":15.6,"รังสิต":10.9}
        }

        path, distance = find_shortest_path(routes, start, end)
        print(f"ระยะทางที่สิ้นที่สุดให้การเดินทางจาก {start} ไปยัง {end} ดังนี้: {' >>> '.join(path)}, Total distance: {distance*10} กิโลเมตร")
        
if __name__ == "__main__":
    main()