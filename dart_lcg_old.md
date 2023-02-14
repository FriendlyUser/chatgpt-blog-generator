---
tags: ['dart']
title: Web Scrapping Super Bowl Winners
description: Web scrapping of the espn page for super bowl winners
pubDate: Fri, 21 March 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/test.png
---
There are several reasons why one might choose to use Dart over Java:

1. Syntax: Dart's syntax is often considered more concise and easier to read than Java's.
2. Performance: Dart's virtual machine is optimized for fast start-up times and efficient just-in-time (JIT) compilation, which can make it faster than Java in some scenarios.
3. Cross-platform development: Dart is often used for cross-platform development, meaning that developers can write code once and deploy it on multiple platforms, such as web, mobile, and desktop.
4. Flutter framework: Dart is the primary language used for the Flutter framework, which is a popular choice for building high-performance, cross-platform mobile and web applications.
5. Modern language features: Dart includes modern language features such as asynchronous programming, extension methods, and null safety, which can make it easier and more efficient to write code.

That being said, Java is a mature language with a large developer community, and there are many scenarios where Java may still be the better choice depending on the specific requirements of the project.


```dart 
 // Class representation of a rational number. This rational number will always 
// be simplified as far as possible, will always indicate sign on the numerator
// and will always represent 0 as 0/1. For example 2/-8 will be represented as 
// -1/4 and 0/-128 will be represented as 0/1.
class Rational {
  // rational numerator, should be integer
  int _num;
  // rational denominator should be integer
  int _denom;

  int get numerator {return _num;}
  int get denominator {return _denom;}
  // creates a simplified rational number
  Rational(this._num, this._denom) {
    simplify();
  }
  Rational operator +(Rational other) {
    // int lcm_rl = std::lcm(this.numerator, other.denominator);
    int lcm_rl = _lcm(this.denominator, other.denominator);
    // // to compute multiple factor switch numbers around
    int left_fact = lcm_rl ~/ this.denominator;
    int right_fact = lcm_rl ~/ other.denominator;
    return Rational((this.numerator * left_fact) + (other.numerator * right_fact), lcm_rl);
  }
  Rational operator -(Rational other) {
    // int lcm_rl = std::lcm(this.numerator, other.denominator);
    int lcm_rl = _lcm(this.denominator, other.denominator);
    // // to compute multiple factor switch numbers around
    int left_fact = lcm_rl ~/ this.denominator;
    int right_fact = lcm_rl ~/ other.denominator;
    return Rational((this.numerator * left_fact) - (other.numerator * right_fact), lcm_rl);
  }
  Rational operator *(Rational other) {
    return Rational(this.numerator * other.numerator, this.denominator * other.denominator);
  }
  Rational operator /(Rational other) {
    return Rational(this.numerator * other.denominator, this.denominator * other.numerator);
  }

  // comparsion operators
  @override
  bool operator ==(Rational other) {
     return (this._num == other._num && this._denom == other._denom);
  }
  bool operator <(Rational other) {
    // compare numerators
    int lcm_com = _lcm(this._denom, other._denom);
    int lcm_denom = lcm_com ~/ this._denom;
    int lcm_rat_denom = lcm_com ~/ other._denom;
    // multiple numerators
    return ( (_num * lcm_denom) < (other._num * lcm_rat_denom));
  }
  // Inequality comparsion with [other]
  bool operator >(Rational other) {
    // compare numerators
    int lcm_com = _lcm(this._denom, other._denom);
    int lcm_denom = lcm_com ~/ this._denom;
    int lcm_rat_denom = lcm_com ~/ other._denom;
    // multiple numerators
    return ( (_num * lcm_denom) > (other._num * lcm_rat_denom));
  }

  void _treat_divide_by_zero() {
    if (_denom == 0) {
        _num = power(2,63) - 1;
        _denom = 1;
    }
  }
  // simplify function
  void simplify() {
    // Always represent 0 as 0/1
    _treat_divide_by_zero();

      // Divide by greatest common divisor, 
      int gcdValue = _gcd(_num, _denom);
      // gcd should never be 0 at this point, but if it is don't divide by zero
      if (gcdValue != 0) {
          _num ~/= gcdValue;
          _denom ~/= gcdValue;
      }

    // Indicate sign on numerator only
    if (_denom < 0) {
      _num = -_num;
      _denom = -_denom;
    }
  }
  // should be a utility function, but whatever
  int power(int x, int y) {
    int power = 1;
    for (int i = 0; i < y; i++) {
      power *= x;
    }
  
    return power;
  }
  // least common multiple
  int _lcm(int a, int b) => (a * b) ~/ _gcd(a, b);
  int _gcd(int a,int b)
  {
    if(b==0)
      return a;
    if(b!=0)
      return _gcd(b,a%b);
    return 0;
  }
  // Returns the integer value for a rational number
  int truncate()
  {   
      // could use integer division instead
      // find wholest number that can be divided by, subtract remainder
      int remain = _num % _denom;
      int whole_num = (_num - remain) ~/ _denom;
      return whole_num;
  }
  bool is_integer() {
    return (_num == 0 || _denom == 1);
  }
  @override
  // print the rational number as numerator/denominator,
  // example 3/5
  String toString() {
    return "${_num}/${_denom}";
  }
}
 
 ```

There are several reasons why one might choose to use Dart over Java:

1. Syntax: Dart's syntax is often considered more concise and easier to read than Java's.
2. Performance: Dart's virtual machine is optimized for fast start-up times and efficient just-in-time (JIT) compilation, which can make it faster than Java in some scenarios.
3. Cross-platform development: Dart is often used for cross-platform development, meaning that developers can write code once and deploy it on multiple platforms, such as web, mobile, and desktop.
4. Flutter framework: Dart is the primary language used for the Flutter framework, which is a popular choice for building high-performance, cross-platform mobile and web applications.
5. Modern language features: Dart includes modern language features such as asynchronous programming, extension methods, and null safety, which can make it easier and more efficient to write code.

That being said, Java is a mature language with a large developer community, and there are many scenarios where Java may still be the better choice depending on the specific requirements of the project.


```dart 
 import './lcg_interface.dart';

/// The event handler responsible for updating the badge in the UI.
class LCG implements LCG_Interface { 
  // lcg multiplier
  final int _a;
  // lcg increment
  final int _c;
  // lcg modulus
  final int _m;
  int _xi;
  // seed 
  int seedValue;
  int get multiplier {return _a;}
  int get increment {return _c;}
  int get modulus {return _m;}
  int get seed {return seedValue;}
  //setters
  void set seed(int newSeed) {seedValue = newSeed;}
  // constructor
  LCG(this._a,this._c,this._m, this.seedValue) {
    if ( _c % _m == 0 && seedValue % _m == 0) {
        _xi = 1;
    } else {
        _xi = seedValue;
    }
  }
  int currValue() {
    return _xi;
  }
  int nextNum() {
    _xi = _next();
    return _xi;
  }
  void discard(int n) {
    for (int i = 0; i < n; i++) {
      _xi = nextNum();
      // cout << "Next Iterator Value is: " << xi;
    }
  }
  int min() {
    if( _c == 0) return 1;
    return 0;
  }
  int max() {
    return _m-1;
  }
  int _next() {
    return (_a * _xi +_c) % _m;
  }
  @override
  bool operator==(LCG other) => (other.increment == this.increment && other.modulus == this.modulus && other.multiplier == this.multiplier);
}
 
 ```

There are several reasons why one might choose to use Dart over Java:

1. Syntax: Dart's syntax is often considered more concise and easier to read than Java's.
2. Performance: Dart's virtual machine is optimized for fast start-up times and efficient just-in-time (JIT) compilation, which can make it faster than Java in some scenarios.
3. Cross-platform development: Dart is often used for cross-platform development, meaning that developers can write code once and deploy it on multiple platforms, such as web, mobile, and desktop.
4. Flutter framework: Dart is the primary language used for the Flutter framework, which is a popular choice for building high-performance, cross-platform mobile and web applications.
5. Modern language features: Dart includes modern language features such as asynchronous programming, extension methods, and null safety, which can make it easier and more efficient to write code.

That being said, Java is a mature language with a large developer community, and there are many scenarios where Java may still be the better choice depending on the specific requirements of the project.


