def inputer(message: str, min_value: int, max_value: int) -> int:
    result: int | None = None

    print(message)
    while True:
        try:
            result = int(input(f"Your option ({min_value}-{max_value - 1}): "))
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
    local_message = f"{message}: \n"
    local_message += "\n".join([f"\t{i + 1}. {args[i]}" for i in range(len(args))])

    return inputer(local_message, 1, len(args)+1)
