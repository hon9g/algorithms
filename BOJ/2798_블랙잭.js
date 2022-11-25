const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const [[N, M], cards] = fs.readFileSync(BOJ_PATH, 'utf-8')
  .trim()
  .split('\n')
  .map(X => X.split(' ').map(x => parseInt(x)))

let result = -1

for (let i = 0; i < N; i++) {
  for (let j = 1; j < N; j++) {
    if (j === i) {
      continue
    }
    for (let k = 2; k < N; k++) {
      if (k === i || k === j) {
        continue
      }
      const sum = cards[i] + cards[j] + cards[k]
      if (sum <= M) {
        result = Math.max(sum, result)
      }
    }
  }
}


console.log(result)
