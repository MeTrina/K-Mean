K-Mean
======

A K-Mean algorithm's implement of python

K-Mean算法的Python实现

用法：

首先，新建一个KMean的实例

    kmean = KMean()
    
用户可以通过设置KMean中的distance和center方法自定义两点之间距离和点群中心点的算法

    def distance(p1,p2):
        return float(abs(p1 - p2))
    def center(points):
        return sum(points)/float(len(points))
    kmean.distance = distance
    kmean.center = center

最后运行run
    
    print kmean.run([1,2,33,12,3,4,14,78,7],2,[1,1.004])
    
运行结果：
    $ python demon.py
    [[1, 2, 12, 3, 4, 14, 7], [33, 78]]
