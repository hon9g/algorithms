const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim()
const [N, M] = input.split(' ').map(x => parseInt(x))

const sequence = []

const backtrack = (N, M, result, seen) => {
  if (result.length === M) {
    sequence.push(result)
    return
  }
  for (let n = 1; n <= N; n++) {
    if (seen.has(n)) {
      continue
    }
    const nextResult = [...result, n]
    backtrack(N, M, nextResult, new Set(nextResult))
  }
}

backtrack(N, M, [], new Set())


for (const result of sequence) {
  console.log(result.join(' '))
}
