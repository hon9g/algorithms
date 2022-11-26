const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, 'utf-8').trim().split('\n')

const N = parseInt(input.shift())
const people = input.map(
  (person, i) => [...person.split(' ').map(x => parseInt(x))]
)

const getScore = (a, b) => {
  if (a[0] < b[0] && a[1] < b[1]) {
    return 1
  }
  if (a[0] > b[0] && a[1] > b[1]) {
    return -1
  }
  return 0
}

const ranks = new Array(N)

for (let i = 0; i < N; i++) {
  let rank = 1
  for (let j = 0; j < N; j++) {
    if (getScore(people[i], people[j]) === 1) {
      rank++
    }
  }
  ranks[i] = rank
}

console.log(ranks.join(' '))
