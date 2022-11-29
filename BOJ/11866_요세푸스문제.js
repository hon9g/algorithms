const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const [N, K] = require('fs').readFileSync(LOCAL_PATH).toString().trim()
  .split(' ').map(x => parseInt(x))

const candidate = Array.from([...new Array(N).keys()].map(x => x + 1))
const sequence = []
let n = 0
while (sequence.length < N) {
  n += K
  n > candidate.length && (n = n % candidate.length)
  if (--n < 0) {
    n = candidate.length - 1
  }
  sequence.push(...candidate.splice(n, 1))
}

console.log(`<${sequence.join(', ')}>`)
