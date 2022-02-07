from importlib.resources import read_text as resource_read_str

from train import data


def main() -> None:
    """Main function."""
    text = resource_read_str(data, "helloworld.txt")
    print(text)


if __name__ == "__main__":
    main()
