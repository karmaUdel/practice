using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LearningBitArray
{
    class Program
    {
        static void Main(string[] args)
        {
            bool[] preload = new bool[3] { true, false, true };


            BitArray enemyGrid = new BitArray(preload);


            //enemyGrid[0] = false;
            //enemyGrid[1] = true;
            //enemyGrid.Set(2, false);

            foreach (var item in enemyGrid)
            {
                Console.WriteLine(item);
            }

        }
    }
}
