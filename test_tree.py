import os

from tree import generate_tree, save_tree_to_file
from fixture_tree import expected_tree, tree_base, file_path


class TestTree:

    def test_tree_base(self, tree_base):
        result = generate_tree(1)
        lines = result.split('\n')

        assert lines[-1].strip() == tree_base, "The base #1 is incorrect"
        assert lines[-2].strip() == tree_base, "The base #2 is incorrect"

    def test_tree_with_2_floors(self, expected_tree):
        expected_result = expected_tree(2)
        result = generate_tree(2)
        assert result == expected_result, f"Test failed for 1 floors. Got:\n{result}"

    def test_tree_with_3_floors(self, expected_tree):
        expected_result = expected_tree(3)
        result = generate_tree(3)
        assert result == expected_result, f"Test failed for 3 floors. Got:\n{result}"

    def test_tree_with_5_floors(self, expected_tree):
        expected_result = expected_tree(5)
        result = generate_tree(5)
        assert result == expected_result, f"Test failed for 5 floors. Got:\n{result}"

    def test_save_tree_to_file(self, file_path):
        tree = generate_tree(3)
        save_tree_to_file(tree, file_path)

        assert os.path.exists(file_path), "File was not created"

        with open(file_path, 'r') as f:
            content = f.read()
            assert content == tree, "File content is incorrect"

        os.remove(file_path)

