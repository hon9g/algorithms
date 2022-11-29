const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const input = require('fs').readFileSync(LOCAL_PATH).toString().trim().split('\n')

const N = parseInt(input.shift())
const CONDITION = {
  O: 'YES',
  X: 'NO',
}
const PS = {
  OPEN: '(',
  CLOSE: ')',
}

const results = []

for (let i = 0; i < input.length; i++) {
  let open = 0
  let close = 0
  let result
  for (let j = 0; j < input[i].length; j++) {
    switch (input[i][j]) {
      case PS.OPEN:
        open++
        break
      case PS.CLOSE:
        close++
        break
    }
    if (close > open) {
      result = CONDITION.X
      break
    }
  }
  results.push(result ?? (open === close ? CONDITION.O : CONDITION.X))
}

const resultsOutfit = results.join('\n')
console.log(resultsOutfit)
