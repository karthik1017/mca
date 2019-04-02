public class Row
{
    public static void main(String[] args)
    {
        int result1 = sum(1, 2);
        int result2 = sum(1, 2, 3);
        int result3 = sum(1, 2, 4, 5, 6, 7);

        System.out.println(result1 + "\n" + result2 + "\n" + result3);
        
    }

    static int sum(int... args)
    {
        int ret = 0;
        float avg=0;
        int count = 0;
        if (args != null)
        {
            for (int val : args)
            {
                ret += val;
                count = count + 1;
                
            }

        }
        avg=ret/count;
        System.out.println("Average: "+ avg);
        return ret;
    }
}