class PriorityQueue {
  constructor() {
    this.queue = []
  }
  enqueue(data, priority) {
    this.queue.push({ data, priority })
    this.sort()
  }
  dequeue() {
    return this.queue.shift()
  }
  sort() {
    this.queue.sort((a, b) => a.priority - b.priority)
  }
  isEmpty() {
    return !this.queue.length
  }
}

function dijkstra(graph, start, end) {
  const distances = {}
  const visited = {}
  const previous = {}
  const queue = new PriorityQueue()
  let currentNode

  for (const node in graph) {
    distances[node] = Infinity
    visited[node] = false
  }
  distances[start] = 0
  queue.enqueue(start, 0)

  while (!queue.isEmpty()) {
    currentNode = queue.dequeue().data
    visited[currentNode] = true

    for (const neighbor in graph[currentNode]) {
      const distance = distances[currentNode] + graph[currentNode][neighbor]

      // Update distance if new distance is shorter
      if (distance < distances[neighbor]) {
        distances[neighbor] = distance
        previous[neighbor] = currentNode
        queue.enqueue(neighbor, distance)
      }
    }
  }

  let path = [end]
  let lastStep = end
  while (lastStep !== start) {
    path.unshift(previous[lastStep])
    lastStep = previous[lastStep]
  }

  return { path, distance: distances[end] }
}

const graph = {
  A: { B: 2, C: 4, E: 7 },
  B: { A: 2, C: 1, D: 3, F: 5 },
  C: { A: 4, B: 1, D: 2, G: 3 },
  D: { B: 3, C: 2, F: 2, H: 4 },
  E: { A: 7, F: 3, I: 2 },
  F: { B: 5, D: 2, E: 3, G: 2, H: 6 },
  G: { C: 3, F: 2, H: 1 },
  H: { D: 4, F: 6, G: 1, I: 3 },
  I: { E: 2, H: 3 },
}

// Another graph example:

//const graph = {
//    "A": {"B": 1, "C": 4},
//    "B": {"C": 2, "D": 5},
//    "C": {"D": 1},
//    "D": {}
//  };
//

const { path, distance } = dijkstra(graph, 'A', 'I')
//  const { path, distance } = dijkstra(graph, "A", "D");
console.log('Shortest path:', path)
console.log('Shortest distance:', distance)
