#ifndef SIMULATOR_H
#define SIMULATOR_H
#include <unordered_map>

#include "Scheduler.h"


template <typename T>
class Simulator {
  Scheduler<T> * sch;

  std::unordered_map<int, std::vector<std::pair<T, int>>> batch;
  int timestep = 0;

public:
  explicit Simulator (Scheduler<T> * sch): sch(sch) {
  }

  void load(TaskEntry<T> entry) {
    batch[timestep + entry.arrival_time].emplace_back(std::pair(entry.task, entry.burst_time));
  }

  void load(const std::vector<TaskEntry<T>>& entries) {
    for (auto element: entries) {
      load(element);
    }
  }

  std::optional<T> next() {
    sch->load(batch[timestep]);
    return sch->schedule();
  }

  void pass() {
    next();
  }

  void reset() {
    timestep = 0;
    sch.reset();
  }
};



#endif //SIMULATOR_H
