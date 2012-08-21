#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from algorithm.kmean import KMean

def main():
    kmean = KMean()
    def distance(p1,p2):
        return float(abs(p1 - p2))
    def center(points):
        return sum(points)/float(len(points))
    kmean.distance = distance
    kmean.center = center
    print kmean.run([1,2,33,12,3,4,14,78,7],2,[1,1.004])

if __name__ == "__main__":
    main()