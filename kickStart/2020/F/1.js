/** 
 * 
 * @param {Number} N the number of people standing in the queue
 * @param {Number} X the maximum amount that a person can withdraw at a time
 * @param {Number[]} A the amount of money i-th person want to withdraw
 * @return {} the order in which all the people leave the queue
 */
const tle_solution = (N, X, A) => {
  const result = []
  let B = A.map((x, i) => [x, i+1])
  while (B.length) {
    B[0][0] -= X
    const [x, i] = B.shift()
    if (x <= 0) {
      result.push(i)
    } else {
      B.push([x, i])
    }
  }
  return result.join(' ')
};

/**
 * 
 * @param {Number} N the number of people standing in the queue
 * @param {Number} X the maximum amount that a person can withdraw at a time
 * @param {Number[]} A the amount of money i-th person want to withdraw
 * @return {} the order in which all the people leave the queue
 */
const solution = (N, X, A) => {
  let B = A.map((x, i) => [Math.ceil(x/X), i+1])
  return B.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] < b[1] ? -1 : 1
    }
    return a[0] < b[0] ? -1 : 1
  })
  .map(x => x[1])
  .join(' ')
};
      
const { createInterface } = require('readline'); 
  
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
  
let T = 0, t = 1, N = 0, X = 0, A = []; 
rl.on('line', line => {
  if (T === 0) {
      T = parseInt(line);
  } else if (N === 0) {
      [N, X] = line.split(' ').map(e => parseInt(e));
  } else {
      A = line.split(' ').map(e => parseInt(e));
      const y = solution(N, X, A);
      console.log(`Case #${t++}: ${y}`);
      if (T < t) {
          rl.close();
      }
      N = 0;
  }
});