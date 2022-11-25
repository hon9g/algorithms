const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(BOJ_PATH, 'utf-8').trim().split(' ')

const [A, B, C] = input.map(x => parseInt(x))

if (B >= C) {
  console.log(-1)
} else {
  console.log(Math.floor(A / (C - B) + 1))
}
