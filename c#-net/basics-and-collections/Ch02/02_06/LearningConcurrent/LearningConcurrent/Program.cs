using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace LearningConcurrent
{
    class Program
    {
        static ConcurrentDictionary<int, int> items = new ConcurrentDictionary<int, int>();

        static void Main(string[] args)
        {
            Thread thread1 = new Thread(new ThreadStart(AddItem));
            Thread thread2 = new Thread(new ThreadStart(AddItem));

            thread1.Start();
            thread2.Start();
        }

        static void AddItem()
        {
            items.TryAdd(1, 2);
            Console.WriteLine(items.Count);
        }
    }
}
