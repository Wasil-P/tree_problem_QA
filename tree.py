space = ' '
body = '*'
base = 'TTTTT'


def add_at_symbol(line, odd):
    if odd:
        return '@' + line[:]
    else:
        return line[:] + '@'


def generate_tree(floors: int) -> str:
    tree = []
    width = floors - 1
    quantity_body = 1

    for floor in range(1, floors + 1):
        if floor == 1:
            tree.append(space * width + ' W')
        elif floor == 2:
            tree.append(space * (floors - 1) + ' *')
        else:
            current_line = (body * quantity_body)

            if floor % 2 != 0:
                current_line = add_at_symbol(current_line, odd=True)
            else:
                current_line = add_at_symbol(current_line, odd=False)

            tree.append(space * width + current_line)

        quantity_body += 2
        width -= 1

    tree_bottom = space * (floors - 2) + base
    tree.append(tree_bottom)
    tree.append(tree_bottom)

    return '\n'.join(tree)


def save_tree_to_file(tree: str, file_path: str):
    with open(file_path, 'w') as f:
        f.write(tree)


def main(floors: int, file_path: str):
    tree = generate_tree(floors)
    save_tree_to_file(tree, file_path)


if __name__ == "__main__":
    floors = 6
    file_path = "tree_output.txt"

    main(floors, file_path)