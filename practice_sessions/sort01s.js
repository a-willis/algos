/* 
Given an array of 0s and 1s, group all 0s on one side and 1s on the other side using the minimum number of moves possible. A "move" is a swap between any adjacent positions. 

[0, 1, 1, 0, 1] => 2 
[0, 1, 1, 0, 0, 1] => 4

[1, 0] => 0
[0, 1] => 0

[1,0,1,1,0,1] =>  4

- 1. bubble sort
- 2. How many moves does it take to get all 0s to left and all 1s to right?
- 2b. How many moves does it take to get all 0s to right and all 1s to left?
- 3. There are only 2 possible end states per input


[0, 1, 1, 0, 1] -> [0, 0, 1, 1, 1]  2
[0, 1, 1, 0, 0, 1] -> [0, 0, 0, 1, 1, 1] 4
[0, 0, 1, 1, 0, 1, 0, 1] -> [0, 0, 0, 1, 1, 1, 1] 5
                   ^
    
ones = 3
swaps = 2
*/

function group0s1s(input) {
  let ones = 0;
  let swaps = 0;
  for (let el of input) {
    if (el === 1) ones += 1;
    else {
      // 0
      swaps += ones;
    }
  }

  // num swaps to get to 0s on right
  let zeros = 0;
  let swaps2 = 0;
  for (let el of input) {
    if (el === 0) zeros += 1;
    else {
      // 0
      swaps2 += zeros;
    }
  }

  return Math.min(swaps, swaps2);
}

console.log(group0s1s([0, 1, 1, 0, 1]), 2);
console.log(group0s1s([0, 1, 1, 0, 1]), 2);
console.log(group0s1s([0, 1, 1, 0, 0, 1]), 4);
console.log(group0s1s([0, 1]), 0);
console.log(group0s1s([1, 0]), 0);




[0,1,2,0,0,2,1]

- create dictionary counts {}
- iterate array
      count how many of each 0,1,2 are in array
      counts 

      