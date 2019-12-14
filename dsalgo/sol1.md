# SOL 1

#### [<--Back to Home](../Readme.md)

### Week 0 :

## Track 1 - Introduction  

# Analysis of Algorithm  

* How do we find which algorithm is better ? - Test Cases - Asymptotic Analysis
* Best Case(Omega Notation) , Average Case(Omega Notation), Worst Case (Big-Oh Notation)
* Shortcomings of Asymptotic analysis : Does not consider the difference caused by constants ie n^2 << n+c (where C might be large)
* [Analysis of Loops](https://telegra.ph/Analysis-of-Loops-06-11)

## Track 2 - Analysis of Recursion

*  General Method : Recursion Tree Method
*  Requires Learning : Formula,Master Theorem 

## Track 3 - Time Complexity of a Computer Program 

* Cost of a statement, Number of times 
* O(1) < O(logn) <O(n) <O(nlogn) < O(n^c) < O(n!)


# SOL 2

## Track 1 - Mathematics

* Finding Number of Digits in a Number 
*  Arithmetic and Geometric Progression  
* Quadratic Equation  
* Mean and Median  
* Prime Numbers
* LCM and HCF 
* Factorials 
* Permutation and Combination Basics
* Modular Arithmetic 

Problems to Solve  
 - Calculating the Absolute value without using inbuilt function [Method 1](https://www.geeksforgeeks.org/compute-the-integer-absolute-value-abs-without-branching/)

 - Convert Celsius To Fahrenheit [Source](https://www.geeksforgeeks.org/program-celsius-fahrenheit-conversion/)

 - Calculating the roots of the Quadratic equation [Source](https://www.geeksforgeeks.org/program-to-find-the-roots-of-quadratic-equation/)

 - Factorial of Number Recursion[Source](https://www.geeksforgeeks.org/program-for-factorial-of-a-number/) 

 - Digits in  Factorial of a Big Number [Source](https://www.geeksforgeeks.org/count-digits-factorial-set-1/)

 - Numbers with Exactly 3 Divisors [Source](https://www.geeksforgeeks.org/numbers-exactly-3-divisors/)

 -  Mean and Median [Source](https://www.geeksforgeeks.org/program-for-mean-and-median-of-an-unsorted-array/)

 -  Print Digits up to N without loop [Source](https://www.geeksforgeeks.org/how-will-you-print-numbers-from-1-to-200-without-using-loop/)

 - Sum of N Digits in a number [Source](https://www.geeksforgeeks.org/program-for-sum-of-the-digits-of-a-given-number/)

 - Digital Roots [Source](https://www.geeksforgeeks.org/digital-rootrepeated-digital-sum-given-integer/)

 - Fibonacci Using Recursion [Source](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/) 

   ```c++
   long long fibonacci(int n)
   {
       if(n<=1)
           return n;
       else 
           return fibonacci(n-1)+fibonacci(n-2);
       }
   ```

   

- Modulo of 10^9+7 the Answer

  ```
  int sumUnderModulo(long long a,long long b)
  {
      int M=1000000007;
      //your code here
      return ((a%M)+(b%M))%M;
  }
  ```

- Find the First Bit Set [Source](https://www.geeksforgeeks.org/position-of-rightmost-set-bit/)

  

## Track 3 - Recursion

- Tower of Hanoi [Source](https://practice.geeksforgeeks.org/problems/tower-of-hanoi/0) 

```
void towerofhanoi(int n,char s,char d ,char aux)
{
	if(n==1)
	{
		cout<<"Move Disk 1 from rod"<<s<< " to rod "<< d <<endl;
		return;
	}
	towerofhanoi(n-1,s,aux,d);
	cout<<"Move Disk "<<n<<" from rod"<< s<< "to rod" << d <<endl;
	towerofhanoi(n-1, aux, d, s);
}
```

- Josephus Problem [Source](https://practice.geeksforgeeks.org/problems/josephus-problem/1) ......[Medium](https://medium.com/@rrfd/explaining-the-josephus-algorithm-11d0c02e7212)

  ```
  int josephus(int n, int k)
  {
  if(n==1)
  return 1;
  return (josephus(n-1,k)+k-1)%n +1;
  }
  ```

- Power using Recursion  [Source](https://www.sanfoundry.com/c-program-power-number-using-recursion/)

- Power Set in Lexicographic order [Source](https://www.geeksforgeeks.org/powet-set-lexicographic-order/)

  ``` 
  #include<bits/stdc++.h> add all the libraries to a c file
  ```









## Track 8 - Sorting

* Bubble Sort Algorithm 
  
  
  

  

  
  
  
  
  
  
  
  