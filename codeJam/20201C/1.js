// constant variables
const sucess = '', fail = 'IMPOSSIBLE'; 
const way = {
  'N': [-1, 0],
  'S': [+1, 0],
  'E': [0, -1],
  'W': [0, +1],
}
let T = 0, t = 1, X = '#', Y = '#', M = '#';
//solution
const solution = (x, y, m) => {
  if (Math.abs(x) + Math.abs(y) === 0) return 0;
  for (let i = 0; i < m.length; i++) {
    const [ns, ew] = way[m[i]];
    x += ew;
    y += ns;
    if (Math.abs(x) + Math.abs(y) <= i + 1) {
      return i + 1;
    }
  }
  return fail;
}
const init = () => {
  X = '#'
  Y = '#'
  M = '#'
}


const { createInterface } = require('readline'); 
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    

rl.on('line', line => {
  if (T === 0) { // get nums of Test Case
    T = parseInt(line);
  } else if (X === '#') {
    // get data for each Case
    [X, Y, M] = line.split(' ');
    X = parseInt(X)
    Y = parseInt(Y)
    // slove
    const res = solution(X*-1, Y*-1, M);
    // print
    console.log(`Case #${t++}: ${res}`);
    if (T < t) {
        rl.close();
    }
    // init
    init();
  }
});