#include <common/Scheduler.h>
#include <common/Simulator.h>
#include <schedulers/FCFS_Scheduler.h>

#include <gtest/gtest.h>


TEST(FCFS_Test, BasicAssertions) {
    const auto sch = new FCFS_Scheduler<std::string>();
    Simulator sim(sch);

    sim.load({"task 1", 5});

    sim.load({
    {"task 2", 12, 8},
    {"task 3", 12, 8},
    });

    EXPECT_EQ(sim.next(), "task 1");
}