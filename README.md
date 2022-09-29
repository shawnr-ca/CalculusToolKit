# CalculusToolKit
A simple visual toolkit useful for those learning Calculus. Currently, toolkit includes visual Riemman Sum Calculator and Function Arc Length Approximation Calculator. They are set to solve for the function f(x) = e^(sin(x)), but this can be easily adjusted. For both Rectangular Integration/Riemann Sums and Arc Length Calculation, the user is prompted to select upper and lower bounds. In the case of Riemann Sums, user inputs the number of rectangles for their calculation and for Arc Lengths, the number of line segments. 

Both Riemann Sums and Arc Length approximation functions according to similar principles. The number of rectangles/line segments are selected and this divides the bounds into equal intervals. For Riemann Sums, these intervals are the widths of the rectangles and the heights are the values of the function at that interval (upper bound). In the end, all the rectngle areas are added together. For Arc Lengths, line segments connecting the intervals are added together, with their lengths computed using the pythagorean theorem. 

Also included are scripts that plot the accuracy of the approximations as the number of line segments/rectangles are increased.

Dependencies: numpy, matplotlib

Examples:

![RiemannSums](https://user-images.githubusercontent.com/113395566/192918849-cf8dffb1-74a0-4915-a6d6-3a8042c1f4cc.png)
![ArcLength1](https://user-images.githubusercontent.com/113395566/192918867-b874a88b-b960-48ed-99e8-28781d5c1b69.png)
![ArcLength2](https://user-images.githubusercontent.com/113395566/192918874-3d00882b-bf0f-420a-aee6-479dea47808c.png)
![RectangularIntegrationAccu](https://user-images.githubusercontent.com/113395566/192918888-aceb57d5-c5c1-4050-ade6-5fff7f2fb431.png)
![ArcLengthAccu](https://user-images.githubusercontent.com/113395566/192918902-6a94544c-2319-4758-97ca-72d5d3af8f9b.png)
