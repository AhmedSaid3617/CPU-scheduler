#ifndef SIMULATOR_H
#define SIMULATOR_H
#include <unordered_map>

#include "Scheduler.h"
#include "TaskEntry.h"

template <typename T, typename M = EmptyOption>
class Simulator {
  Scheduler<T, M> * sch;

  std::unordered_map<int, std::vector<std::tuple<T, int, std::optional<M>>>> batch;
  int timestep = 0;

public:
  explicit Simulator (Scheduler<T, M> * sch): sch(sch) {
  }

  void load(TaskEntry<T, M> entry) {
    batch[timestep + entry.arrival_time].emplace_back(std::tuple<T, int, std::optional<M>>(entry.task, entry.burst_time, entry.option));
  }

  void load(const std::vector<TaskEntry<T, M>>& entries) {
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
