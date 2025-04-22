# Simulator

**Description**:  
The `Simulator` class provides a framework to simulate the execution of tasks using a given scheduling algorithm. It allows for step-by-step simulation of task execution, tracking the history of executed tasks, and managing task arrivals.

**Attributes**:  
- `scheduler`: The scheduler instance used to determine task execution order.  
- `batch`: A dictionary where keys are arrival times and values are lists of tasks arriving at those times.  
- `timestep`: The current time step in the simulation.  
- `history`: A list tracking the task executed at each time step.  
- `tasks`: A set of all tasks loaded into the simulator.  

**Methods**:  

### `__init__(self, scheduler)`  
Initializes the simulator with a given scheduler.  

**Parameters**:  
- `scheduler`: An instance of a scheduler to manage task execution.  

**Behavior**:  
- Initializes the `batch`, `timestep`, `history`, and `tasks` attributes.  

---

### `load(self, task: Task) -> None`  
Loads a single task into the simulator based on its arrival time.  

**Parameters**:  
- `task`: The task to be loaded.  

**Behavior**:  
- Adds the task to the `batch` dictionary under its arrival time.  

---

### `load_bulk(self, tasks: List[Task]) -> None`  
Loads multiple tasks into the simulator.  

**Parameters**:  
- `tasks`: A list of tasks to be loaded.  

**Behavior**:  
- Iterates through the list of tasks and loads each one using the `load` method.  

---

### `next(self) -> Task`  
Processes the next batch of tasks and schedules one for execution.  

**Behavior**:  
- Loads tasks arriving at the current `timestep` into the scheduler.  
- Returns the task selected by the scheduler for execution.  

**Returns**:  
- The task scheduled for execution or `None` if no tasks are available.  

---

### `advance(self) -> Task`  
Advances the simulation by one time step and schedules the next task.  

**Behavior**:  
- Calls the `next` method to schedule a task.  
- Increments the `timestep` by 1.  
- Appends the scheduled task (or `None`) to the `history`.  

**Returns**:  
- The task scheduled for execution in the current time step.  

---

### `history_matches(self, tasks: List[Task]) -> bool`  
Checks if the simulation's history matches a given list of tasks.  

**Parameters**:  
- `tasks`: A list of tasks to compare against the simulation's history.  

**Behavior**:  
- Compares the first `len(tasks)` elements of the `history` with the given list.  

**Returns**:  
- `True` if the history matches, `False` otherwise.  

---

### `reset(self) -> None`  
Resets the simulator and the scheduler.  

**Behavior**:  
- Resets the `timestep` to 0.  
- Calls the `reset` method of the scheduler.  

---

### `are_all_tasks_loaded(self) -> bool`  
Checks if all tasks have been loaded into the scheduler.  

**Behavior**:  
- Verifies that all tasks with arrival times up to the current `timestep` have been loaded.  

**Returns**:  
- `True` if all tasks are loaded, `False` otherwise.  

---

### `accept(self, visitor)`  
Accepts a visitor object to perform operations on the simulator.  

**Parameters**:  
- `visitor`: An object implementing a `visit` method for the simulator.  

**Behavior**:  
- Calls the `visit` method of the visitor with the simulator as an argument.  

---

**Notes**:  
- The `Simulator` class is designed to work with any scheduler implementing the required interface.  
- The `advance` method ensures that the simulation progresses in discrete time steps, while the `next` method schedules tasks without incrementing time.