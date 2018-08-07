using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningHashSet
{
    class Program
    {
        static void Main(string[] args)
        {
            var myHash = new HashSet<String>();

            myHash.Add("hello");
            myHash.Add("hello");

            String[] s = new String[] { "hello" };

            Console.WriteLine(myHash.Count);
            Console.WriteLine(myHash.Overlaps(s));
        }
    }
}
