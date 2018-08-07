using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningProperties
{
    class Player
    {
        public bool isAlive {
            get {
                return health > 0;
            }
        }
        int health = 100;

        public bool bored { get; internal set; } = true;
        public void Hit()
        {
            Random r = new Random();
            health -= r.Next(5, 50);
            if (!isAlive)
            {
                bored = false;
            }
        }

    }
    class Program
    {
        static void Main(string[] args)
        {
            Player player = new Player();
            for (int i = 0; i < 20 && player.bored ; i++)
            {
                //player.bored = false;
                player.Hit();
                Console.WriteLine("Is player alive: " + player.isAlive);
            }
        }
    }
}
