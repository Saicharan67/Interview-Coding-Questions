/*

You’re given coins of different denominations and a total amount of money. From that, you need to write a function to compute the fewest number of coins that you need to make up that amount. If you can’t reach the given amount of money with any combination of the coins, you return -1

*/

#include <iostream>
using namespace std;
 
int countChange(int denoms[], int denomsLength, int amount) {

  if(amount <= 0 || denomsLength <= 0)
    return 0;
  
  int i, j, x, y;

  int lookupTable[amount + 1][denomsLength];
 

  for (i = 0; i < denomsLength; i++)
    lookupTable[0][i] = 1;
 
 
  for (i = 1; i < amount + 1; i++) {
    for (j = 0; j < denomsLength; j++) {

      x = (i - denoms[j] >= 0) ? lookupTable[i - denoms[j]][j] : 0;
 
      y = (j >= 1) ? lookupTable[i][j - 1] : 0;

      lookupTable[i][j] = x + y;
    }
  }
  return lookupTable[amount][denomsLength - 1];
}
 
int main() { 
  int denoms[4] = {25,10,5,1};
  cout << countChange(denoms, 4, 10) << endl;
}
