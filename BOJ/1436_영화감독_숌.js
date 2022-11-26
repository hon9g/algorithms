const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, 'utf-8').trim()

const N = parseInt(input)
const cache = [-1]

let n = cache.length === 1 ? 666 : cache[cache.length - 1]

while(!cache[N]) {
  const regexp = /666/g;
  if (regexp.test(n.toString())) {
    cache.push(n)
  }
  n++
}

console.log(cache[N])
