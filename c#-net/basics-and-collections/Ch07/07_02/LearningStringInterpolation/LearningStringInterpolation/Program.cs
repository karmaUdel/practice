using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningStringInterpolation
{
    class Program
    {
        static void Main(string[] args)
        {
            var point = new { x = 1, y = 2 };

            Console.WriteLine("x " + point.x + " y " + point.y);

            Console.WriteLine("x {0} y {1}", point.x, point.y);
        }
    }
}
