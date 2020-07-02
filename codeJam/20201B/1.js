const name = 'SNWE';
const xy = [[0, -1], [0, 1], [-1, 0], [1, 0]];

const solution = (X, Y) => {
    if (Math.abs(X)%2 === Math.abs(Y)%2) {
        return 'IMPOSSIBLE';
    }
    const candidate = [];
    backtrack(0, 0, 0, []);
    // console.log(candidate);
    return candidate.reduce((old, cur) => {
        if (!old.length) return cur;
        return old.length > cur.length ? cur : old;
    }, []).join('');
    
    function backtrack(idx, x, y, path) {
        // console.log(x, y, X, Y, typeof(X), typeof(x), path);
        if (x === X && Y === y) {
            candidate.push(path.filter(e => true));
            return;
        }
        if (Math.pow(2, idx) < Math.abs(X) + Math.abs(Y)) {
            for (let i = 0; i < 4; i++) {
                path.push(name[i]);
                x += Math.pow(2, idx) * xy[i][0];
                y += Math.pow(2, idx) * xy[i][1];
                const ans = backtrack(idx + 1, x, y, path);
                path.pop();
                x -= Math.pow(2, idx) * xy[i][0];
                y -= Math.pow(2, idx) * xy[i][1];
            }
        }
    }
};
        
const { createInterface } = require('readline'); 
    
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    
let T = 0, t = 1, X = 0, Y = 0; 
rl.on('line', line => {
    if (T === 0) {
        T = parseInt(line);
    } else if (X === 0) {
        [X, Y] = line.split(' ').map(e => parseInt(e));
        const y = solution(X, Y);
        console.log(`Case #${t++}: ${y}`);
        if (T < t) {
            rl.close();
        }
        X = 0;
    }
});