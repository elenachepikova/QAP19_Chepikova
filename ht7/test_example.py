from pytest import mark

class TestHT7T1:

    @mark.len
    def test_len1(self):
        assert len(['apple','banana','tea']) == 3

    @mark.sum
    def test_sum1(self):
        assert sum([1,2,3]) == 6

    @mark.sorted
    def test_sorted1(self):
        sl1 = sorted([5,8,1])
        assert sl1 == [1,5,8]

class TestHT7T2:

    @mark.len
    def test_len2(self,generate_numbers):
        assert len(generate_numbers) == 10

    @mark.sum
    def test_sum2(self,generate_numbers):
        assert sum(generate_numbers) > 0

    @mark.sorted
    def test_sorted2(self,generate_numbers):
        sl2 = sorted(generate_numbers)
        for i in sl2:
            assert i <= i + 1

class TestHT7T3:

    @mark.skip
    def test_even(self,generate_numbers):
        for i in generate_numbers:
            assert i % 2 == 0

    @mark.xfail
    def test_odd(self,generate_numbers):
        for i in generate_numbers:
            assert i % 2 != 0