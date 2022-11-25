// @ts-check

const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(BOJ_PATH, "utf-8").trim().split('\n')

const V = parseInt(input[2])
const nums = input[1].split(' ').map(x => parseInt(x))

let cnt = 0

for (const n of nums) {
  if (n === V) {
    cnt++
  }
}

console.log(cnt)
