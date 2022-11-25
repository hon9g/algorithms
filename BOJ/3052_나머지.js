// @ts-check

const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(BOJ_PATH, 'utf-8').trim().split('\n')
  .map(x => parseInt(x))

const mods = new Set()

for (const n of input) {
  mods.add(n % 42)
}

console.log(mods.size)
