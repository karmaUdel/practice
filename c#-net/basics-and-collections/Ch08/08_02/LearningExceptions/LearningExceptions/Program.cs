using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningExceptions
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string s = null;
                var l = s.Length;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
        }
    }
}
