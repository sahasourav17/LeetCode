/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    const numString = num.toString();
    for(let i = 0; i < numString; i++){
        return numString.replace('6','9',1);
    }

    return Number(numString);
};