### Negative number are represented in 2's complement form

> - Range of numbers: [-2^(n-1), 2^(n-1)-1]
> - n: number of bits

## Step to get 2's complement of a number:

1. Get 1's complement of the number i.e invert all the bits
2. Add 1 to the 1's complement

Example: n =4 and number = -3

1. 3 = 0011
2. 1's complement of 3 = 1100
3. 2's complement of 3 = 1101 , which is -3

### Direct formula to get 2's complement of a number: _2^n - number_

In case of unsigned number the range is 0 to 2^n -1
