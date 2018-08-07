using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BasicDelegates
{
    // declare the delegate type

    class Program
    {
        // INSERT DELEGATES HERE
        public delegate string MyDelegate(int a, int b);
        static string add(int a, int b) {
            return "" + (a + b);
        }
        static string mult(int a, int b)
        {
            return ""+(a * b);
        }

        static void Main(string[] args)
        {
            MyDelegate f = add;
            Console.WriteLine(" Addition is "+ f(10, 20));
            f = mult;
            Console.WriteLine(" Multiplication is "+ f(10, 20));
            Console.ReadLine();
        }
    }
}
