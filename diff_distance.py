from typing import Callable, List
import math
#DO NOT MAKE UNNECESSARY CHANGES
class DistanceFuncs:
    def calc_distance( self, point_a: List[float], point_b: List[float], dist_func: Callable)->float:
        """ Calculates distance between two points using the passed dist_func """
        return dist_func(point_a, point_b)
    
    @staticmethod
    def euclidean(point_a: List[float], point_b: List[float])->float:
        """
        Calculates Euclidean Distance between two points Example:
        >>> DistanceFuncs.euclidean([1,1],[1,1])
        0.0
        """
        distance = 0
        for pts1, pts2 in zip(point_a, point_b):
            distance += (pts1-pts2)**2
        
        distance = distance**0.5
        return distance

    @staticmethod
    def manhattan_distance(point_a: List[float], point_b: List[float])->float: 
        """Compute the manhattan_distance between two points""" 
        if len(point_a) != len(point_b):
            raise ValueError

        distance = 0
        for pts1, pts2 in zip(point_a, point_b):
            distance += abs(pts1 - pts2)
        return distance

    @staticmethod
    def jaccard_distance(point_a: List[float], point_b: List[float])->float: 
        """Compute the jaccard_distance between two points""" 
        size_a, size_b = len(point_a), len(point_b)
        intersect = set(point_a) & set(point_b)
        size_intersect = len(intersect)
        jaccardDistance = 1 - size_intersect / (size_a + size_b - size_intersect)
        return jaccardDistance

def main():
    """Demonstrate the usage of DistanceFuncs """
    point_a = [1,2]
    point_b = [2,5]
    print(f"Euclidean distance between {point_a} and {point_b} ==> ", DistanceFuncs.euclidean(point_a, point_b))
    print(f"Manhattan distance between {point_a} and {point_b} ==> ", DistanceFuncs.manhattan_distance(point_a, point_b))
    print(f"Jaccard distance between {point_a} and {point_b} ==> ", DistanceFuncs.jaccard_distance(point_a, point_b))
pass

if __name__ == "__main__":
    main()
