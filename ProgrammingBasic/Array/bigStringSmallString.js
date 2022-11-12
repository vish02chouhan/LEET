function smallestSubstringContaining(bigString, smallString) {
    // Write your code here.const charMap = {};    
    for (let char of smallString) {
        charMap[char] = (charMap[char] || 0) + 1;
    }
    let left = 0;
    let right = -1;
    let countNeeded = Object.keys(charMap).length;
    let res = '';
    while (right <= bigString.length) {
        if (countNeeded === 0) {
            if (!res || res.length > right - left) {
                res = bigString.slice(left, right + 1);
            }
            const leftChar = bigString[left];
            if (leftChar in charMap) charMap[leftChar]++;
            if (charMap[leftChar] === 1) {
                countNeeded++;
            }
            left++;
        } else {
            right++;
            const rightChar = bigString[right];
            if (rightChar in charMap)
                charMap[rightChar]--;
            if (charMap[rightChar] === 0) countNeeded--;
        }
    }
    return res;
}


let bigString = 'abcd$ef$axb$c$'
let smallString = "$$abf"
console.log(smallestSubstringContaining(bigString,  smallString))