using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningLists
{
    class Program
    {
        static void Main(string[] args)
        {
            List<String> customers = new List<string>();

            customers.Add("Kim");
            customers.Add("John");
            customers.Add("Tim");

            Console.WriteLine(customers.Count);

            foreach (var customer in customers)
            {
                Console.WriteLine(customer);
            }

            Console.WriteLine(customers[1]);
        }
    }
}
