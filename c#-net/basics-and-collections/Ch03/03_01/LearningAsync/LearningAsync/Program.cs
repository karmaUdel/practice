using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace LearningAsync
{
    class Program
    {
        static int i = 0;
        static void Main(string[] args)
        {
            Console.WriteLine("Downloading file");
            Download(inBetween);
            Console.ReadLine();
        }
        static void inBetween() {
            Console.WriteLine("called" + ++i);
        }

        static void Download(Action callback)
        {
            Task.Run(() => {
                callback();
                Thread.Sleep(3000);
                callback();
                Console.WriteLine("Download Complete");
                callback();
            });

        }
    }
}
