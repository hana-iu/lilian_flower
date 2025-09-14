"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """This Function verifies whether pacman can eat a ghost or not
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.
    """
    return touching_power_pellet or touching_dot
    


def lose(power_pellet_active, touching_ghost):
    """Trigger the lose event when pacman doesn't have a power pellet on and touches a ghost
    """
    return  not power_pellet_active and touching_ghost
    



def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.
and pacman did not get eaten
    """
    didnot_lose = lose(power_pellet_active , touching_ghost)
    return not didnot_lose and has_eaten_all_dots
