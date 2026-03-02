const romanToInt = function (s) {

    const LETTERS = ["I", "V", "X", "L", "C", "D", "M"];
    const NUMBERS = [1, 5, 10, 50, 100, 500, 1000];
    const LETTERS_ARRAY = s.split('');

    let values = [];
    let sum = 0;

    for (let i = 0; i < LETTERS_ARRAY.length; i++) {
        let value = NUMBERS[LETTERS.indexOf(LETTERS_ARRAY[i])];
        values.push(value);
    }

    for (let i = 0; i < values.length; i++) {
        if (values[i] < values[i + 1] && values[i] !== 0 && values[i + 1] !== 0) {
            values[i] = (values[i] - values[i + 1]) * -1;
            values[i + 1] = 0;
        }
    }

    values.forEach(element => { sum += element; });
    return sum;
}