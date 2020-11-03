# EPAi_assignment13

In this assignment we have defined a ploygon class as well as a custom sequence type using the same class.
We then proceed to make seperate modules of them both.


Polygon class:

Initializer: 
number of edges/vertices
circumradius

Properties:
1. edges
2. radius
3. interior angle
4. edge length
5. apothem
6. area
7. perimeter

Functionalities:
1. __repr__ function
2. implements equality (==) based on # vertices and circumradius (__eq__)
3. implements > based on number of vertices only (__gt__)



Custom Polygon Sequence type: 

Initializer:
1. number of vertices for largest polygon in the sequence
2. common circumradius for all polygons

Properties: 
1. max efficiency polygon: returns the Polygon with the highest area: perimeter ratio

Functionalities:
1. __getitem__ function (for indexing and iterating)
2. __len__ function
3. __repr__ function
