using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Zad_02___Inheritance;

namespace Zad_02___Inheritance
{
public class Complex {
	private double _re, _im;

	public Complex(double inRe) { _re = inRe; _im = 0.0; }
}

public class Base {
    public void g(int a) { Console.WriteLine("Base::g(int)"); }

	public virtual void f( int a ) { Console.WriteLine("Base::f(int)"); }
	public virtual void f( double a) { Console.WriteLine("Base::f(double)"); }
};

    public class Derived : Base
    {
        public void g(double a) { Console.WriteLine("Derived::g(double)"); }

//        public override void f(double a) { Console.WriteLine("Derived::f(double)"); }
        public void f(Complex a) { Console.WriteLine("Derived::f(Complex)"); }
    };

	public class Program
	{
		static void Main(string[] args)
		{
			Derived	d = new Derived();
			Base 	pb = new Derived();

		    d.f(1);
			d.f(1.0);		
            d.g(1);
		    d.g(1.0);

            Console.WriteLine();

		    pb.f(1);
			pb.f(1.0);		
            pb.g(1);
//            pb.g(1.0);
		}
	}
}
