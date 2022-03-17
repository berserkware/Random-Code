using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Calc();
        }

        public static void Calc() {
            
            Console.WriteLine("Welcome to Terminal Calculator");
            Console.WriteLine("Insert Operator");
            string OP = Console.ReadLine();
            Console.WriteLine("Insert first number");
            string One = Console.ReadLine();
            Console.WriteLine("Insert second number");
            string Two = Console.ReadLine();

            if(OP == "+") {
                Console.WriteLine(Int32.Parse(One) + Int32.Parse(Two));
            }
            else if (OP == "-") {
                Console.WriteLine(Int32.Parse(One) - Int32.Parse(Two));
            }
            else if (OP == "*") {
                Console.WriteLine(Int32.Parse(One) * Int32.Parse(Two));
            }
            else if (OP == "/") {
                Console.WriteLine(Int32.Parse(One) / Int32.Parse(Two));
            }
            else {
                Console.WriteLine("Unknown Operator");
                Calc();
            }
        }
    }
}
