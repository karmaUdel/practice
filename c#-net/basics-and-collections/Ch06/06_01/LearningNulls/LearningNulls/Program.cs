using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningNulls
{
    class Program
    {
        static void Main(string[] args)
        {
            int? s = null; //"hello";
            int s2 = s ?? 2;

            Console.WriteLine(s2);
        }
    }
}
