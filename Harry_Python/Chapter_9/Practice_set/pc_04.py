import os


def generate_table(n: int) -> str:
    """Generate multiplication table for n and save to a file.
    
    Returns the file path where the table was saved.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")
    if n < 1:
        raise ValueError(f"n must be a positive integer, got {n}")

    table_lines = [f"{n} X {i} = {n * i}" for i in range(1, 11)]
    table = "\n".join(table_lines) + "\n"

    output_dir = "table"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"table_{n}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(table)

    return file_path


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        path = generate_table(user_input)
        print(f"Table saved to: {path}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")