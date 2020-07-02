// constant variables
// const sucess = '', fail = ''; 

//solution
const solution = () => {}
        
const { createInterface } = require('readline'); 
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    
let T = 0, t = 1, X = 0, Y = 0; 
rl.on('line', line => {
    if (T === 0) { // get nums of Test Case
        T = parseInt(line);
    } else if (X === 0) {
        // get data for each Case
        [X, Y] = line.split(' ').map(e => parseInt(e));
        // slove
        const y = solution(X, Y);
        // print
        console.log(`Case #${t++}: ${y}`);
        if (T < t) {
            rl.close();
        }
        // init
        X = 0;
    }
});