using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningHashTables
{
    class Program
    {
        static void Main(string[] args)
        {
            Hashtable table = new Hashtable();

            table.Add("title", "MyWebsite");

            var s = (String)table["title"];
            Console.WriteLine(s);
        }
    }
}
