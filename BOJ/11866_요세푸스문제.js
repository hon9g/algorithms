const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const [N, K] = require('fs').readFileSync(LOCAL_PATH).toString().trim()
  .split(' ').map(x => parseInt(x))


const removed = new Set()
const sequence = []
let n = 0

while (removed.size < N) {  
  let k = 0
  while (k < K) {
    k++
    n++
    while (removed.has(n)) {
      n++
      if (n > N) {
        n %= N
      }
    }
    if (n > N) {
      n %= N
    }
  }
  removed.add(n)
  sequence.push(n)
}

console.log(`<${sequence.join(', ')}>`)
