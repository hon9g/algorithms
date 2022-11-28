const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim()
const alphabets = new Set (['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])

let idx = 0
let count = 0

while (idx < input.length) {
  if (alphabets.has(input.substring(idx, idx + 2))) {
    idx += 2
    count++
    continue
  }
  if (alphabets.has(input.substring(idx, idx + 3))) {
    idx += 3
    count++
    continue
  }
  count++
  idx++
}

console.log(count)
