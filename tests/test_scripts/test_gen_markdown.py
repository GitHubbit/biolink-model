import os
import unittest


from metamodel.generators.markdowngen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click

update_test_files = True


class GraphvizTestCase(ClickTestCase):
    testdir = "genmarkdown"
    click_ep = cli
    prog_name = "gen-markdown"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        outdir = os.path.join(self.testdir_path, 'meta')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.metamodel_file + f" -d {outdir}", update_test_file=update_test_files)
        # self.do_test(self.metamodel_file + f" -f svg -d {outdir} -o all", update_test_file=update_test_files)
        # self.do_test(self.metamodel_file + f' -f xyz -d {outdir} -o all', update_test_file=update_test_files,
        #              error=click.exceptions.BadParameter)
        # outdir = os.path.join(self.testdir_path, 'meta2')
        # self.do_test(self.metamodel_file + f" -d {outdir} -c definition", update_test_file=update_test_files)
        # self.do_test([self.metamodel_file, "-d", outdir, "-c", "class definition", "-c", "element"],
        #              update_test_file=update_test_files)
        # self.do_test([self.metamodel_file, "-c", "nada"], error=ValueError)
        # self.do_test(self.metamodel_file + f" -o {os.path.join(outdir, 'all2')}", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        outdir = os.path.join(self.testdir_path, 'biolink-model')
        os.makedirs(outdir, exist_ok=True)
        self.do_test(self.biolink_file + f" -d {outdir}", update_test_file=update_test_files)
        # self.do_test(self.biolink_file + f" -f svg -d {outdir} -o all", update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
