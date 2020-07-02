//solution
const solution = (arr, k) => {
  let res = 0, i = -1;
  while (++i < arr.length) {
    if (k === arr[i]) {
      for (let cur = k; 0 <= cur; cur--) {
        if (cur === 0) {
          res++;
          break;
        }
        if (cur !== arr[i]) {
          i--;
          break;
        }
        i++;
      }
    }
  }
  return res;
}
        
const { createInterface } = require('readline'); 
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    
let T = 0, t = 1, N = 0, K = 0;
rl.on('line', line => {
  if (T === 0) { // get nums of Test Case
      T = parseInt(line);
  } else if (N === 0) {
    [N, K] = line.split(' ').map(e => parseInt(e));
  } else {
    const arr = line.split(' ').map(e => parseInt(e));
    const y = solution(arr, K);
    console.log(`Case #${t++}: ${y}`);
    N = 0;
    if (T < t) {
      rl.close();
    }
  }
});