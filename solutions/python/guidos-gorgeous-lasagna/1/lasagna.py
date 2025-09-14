EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
  
def preparation_time_in_minutes(number_of_layers):
     """This function takes number of layers of cake as a parameter and then return the total preparation time needed for the whole cake"""
     return PREPARATION_TIME * number_of_layers


#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """This function takes two parameters and returns the total time of baking process both preparation and baking
    """
    total_prep_time = preparation_time_in_minutes(number_of_layers)
    return total_prep_time + elapsed_bake_time

