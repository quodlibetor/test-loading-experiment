from nose.plugins.attrib import attr

class TestCase(object):
    def test_something(self):
        pass

    @attr("unsafe")
    def test_other(self):
        pass
