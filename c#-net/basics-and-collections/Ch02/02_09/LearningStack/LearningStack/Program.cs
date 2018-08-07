using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningStack
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<String> pancakes = new Stack<string>();

            pancakes.Push("first pancake made");
            pancakes.Push("second pancake made");
            pancakes.Push("last pancake made");

            //foreach (var pancake in pancakes)
            //{
            //    Console.WriteLine(pancake);
            //}

            Console.WriteLine(pancakes.Pop());
            Console.WriteLine(pancakes.Peek());
            Console.WriteLine(pancakes.Peek());
            Console.ReadLine();


        }
    }
}
