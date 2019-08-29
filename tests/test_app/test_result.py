from unittest import TestCase, main

from cogent3.app.result import generic_result


__author__ = "Gavin Huttley"
__copyright__ = "Copyright 2007-2019, The Cogent Project"
__credits__ = ["Gavin Huttley"]
__license__ = "BSD-3"
__version__ = "2019.8.30a"
__maintainer__ = "Gavin Huttley"
__email__ = "Gavin.Huttley@anu.edu.au"
__status__ = "Alpha"


class TestGenericResult(TestCase):
    def test_deserialised_values(self):
        """correctly deserialises values"""
        from cogent3 import DNA

        data = {"type": "cogent3.core.moltype.MolType", "moltype": "dna"}
        result = generic_result(source="blah.json")
        result["key"] = data
        result.deserialised_values()
        got = result["key"]
        self.assertEqual(got, DNA)
        # if we have a type value without "cogent3", leaves as is
        data = {"type": "core.moltype.MolType", "moltype": "dna"}
        result = generic_result(source="blah.json")
        result["key"] = data
        result.deserialised_values()
        got = result["key"]
        self.assertEqual(got, data)
        # or if no "type" entry, leaves as is
        data = {"moltype": "dna"}
        result = generic_result(source="blah.json")
        result["key"] = data
        result.deserialised_values()
        got = result["key"]
        self.assertEqual(got, data)


if __name__ == "__main__":
    main()
