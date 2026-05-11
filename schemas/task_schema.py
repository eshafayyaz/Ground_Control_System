from pydantic import BaseModel
from typing import List, Union
from enum import Enum


class TaskType(str, Enum):
    TAKEOFF = "TAKEOFF"
    MOVE = "MOVE"
    ACTION = "ACTION"
    LAND = "LAND"


class MoveTask(BaseModel):
    task_type: TaskType
    coordinates: str

class ActionTask(BaseModel):
    task_type: TaskType
    action: str


class TakeoffTask(BaseModel):
    task_type: TaskType

class LandTask(BaseModel):
    task_type: TaskType


Task = Union[TakeoffTask, MoveTask, ActionTask, LandTask]

class TaskList(BaseModel):
    tasks: List[Task] = []