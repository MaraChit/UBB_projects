using LAB_4.Implementation;
using System;
using System.Collections.Generic;

namespace LAB_4
{
    class Program
    {
        private static readonly List<string> Pages = new List<string> {

            "www.cs.ubbcluj.ro/~forest/pdav",

            "www.cs.ubbcluj.ro/~rares/course/vr",

            "math.ubbcluj.ro/~cpblaga/astronomie.html",
        };

        public static void Main(string[] args)
        {
            //EventDriven.Run(Pages);
            //TaskDriven.Run(Pages);
            AsyncTaskDriven.Run(Pages);
        }
    }
}
