from typing import List, Union

#discover degrees;
def connections(graph) -> dict:
    connections = {}
    for i in graph:
        for j in i:
            if j not in connections:
                connections[j] = 0;
            connections[j] += 1;

    return connections

#to find out if you are a eulerian;
def checkGraphEulerian(graph: List[List[int]]) -> bool:
    connect = connections(graph);
    for i in connect:
        degress = connect[i] % 2
        if (degress != 0): 
            return False

    return True


#to find out if you are a semi eulerian;
def checkGraphSemiEulerian(graph: List[List[int]]) -> bool:
    connect = connections(graph)
    count = 0

    for i in connect:
        degress = connect[i] % 2
        if (degress != 0): 
            count += 1

        if (count > 3): 
            return False

    return count == 2


# to find out if you are not an eulerian;
def checkNoGraphEulerian(graph: List[List[int]]) -> bool:
    return (not checkGraphEulerian(graph) and not checkGraphSemiEulerian(graph))


#graph with connections;
graphs = [
            [
                [1, 2], [1, 3], [1, 6], [1, 7], [2, 3], [2, 4], [2, 6], [3, 4], [3, 5], [4, 5], [4, 7], [5, 6], [5, 7], [6, 7],
            ],
            [ 
                [1, 2], [1, 3], [1, 6], [1, 7], [2, 3], [2, 4], [2, 6], [3, 4], [4, 5], [4, 7], [5, 6],  [5, 7], [6, 7],
            ],
            [
                [1, 2], [1, 3], [1, 6], [1, 7], [2, 3], [3, 4], [4, 5], [5, 6], [5, 7], [6, 7],
            ],
            [
                [1, 2], [1, 3], [1, 6], [1, 7], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7],
            ]
]

for graph in graphs:

    print(f'Graph is eulerian: {checkGraphEulerian(graph)}')
    print(f'Graph is semi eulerian: {checkGraphSemiEulerian(graph)}')
    print(f'Graph not is eulerian: {checkNoGraphEulerian(graph)}')
    print('____________________________________________________________')