const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, 'utf-8').trim().toLocaleUpperCase()

const count = new Array(26).fill(0)
const startCode = 'A'.charCodeAt()

let maxCount = 0

for (const e of input) {
  const code = e.charCodeAt() - startCode
  maxCount = Math.max(++count[code], maxCount)
}

let maxChar

for (let i = 0; i < 26; i++) {
  if (count[i] === maxCount) {
    maxChar = !maxChar ? String.fromCharCode(startCode + i) : '?'
  }
}

console.log(maxChar)
