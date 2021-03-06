import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from spring.cloud.stream import components

class TestTypes(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, os.path.abspath('..'))

    def test_create_sink(self):
        sink = components.Sink()
        self.assertEqual('input',sink.name)

    def test_create_source(self):
        source = components.Source()
        self.assertEqual('output',source.name)


    def test_create_processor(self):
        processor = components.Processor()
        self.assertEqual(components.Sink, processor.input.__class__)
        self.assertEqual('input', processor.input.name)

        self.assertEqual(components.Source, processor.output.__class__)
        self.assertEqual('output', processor.output.name)

if __name__ == '__main__':
    unittest.main()