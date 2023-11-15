"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730573354"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, point: Point) -> float:
        """Method that finds the distance between 2 points and returns it."""
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Method which is used to count ticks and determine when a cell gains immunity."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.sickness = -1
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        elif self.is_infected() is True:
            return "red"
        elif self.is_immune() is True:
            return "blue"

    def contract_disease(self) -> None:
        """Method that starts certain cells as infected from the beginning."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Method that checks if a cell is vulnerable and returns true if it is."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Method that checks if a cell is infected and returns true if it is."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, other_cell: Cell) -> None:
        """Method that makes infected cells infect other cells."""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()
        elif self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Used to make certain cells immune from start."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Checks if the cell is immune and returns true if it is."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, inf_cells: int, imm_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if inf_cells < 1:
            raise ValueError("Infected Starting Value is below 1!")
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if inf_cells != 0:
                cell.contract_disease()
                inf_cells -= 1
            else:
                if imm_cells != 0:
                    cell.immunize()
                    imm_cells -= 1
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            self.enforce_bounds(cell)
            cell.tick()
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.sickness >= 1:
                return False
        return True
    
    def check_contacts(self) -> None:
        """Method that checks whether 2 cells make contact."""
        for i in range(len(self.population)):
            for z in range(len(self.population)):
                if i == z:
                    pass
                else:
                    if Point.distance(self.population[i].location, self.population[z].location) < constants.CELL_RADIUS:
                        self.population[z].contact_with(self.population[i])