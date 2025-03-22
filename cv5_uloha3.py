from machine import Pin, PWM


def get_user_input_part(n: int, min_value: int, max_value:int) -> int:
    i: int
    while True:
        try:
            i = int(input(f"Enter input #{n} (value from interval <{min_value}, {max_value}>): "))
            if i < min_value or i > max_value:
                raise Exception
            break

        except:
            print("You didnt enter the right value...")

    return i

def get_user_input() -> list[int]:
    out = list()

    for i in range(3):
        out.append(get_user_input_part(i, 0, 1023))

    return out

def cv5():
    r_duty, g_duty, b_duty = get_user_input()

    r = PWM(21, freq=120, duty_u16=r_duty*64)
    g = PWM(11, freq=120, duty_u16=g_duty*64)
    b = PWM(10, freq=120, duty_u16=b_duty*64)


