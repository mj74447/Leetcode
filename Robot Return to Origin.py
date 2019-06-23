import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        How counter works
        import collections

        print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
        print collections.Counter({'a':2, 'b':3, 'c':1})
        print collections.Counter(a=2, b=3, c=1)
        $ python collections_counter_init.py

        Counter({'b': 3, 'a': 2, 'c': 1})
        Counter({'b': 3, 'a': 2, 'c': 1})
        Counter({'b': 3, 'a': 2, 'c': 1})
        """
        X=collections.Counter(moves)
        return X["U"]==X["D"] and X["L"]==X["R"]
