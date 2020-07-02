// constant variables
// const sucess = '', fail = ''; 

//solution
const solution = (arr, d) => {
  if (arr.length === 1) return d-1;
  const cnt = new Map();
  let cut = 0;
  let maxP = 0, maxC = 0;
  for (a of arr) {
    if (cnt.has(a)) {
      if (d <= cnt.get(a) + 1) return 0;
      cnt.set(a, cnt.get(a) + 1);
    } else {
      cnt.set(a, 1);
    }
    if (maxP < cnt.get(a)) {
      maxP = a;
      maxC = cnt.get(a);
    }
  }
  cnt.delete(a);
  if (cnt.has(a * 2)) {
    while (cnt.get(a * 2)){    
      cut++;
      maxC += 2;
      cnt.set(a * 2, cnt.get(a * 2) - 1);
      if (d <= maxC) {
        return cut;
      }
    }
    cnt.delete(a * 2);
  }
  for (cnt.size) {
    
  }

}

const init = () => {
  N = '#';
  D = '#';
}

const { createInterface } = require('readline'); 
const rl = createInterface({ input: process.stdin, output: process.stdout }); 

let T = 0, t = 1, N = '#', D = '#'; 

rl.on('line', line => {
  if (T === 0) { // get nums of Test Case
    T = parseInt(line);
  } else if (N === 0) {
    // get data for each Case
    [N, D] = line.split(' ').map(e => parseInt(e));
  } else {
    const A = line.split(' ')
      .map(e => parseInt(e));
    const y = 1 < D ? solution(A, D) : 0;
    // print
    console.log(`Case #${t++}: ${y}`);
    if (T < t) {
        rl.close();
      }
    // init
    init();
  }
});