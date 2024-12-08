package learn.j.dsa;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assume.assumeTrue;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        assertTrue( true );
        assertTrue("this is the msg for assertTrue", false);
        
        assertFalse(false);
        assertFalse("this is the msg for assertFalse", false);
        
        assertArrayEquals(new Object[] {}, null);
       
        assertEquals(0, 0);
        assertNotEquals(0, 0);
        
        assertNull(null);
        assertNull("this is the msg for assertNull",getClass());
        
        assertNotNull(getClass());
        assertNotNull("this is the msg for assertNotNull",getClass());
        
        assumeTrue(null, false);
        
        
    }
}
