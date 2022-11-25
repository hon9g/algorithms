// @ts-check

const BOJ_PATH = 'dev/stdin'
const LOCAL_PATH = `${__dirname}/stdin/test1.txt`

const fs = require('fs')
const input = fs.readFileSync(LOCAL_PATH, "utf-8").trim().split('\n')
  .map(x => parseInt(x))

const STUDENT_NUM = 30
const checkSheet = new Array(STUDENT_NUM).fill(false)

for (const n of input) {
  checkSheet[n-1] = true
}

let cnt = 0
const CALL_LIMIT = 2
for (let i = 0; i < STUDENT_NUM; i++) {
  if (!checkSheet[i]) {
    console.log(i + 1)
    cnt++
  }
  if (cnt === CALL_LIMIT) {
    break
  }
}
