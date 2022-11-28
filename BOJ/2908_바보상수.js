const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString()

const [A, B] = input.trim().split(' ').map(
  x => parseInt(x.split('').reverse().join(''))
)

console.log(A > B ? A : B)
