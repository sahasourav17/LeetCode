/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
 var decodeMessage = function (key, message) {
    const subTable = {

    };

    let initCharCode = 97;

    for (let i = 0; i < key.length; i++) {
        if (key[i].trim() && !subTable[key[i]]) {
            subTable[key[i]] = String.fromCharCode(initCharCode);
            initCharCode++;
        }
    }

    let decodedStr = "";

    for (let i = 0; i < message.length; i++) {
        if (message[i] === " ") {
            decodedStr += " ";
        } else {
            decodedStr += subTable[message[i]];
        }
    }

    return decodedStr;
};