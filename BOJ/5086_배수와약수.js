// @ts-check

const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim()
  .split('\n').map(row => row.split(' ').map(x => parseInt(x)))

const END = 0
const condition = {
  f: 'factor',
  m: 'multiple',
  x: 'neither',
} 

for (const [a, b] of input) {
  if (a === END && b === END) {
    break
  }
  if (a === 0 || b === 0) {
    console.log(condition.x)
    continue
  }
  if (b / a === Math.floor(b / a)) {
    console.log(condition.f)
    continue
  }
  if (a / b === Math.floor(a / b)) {
    console.log(condition.m)
    continue
  }
  console.log(condition.x)
}
