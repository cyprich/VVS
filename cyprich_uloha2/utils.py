"""Utilities."""


def inputer(message: str, min_value: int, max_value: int) -> int:
    """Asks user to choose numeric value from range.

    If the user enters invalid value, it asks again

    :param message: Text, that displays before asking user to input value
    :param min_value: Minimal value that user can choose from (included)
    :param max_value: Maximal value that user can choose from (excluded)
    :return: Returns the value that user entered
    """
    print(message)

    while True:
        try:
            result: int = int(input(f"Your option ({min_value}-{max_value - 1}): "))
            if result not in range(min_value, max_value):
                raise IndexError
            break
        except ValueError:
            print("You didn't enter a number...")
        except IndexError:
            print(f"You didn't enter a number from {min_value} to {max_value - 1}...")
        except Exception as e:
            print(f"Unexpected error happened...\n{e}")

    return result


def decider(message: str, *args) -> int:
    """Asks user to choose from certain values.

    Used when it's necessary to display additional message, not only to choose numerical value
    Uses "inputer" function

    :param message: Text that displays before asking user to input value
    :param args: Values to choose from. Displays them line by line, with number before them
    :return: Returns the value that user entered
    """
    local_message: str = f"{message}: \n"
    local_message += "\n".join([f"\t{i + 1}. {args[i]}" for i in range(len(args))])

    return inputer(local_message, 1, len(args) + 1)


def rgb_inputer(message: str, max_value: int = 255) -> tuple[int, int, int]:
    result: list[int] = []
    colors = ["red", "green", "blue"]

    print(f"{message}: ")
    for i in range(3):
        while True:
            try:
                user = int(input(f"\tValue for {colors[i]} (0-{max_value}): "))
                if user not in range(max_value + 1):
                    raise IndexError
                result.append(user)
                break
            except ValueError:
                print("You didn't enter a number...")
            except IndexError:
                print(f"You didn't enter a number from 0 to {max_value}...")
            except Exception as e:
                print(f"Unexpected error happened...\n{e}")
    return result[0], result[1], result[2]