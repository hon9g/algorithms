// @ts-check

/** Represent Graph
 * @class
 */
class Graph {
    /** init
     * @param {number} n Number of vertices
     */
    constructor(n) {
        /** @member {Array.<Array.<number>>} list Adjacent List */
        this.list = Array.from(new Array(n + 1), () => [])
    }
    /** Add a edge 
     * @param {number} a vertice 1
     * @param {number} b vertice 2
    */
    add(a, b) {
        this.list[a].push(b)
        this.list[b].push(a)
    }

    /** Get adjecent vertices
     * @param {number} v current vertice
     * @return {Array.<number>} Adjecent vertices of the vertice v
    */
    get(v) {
        return this.list[v]
    }

    /** Sort graph */
    sort() {
        for (let i = 1; i < this.list.length; i++) {
            this.list[i].sort()
        }
    }
}

/** Traverse a graph by Depth First Search
 * @param {Object} o
 * @param {number} o.v Current vertice
 * @param {Graph} o.graph a graph to traverse
 * @param {Set<number>} o.visited Store the visited vertices
 * @param {Array.<number>} o.path Path from start vertice to current vertice
 * @return {Array.<number>} Path from start vertice to end vertice
*/
const DFS = ({ v, graph, visited, path }) => {
    if (visited.has(v)) {
        return path
    }
    const nexts = graph.get(v)
    visited.add(v)
    path.push(v)
    for (const u of nexts) {
        DFS({ v: u, graph, visited, path})
    }
    return path
}

/** Traverse a graph by Breadth First Search
 * @param {Object} o
 * @param {number} o.v  Current vertice
 * @param {Graph} o.graph a graph to traverse
 * @return {Array.<number>} Path from start vertice to end vertice
 */
const BFS = ({ v, graph }) => {
    const path = []
    const visited = new Set()
    const queue = [v]
    while (queue.length) {
        const u = queue.shift()
        if (visited.has(u)) {
            continue
        }
        path.push(u)
        visited.add(u)
        queue.push(...graph.get(u))
    }
    return path
}

// main
const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, "utf-8").trim().split('\n')

const [N, M, V] = input.shift().split(' ').map(x => parseInt(x))
const graph = new Graph(N)

for (const line of input) {
    const [a, b] = line.split(' ').map(x => parseInt(x))
    graph.add(a, b)
}

graph.sort()

const dfsResult = DFS({ v: V, graph, visited: new Set(), path: [] }).join(' ')
const bfsResult = BFS({ v: V, graph }).join(' ')

console.log(dfsResult)
console.log(bfsResult)
