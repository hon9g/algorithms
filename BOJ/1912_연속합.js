const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim().split('\n')

const N = parseInt(input[0])
const nums = input[1].split(' ').map(x => parseInt(x))

for (let i = 1; i < N; i++) {
  nums[i] = Math.max(nums[i], nums[i] + (nums[i-1] ?? 0))
}

console.log(Math.max(...nums))
