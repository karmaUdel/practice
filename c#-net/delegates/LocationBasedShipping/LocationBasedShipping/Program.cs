using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LocationBasedShipping
{
    class Program
    {
        public delegate string Mydelegate(int price, int rate);
        public static string calculate(int price,int rate) {
            return "The Shipping fees are " + (price * rate / 100);
        }
        static void Main(string[] args)
        {
            string zone = "";
            int price = 0;
            Mydelegate f = calculate;
            while (zone!="exit") {
                Console.WriteLine("Enter Zone");
                zone = Console.ReadLine();
                if(zone == "exit"){
                    break;
                }
                Console.WriteLine("Enter Price");
                price = Convert.ToInt32(Console.ReadLine());

                switch (zone) {
                    case "zone1": Console.WriteLine(f(price, 25));
                        continue;
                    case "zone2":
                        Console.WriteLine(f(price, 25+12));
                        continue;
                    case "zone3":
                        Console.WriteLine(f(price, 8));
                        continue;
                    case "zone4":
                        Console.WriteLine(f(price, 25 + 4));
                        continue;
                    case "exit": continue;
                    default: Console.WriteLine("Invalid Zone ");
                        continue;
                }
            }
        }
    }
}
