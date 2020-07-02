const solution = (R, S) => {
    let deck = [];
    for (let s = 0; s < S; s++) {
        for (let r = 1; r <= R; r++) {
            deck.push(r);
        }
    }
    const op = [];
    while (1 < R) {
        let y = deck.pop(), b = [];
        if (y === R) {
            if (deck.indexOf(R) === -1) R--;
            continue;
        }
        while (y !== R) {
            b.unshift(y);
            y = deck.pop();
        }
        deck.push(y);
        deck.unshift(...b);
        op.push([deck.length - b.length, b.length]);
    }
    return [op.length, op];
};
        
const { createInterface } = require('readline'); 
    
const rl = createInterface({ input: process.stdin, output: process.stdout }); 
    
let T = 0, t = 1; 
rl.on('line', line => {
    if (T === 0) {
        T = parseInt(line);
    } else {
        const [R, S] = line.split(' ').map(e => parseInt(e));
        const [y, op] = solution(R, S);
        console.log(`Case #${t++}: ${y}`);
        for (o of op) {
            console.log(o.join(' '));
        }
        if (T < t) {
            rl.close();
        }
    }
});