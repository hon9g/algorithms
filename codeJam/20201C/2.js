var fs = require('fs');
var arr = fs.readFileSync('input2.txt').toString().split("\r\n");
// console.log(array.slice(0,5))

let memo = new Map();
let res = new Array(10).fill(-1);
let T = 0, t = 1, U = 0, l = 0; 

//solution
const solution = () => {
  for (let i = 0; i < 10; i++){
    for (key of memo.keys()) {
      if (memo.get(key) === i) {
        res[i] = key;
        break;
      }
    }
  }
}

const init = () => {
  memo.clear();
  res = new Array(10).fill(-1);
  U = 0; 
}

for (line of arr) {
    if (T === 0) { // get nums of Test Case
        T = parseInt(line);
    } else if (U === 0) {
        // get data for each Case
        U = parseInt(line);
    } else {
      const bound = Math.pow(10, U);
      const [m, r] = arr[l + 2].split(' ');
      for (let i = 0; i < r.length; i++) {
        let j = i - r.length + 1;
        let x = 0;
        j ? x = parseInt(m.slice(i, j)) : x = parseInt(m.slice(i));
        while (bound <= x) {
          x = parseInt(m.slice(i, --j))
        }
        memo.has(r[i]) ? memo.set(r[i], Math.min(memo.get(r[i]), x)) : memo.set(r[i], x);
      }
      if (++l === Math.pow(10, 4)) {
        // slove
        solution();
        // print
        console.log(`Case #${t++}: ${res.join('')}`); // Case #1: TPFOXLUSHB
        // if (T < t) {
        //     rl.close();
        // }
        // init
        init();
    }
  }
}
