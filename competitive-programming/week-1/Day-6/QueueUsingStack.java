import java.util.Stack;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    // fill in the definitions for enqueue() and dequeue()
    
    public static class QueueTwoStacks {

        private Stack<Integer> s1 = new Stack<>();
        private Stack<Integer> s2 = new Stack<>();
        
        public void enqueue(int item) {
            s1.push(item);
        }

        public int dequeue() {
            if(s1.empty() && s2.empty()) {
                throw new IllegalArgumentException("stack empty");
            }
            else if(s2.empty())
            {
                while(!s1.empty())
                {
                    s2.push(s1.pop());
                }

                return s2.pop();
            }
            else
            {
                return s2.pop();
            }
        }
    }






    // tests

    @Test
    public void basicQueueOperationsTest() {
        final QueueTwoStacks q = new QueueTwoStacks();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        assertEquals("dequeue #1", 1, q.dequeue());
        assertEquals("dequeue #2", 2, q.dequeue());
        q.enqueue(4);
        assertEquals("dequeue #3", 3, q.dequeue());
        assertEquals("dequeue #4", 4, q.dequeue());
    }

    @Test(expected = Exception.class)
    public void exceptionWhenDeuqueFromNewQueueTest() {
        final QueueTwoStacks q = new QueueTwoStacks();
        q.dequeue();
    }

    @Test(expected = Exception.class)
    public void exceptionWhenDeuqueFromEmptyQueueTest() {
        final QueueTwoStacks q = new QueueTwoStacks();
        q.enqueue(1);
        q.enqueue(2);
        q.dequeue();
        q.dequeue();
        q.dequeue();
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