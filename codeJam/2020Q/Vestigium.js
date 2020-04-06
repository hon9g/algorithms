const solution = board => {
    let k = 0, r = 0, c = 0;
    const cols = [];
    for (let i = 0; i < board.length; i++) {
        const rows = new Set();
        for (let j = 0; j < board.length; j++) {
            if (i === 0) {
                cols.push(new Set());
            }
            if (i === j) {
                k += board[i][j];
            }
            rows.add(board[i][j]);
            cols[j].add(board[i][j]);
            if (i + 1 === board.length && cols[j].size !== board.length) {
                c++;
            }
        }
        if (rows.size !== board.length) {
            r++;
        }
    }
    return [k, r, c];
}

const { createInterface } = require('readline');

(async () => {
    const rl = createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let T = 0, t = 1, N = 0, board = [];
    
    rl.on('line', line => {
        if (T === 0) {
            T = parseInt(line);
            return;
        } else {
            if (N === 0) {
                N = parseInt(line);
                board = []
                return;
            } else {
                board.push(line.split(' ').map(e => parseInt(e)));
                if (board.length === N) {
                    const [k, r, c] = solution(board);
                    console.log(`Case #${t++}: ${k} ${r} ${c}`);
                    N = 0;
                }
            }
        }
        
    })

    await rl.close;
})();
