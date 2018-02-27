import os
from glob import glob
import tempfile
import shutil
from unittest import TestCase, main


import md_autogen
from md_autogen import MarkdownAPIGenerator, to_md_file


class TestMarkdownAPIGenerator(TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_docs_generation(self):
        modules = [
            md_autogen,
        ]
        output_folder = os.path.join(self.tempdir, "generated")
        os.mkdir(output_folder)
        md_gen = MarkdownAPIGenerator("md_autogen", "https://github.com/raghakot/markdown-apidocs")
        for m in modules:
            md_string = md_gen.module2md(m)
            to_md_file(md_string, m.__name__, output_folder)

        self.assertTrue(output_folder)
        self.assertEqual(1, len(glob(os.path.join(output_folder, "*.md"))))


if __name__ == "__main__":
    main()
