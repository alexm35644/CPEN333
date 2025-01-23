# Part 1: Implementing a simple GUI-based python program for rational numbers
In this lab, you will implement a simple GUI based app that allows us to add, subtract, multiply and divide rational numbers. We represent the rational number type using a python class. The class also has a toString method that returns a string representation of the rational number.

Please note that tkinter is a part of the Python Standard Library, so if you have installed anaconda and using it correctly, there is no need for any additional package installation or such to use tkinter. 

Note that:

A rational number is represented by a numerator and a denominator (both integer) in the form numerator/denominator.
We use a class to define the rational number type. The class uses two fields to store the numerator and the denominator.
The user can enter any valid rational number, but we store a rational number in its lowest form. We say a rational number is in its lowest form if both the numerator and denominator have no common factor other than 1. In our class, the numerator stores the sign of this rational number. 
A rational number cannot have a denominator of 0. We store such a rational number as usual, but we display it as NaN (not a number) when displaying the result of the calculation on our GUI. Note that we are representing undefined also as NaN. The result of a division involving NaN should also be NaN.
The numerator and the denominator must be integers (whole numbers). Otherwise, it is treated as invalid (resulting NaN). 
Every integer d has an equivalent rational number d/1. We store such a rational number as usual, but we display only the integer value when displaying the result of the calculations on our GUI.
Assuming that we have  and , then recall that:

a/b + c/d = (ad + bc)/bd
a/b - c/d = (ad - bc)/bd
a/b * c/d = ac/bd
(a/b) / (c/d) = ad/bc


Consider the following code template. The provided code has two classes: Rational and GUI. 

Use the GUI class as is. It creates the user interface for your program. It is quite unassuming but does the job.
The initializer method for the Rational class is also given to you. Use as is.
You are to complete the Rational class by implementing its remaining methods: add, subtract, multiply, divide and toString. 
All of the add, subtract, multiply and divide methods return a new rational number containing the result. Obviously, they must not mutate any of the operands.
See the code for the comments, and watch this video as a demo for the app first:
https://youtu.be/y-AeZVq4Iv8 Links to an external site.
