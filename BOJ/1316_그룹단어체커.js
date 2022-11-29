const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim().split('\n')

const N = parseInt(input.shift())
let nonGroupWordNum = 0

for (const word of input) {
  const seen = new Set()
  let prev
  for (const char of word) {
    if (seen.has(char) && prev !== char) {
      nonGroupWordNum++
      break
    }
    prev = char
    seen.add(char)
  }
}

console.log(input.length - nonGroupWordNum)
