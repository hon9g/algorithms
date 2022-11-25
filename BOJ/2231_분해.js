const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = parseInt(fs.readFileSync(BOJ_PATH, 'utf-8').trim())

let result = 0

for (let n = 1; n < input; n++) {
  const sum = n + n.toString().split('').reduce((sum, m) => sum + parseInt(m), 0)
  if (input === sum) {
    result = n
    break
  }
}

console.log(result)
