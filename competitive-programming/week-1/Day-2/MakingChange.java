import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import java.util.*;

import static org.junit.Assert.*;

public class MakingChange {

   public static int changePossibilities(int amount, int[] denominations) {

        // calculate the number of ways to make change
        int[] coins = new int[amount+1];
        int m=denominations.length;
        
        for(int i = 0; i < amount+1 ; i++)
        {
            coins[i] = 0;
        }
        
        coins[0] = 1;
        
        for(int coin: denominations)
            for(int j= coin; j < coins.length; j++ )
                coins[j] = coins[j]+coins[j-coin];

        return coins[amount];


   }
    
    // tests

    @Test
    public void sampleInputTest() {
        final int actual = changePossibilities(4, new int[] {1, 2,3});
        final int expected = 4;
        assertEquals(expected, actual);
    }

    @Test
    public void oneWayToMakeZeroCentsTest() {
        final int actual = changePossibilities(0, new int[] {1, 2});
        final int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void noWaysIfNoCoinsTest() {
        final int actual = changePossibilities(1, new int[] {});
        final int expected = 0;
        assertEquals(expected, actual);
    }

    @Test
    public void bigCoinValueTest() {
        final int actual = changePossibilities(5, new int[] {25, 50});
        final int expected = 0;
        assertEquals(expected, actual);
    }

    @Test
    public void bigTargetAmountTest() {
        final int actual = changePossibilities(50, new int[] {5, 10});
        final int expected = 6;
        assertEquals(expected, actual);
    }

    @Test
    public void changeForOneDollarTest() {
        final int actual = changePossibilities(100, new int[] {1, 5, 10, 25, 50});
        final int expected = 292;
        assertEquals(expected, actual);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}