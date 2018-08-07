using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ComposableDelegates
{
    // declare the delegate type
    public delegate void MyDelegate(int arg1, int arg2);
    public delegate void MyDelRef(int arg1, ref int arg2);

    class Program
    {
        static void func1(int arg1, int arg2)
        {
            string result = (arg1 + arg2).ToString();
            Console.WriteLine("The number is: " + result);
        }
        static void func2(int arg1, int arg2)
        {
            string result = (arg1 * arg2).ToString();
            Console.WriteLine("The number is: " + result);
        }

        static void funcRef1(int arg1, ref int arg2)
        {
            string result = (arg1 + arg2).ToString();
            arg2 += 10; //changing value of arg2
            Console.WriteLine("The number is: " + result);
        }
        static void funcRef2(int arg1, ref int arg2)
        {
            string result = (arg1 * arg2).ToString();
            arg1 += 10; // won't change anything
            Console.WriteLine("The number is: " + result);
        }
        static void Main(string[] args)
        {
            MyDelegate f1 = func1, f2 = func2;
            MyDelegate both = f1 + f2;
            int a = 20, b = 20;
            Console.WriteLine("Composable call ");
            f1(a, b);
            f2(a, b);
            both(a, b);
            both -= f1;
            both(a, b);

            MyDelRef ref1 = funcRef1, ref2 = funcRef2;
            MyDelRef comb = ref1 + ref2;
            Console.WriteLine("value of b {0}", b);
            ref1(a,ref b);
            ref2(a,ref b);
            Console.WriteLine("value of b {0}", b);
            comb(a,ref b);
            Console.WriteLine("value of b {0}", b);

            Console.WriteLine("\nPress Enter Key to Continue...");
            Console.ReadLine();
        }
    }
}
