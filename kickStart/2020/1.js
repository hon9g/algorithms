const solution = (N, B, H) => {
    H.sort((a,b) => a > b ? 1 : -1);
    return H.reduce((s, x) => {
        B -= x;
        return 0 <= B ? s + 1 : s;
    }, 0);
};
        
const { createInterface } = require('readline'); 
    
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    
let T = 0, t = 1, N = 0, B = 0, H = []; 
rl.on('line', line => {
    if (T === 0) {
        T = parseInt(line);
    } else if (N === 0) {
        [N, B] = line.split(' ').map(e => parseInt(e));
    } else {
        H = line.split(' ').map(e => parseInt(e));
        const y = solution(N, B, H);
        console.log(`Case #${t++}: ${y}`);
        if (T < t) {
            rl.close();
        }
        N = 0;
    }
});