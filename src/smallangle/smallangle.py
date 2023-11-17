# a programme that uses click to print either the sin or tan of a certain number of values between 0 to 2pi 

import click
import numpy as np
from numpy import pi
import pandas as pd

# we will create a group of commands
@click.group()
def cmd_group():
    pass

# add subcommand to calculate sin
@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default=10,
    help="Number of x values between 0 and 2pi.",
    show_default=True)
def sin(number):
    """print sin of *number* values evenly spaced between 0 and 2pi

    Args:
        number (int): 0 and 2pi is evenly divided into *number* values inbetween
    """
    x = np.linspace(0, 2 * pi, number)

    # check if number is integer
    if type(number) == int:
        df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
        print(df)
        return

# add subcommand to calculate tan
@cmd_group.command()
@click.option(
    "-number",
    "-n",
    default=10,
    help="Number of x values between 0 and 2pi.",
    show_default=True)
def tan(number):
    """print tan of *number* values evenly spaced between 0 and 2pi

    Args:
        number (int): 0 and 2pi is evenly divided into *number* values inbetween
    """
    x = np.linspace(0, 2 * pi, number)

    # check if number is integer
    if type(number) == int:
        df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
        print(df)
        return

if __name__ == "__main__":
    cmd_group()

# information on the subcommands and their functions
# obtain with smallangle.py (subcommand) --help
help(sin)
help(tan)