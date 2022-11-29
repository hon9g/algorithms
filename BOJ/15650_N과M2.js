const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim()
const [N, M] = input.split(' ').map(x => parseInt(x))

const sequence = []

const backtrack = (N, M, result) => {
  if (result.length === M) {
    sequence.push(result)
    return
  }
  for (let n = (result[result.length - 1] ?? 0) + 1; n <= N; n++) {
    backtrack(N, M, [...result, n])
  }
}

backtrack(N, M, [])


for (const result of sequence) {
  console.log(result.join(' '))
}
