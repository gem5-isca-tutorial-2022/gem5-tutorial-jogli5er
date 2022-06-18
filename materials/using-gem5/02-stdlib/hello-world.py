from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import Resource
from gem5.simulate.simulator import Simulator

# obtain components:
cache_hierarchy = NoCache() # Processor connects directly to memory
memory = SingleChannelDDR3_1600("16GiB")
processor = SimpleProcessor(cpu_type=CPUTypes.ATOMIC, num_cores=1)

# Add components to the board
# Simple board is enough for this case but might needs more
board = SimpleBoard(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

binary = Resource("x86-hello64-static")
board.set_se_binary_workload(binary)

sim = Simulator(board=board)
sim.run()