const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, 'utf-8').trim().split('\n')

const [N, M] = input.shift().split(' ').map(x => parseInt(x))
const board = input.map(
  row => row.split('').map(_ => ({
    b: 0, // 검정으로 시작했다고 했을 때, 바뀌어야하는 칸 수.
    w: 0 // 하양으로 시작했다고 했을 때, 바뀌어야하는 칸 수.
  })) // 가로 방향 누적으로 셀 것임.
)

for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    if (input[n][m] === "B") {
      if (n % 2 === 0) {
        board[n][m].b = (m % 2 === 0) ? 0 : 1
        board[n][m].w = (m % 2 === 0) ? 1 : 0
      } else {
        board[n][m].b = (m % 2 === 0) ? 1 : 0
        board[n][m].w = (m % 2 === 0) ? 0 : 1
      }
    }
    if (input[n][m] === "W") {
      if (n % 2 === 0) {
        board[n][m].b = (m % 2 === 0) ? 1 : 0
        board[n][m].w = (m % 2 === 0) ? 0 : 1
      } else {
        board[n][m].b = (m % 2 === 0) ? 0 : 1
        board[n][m].w = (m % 2 === 0) ? 1 : 0
      }
    }
    board[n][m].b += board[n][m - 1]?.b ?? 0
    board[n][m].w += board[n][m - 1]?.w ?? 0
  }
}

console.log(board)

let num = N * M
let b = 0
let w = 0

for (let n = 0; n < N; n++) {
  for (let m = 0; m <= M - 8; m++) {
    b += board[n][m + 7].b
    w += board[n][m + 7].w
    if (m + 7 >= 8) {
      b -= board[n][m - 1].b
      w -= board[n][m - 1].w
      console.log('-', n, m-1, board[n][m-1])
    }
    if (n >= 8) {
      b -= board[n - 8][m + 7].b
      w -= board[n - 8][m + 7].w
      console.log('-', n-8, m+7, board[n-8][m+7])
    }
    if (n >= 7 && m + 7 >= 7) {
      num = Math.min(b, w, num)
      console.log(`n: ${n}, m: ${m}`, b, w, num)
    }
  }
}

console.log(num)
