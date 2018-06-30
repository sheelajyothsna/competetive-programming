import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;
import java.util.*;

public class Solution{

    // fill in the definitions for push(), pop(), and getMax()
    
    static Stack<Integer> s1=new Stack<>();
    static Stack<Integer> maxstack=new Stack<>();
    public static class MaxStack {

        public void push(int item) {
            if(maxstack.empty() || maxstack.peek()<=item)
            {
                maxstack.push(item);
            }
            s1.push(item);
        }

        public int pop() {
            if (s1.empty())
            {
            throw new EmptyStackException();
            }
            int k=s1.pop();
            if(maxstack.peek() == k) maxstack.pop();
            return k;
        }

        public int getMax() {
            
            return maxstack.peek();
        }
    }


    // tests

    @Test
    public void maxStackTest() {
        final MaxStack s = new MaxStack();
        s.push(5);
        assertEquals("check max after 1st push", 5, s.getMax());
        s.push(4);
        s.push(7);
        s.push(7);
        s.push(8);
        assertEquals("check before 1st pop", 8, s.getMax());
        assertEquals("check pop #1", 8, s.pop());
        assertEquals("check max after 1st pop", 7, s.getMax());
        assertEquals("check pop #2", 7, s.pop());
        assertEquals("check max after 2nd pop", 7, s.getMax());
        assertEquals("check pop #3", 7, s.pop());
        assertEquals("check max after 3rd pop", 5, s.getMax());
        assertEquals("check pop #4", 4, s.pop());
        assertEquals("check max after 4th pop", 5, s.getMax());
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