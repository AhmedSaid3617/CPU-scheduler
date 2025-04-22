# CPU Scheduler Simulator Documentation

# Introduction

This is a CPU Scheduler Simulator. It simulates the behavior of different CPU scheduling algorithms, allowing users to visualize how each algorithm manages processes in a CPU environment. The simulator provides a graphical user interface (GUI) for easy interaction and understanding of the scheduling algorithms.

## Team
| Name                             | Role                                                                       |
|----------------------------------|----------------------------------------------------------------------------|
| Shams El-Din Mohamed Abdel-Monem | Core Simulator Engine, Documentation compiling, FCFS scheduler             |
| Ahmed Said Sayed                 | Repo maintenance, pull-requests reviewer, Task model updating, GUI windows |
| Abdelrahman Sherif Hassan        | SJF, Priority (preemptive and non-preemptive) schedulers                   |
| Mahmoud Essam Noureldin          | GUI testing and maintenance                                                |
| Omar Tamer Mohamed               | Round Robin scheduler, verified and fixed statistics                       |
| Fares Khalaf Salman Sultan       | Verified FCFS, Priority scheduler. Fixed issues                            |
| Kareem Gaber El Halaby           | Python packages management, GUI windows, fixed issues in Core Simulator    |

## Architecture

The simulator is designed with a modular architecture, allowing for easy addition and modification of scheduling algorithms. The core components of the simulator include:
- **Simulator**: The main engine that wraps the scheduling algorithms and manages the simulation process.
- **Schedulers**: Different scheduling algorithms implemented as classes, each with its own logic for managing processes, uncoupled from other schedulers.
- **GUI**: The graphical user interface that allows users to interact with the simulator, input processes, and visualize the scheduling process.

## Testing

We have utilized the `unittest` framework for testing the simulator. Each scheduler has its own set of unit tests to ensure correctness and reliability. The tests cover various scenarios, including edge cases and typical use cases.

```{figure} testing1.png
:scale: 50 %

Final tests run, all passed.
Testing proved to be a really important step in the development process, as it helped us identify and fix bugs early on.
```

```{figure} github1.png
:scale: 50 %

Use of GitHub Issues to have a clear view of the bugs and issues we faced during the development process.
```

```{figure} gactions1.png
:scale: 50 %

Use of GitHub Actions to run the tests automatically on every Pull Request, to spot on bad code before merging.
```


# Simulator
```{toctree}
sections/simulator.md
```

# Scheduler Interface
```{toctree}
sections/scheduler.md
```

# Schedulers

## FCFS
```{toctree}
sections/fcfs.md
```

## SJF
```{toctree}
sections/sjf.md
```

## Priority
```{toctree}
sections/priority.md
```

## Round Robin
```{toctree}
sections/RoundRobin.md
```
# GUI

```{toctree}
sections/gui.md
```