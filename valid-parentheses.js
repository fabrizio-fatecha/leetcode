/**
 * @param {string} s
 * @return {boolean}
 * 
 */
var isValid = function(s) {
    
    const OPTIONS = [['(','{','['],[')','}',']']];
    const STRING_ARRAY = s.split('');

    const pair = (opening,closure,array) => {

        let openings = 0;
        let closures = 0;

        for (let index = 0; index < array.length; index++) {
            const element = array[index];
            for(let subIndex = 0; subIndex < opening.length ; subIndex++){
                if (element === opening[subIndex]) {openings++;}
                if (element === closure[subIndex]) {closures++;}
            }
        }

        if (condition) {
            
        }

        return openings === closures
    }

    return pair(OPTIONS[0],OPTIONS[1],STRING_ARRAY)

};

console.log(isValid('(]'));