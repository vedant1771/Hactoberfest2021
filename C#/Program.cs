// Adding Strings

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AddString
{
    class Program
    {
        static void Main(string[] args)
        {
            string phrase = "United " + "International " + "University";
            Console.WriteLine(phrase);

            Console.WriteLine(phrase.Length); // Finding the length of the string

            Console.WriteLine(phrase.ToUpper()); // Print the whole string in uppercase

            Console.WriteLine(phrase.ToLower()); // Print the whole string in lowercase

            Console.WriteLine(phrase.Contains("International")); // It will search for the word "International" in the string and will return True/False
            Console.WriteLine(phrase.Contains("Internationals"));

            Console.WriteLine(phrase[5]); // it will print the character of index 5 of the whole string

            Console.WriteLine(phrase.IndexOf("International")); // it will tell in which index positon "International" is in the string
            Console.WriteLine(phrase.IndexOf("o")); // it will tell in which index positon first "o" is in the string
            Console.WriteLine(phrase.IndexOf("21")); // it will provide -1 as 21 isn't in the string

            Console.WriteLine(phrase.Substring(7)); // it will grab the letter of index 7 and will print the entire rest of the part of the string after the character of index 7

            Console.WriteLine(phrase.Substring(7, 3));  // it will grab the letter of index 7 and will print the rest of 3 index values after the character of index 7

            Console.ReadLine();
        }
    }
}