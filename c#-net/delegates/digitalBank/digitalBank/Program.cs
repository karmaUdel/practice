using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace digitalBank
{
    public delegate void valueChangedHandler();
    class Program
    {
        static void Main(string[] args)
        {
            PiggyBank bank= new PiggyBank();
            bank.valueChanged += bank.balanceUpdate;
            bank.valueChanged += bank.balanceWatch;
            int amount = 0;
            string option = "";
            while (option!="exit") {
                Console.WriteLine("How much amount to deposit");
                option = Console.ReadLine();
                amount = 0;
                if (option != "exit") {
                    amount = Convert.ToInt32(option);
                    Console.WriteLine(bank.balance);
                    bank.Balance += amount;
                }
            }
        }
    }
    public class PiggyBank
    {

        public int balance;
        public event valueChangedHandler valueChanged;
        public int Balance {
            get {
                return balance;
            }
            set {
             
                balance = value;
                Console.WriteLine(value);
                valueChanged();        
            }
        } 

        public void balanceUpdate()
        {
            Console.WriteLine("Balance is {0}", balance);
        }
        public void balanceWatch()
        {
            if (balance > 500)
                Console.WriteLine("You reached your savings goal! You have {0}", balance);
        }
    }
}
