const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, 'utf-8').trim().split('\n')

const N = parseInt(input.shift())
const queries = input
  .map((query) => query.split(' '))
  .map(([n, str]) => [parseInt(n), str])

for (const query of queries) {
  const [n, str] = query
  const result = str.split('').map(c => c.repeat(n))
  console.log(result.join(''))
}
