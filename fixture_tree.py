import pytest

@pytest.fixture
def tree_base():
    return "TTTTT"

@pytest.fixture
def file_path():
    return "test_tree.txt"

@pytest.fixture
def expected_tree():
    def _generate_expected_tree(floors):
        if floors == 2:
            return (
                "  W\n"
                "  *\n"
                "TTTTT\n"  
                "TTTTT"
            )
        elif floors == 3:
            return (
                "   W\n"  
                "   *\n"  
                "@*****\n"  
                " TTTTT\n"  
                " TTTTT"
            )
        elif floors == 5:
            return (
                "     W\n"  
                "     *\n"  
                "  @*****\n"  
                " *******@\n"  
                "@*********\n"  
                "   TTTTT\n"  
                "   TTTTT"
            )
        return None

    return _generate_expected_tree