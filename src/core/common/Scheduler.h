#ifndef SCHEDULER_H
#define SCHEDULER_H

#include <optional>
#include <vector>

#include "EmptyOption.h"

template <typename T, typename M = EmptyOption>
class Scheduler {

public:
    virtual ~Scheduler() = default;

    /**
     * Reset the state of the scheduler and removes all tasks
     */
    virtual void reset() = 0;

    virtual void load(T task, int burst, std::optional<M> option) = 0;

    virtual void load(std::vector<std::tuple<T, int, std::optional<M>>> tasks) {
        for (auto element: tasks) {
            load(std::get<0>(element), std::get<1>(element), std::get<2>(element));
        }
    }

    virtual std::optional<T> schedule() = 0;

    Scheduler(const Scheduler&) = delete;
    Scheduler& operator=(const Scheduler&) = delete;
    Scheduler() = default;
};



#endif //SCHEDULER_H
