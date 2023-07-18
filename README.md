# PCA-data-visualizer
5-dimensional static data visualization using PCA for reduction and xyRGB for display

This program is a demo for a 5-D prototype scatterplot data visualizer

It reads in an excel file to get a table of multidimensional points, decomposes to 5 principle dimensions using PCA, normalizes to [0,255] for each dimension and displays the points by setting those 5 values as the x, y, R, G, B values respectively

As this is a demo, I did not add many safeguards. The table must be fully populated (no empty values), must be 5+ dimensional, and must be excel (comma sepatated, 1 point per line, no headers/footers)

Please enjoy!
