from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
root_process_rank = 3

if rank == root_process_rank:
    array_to_share = [i for i in range(0,10)]
else:
    array_to_share = None
    
variable_received = comm.scatter(array_to_share, root = root_process_rank)
print("Process : " + str(rank) + " shared data : " + str(variable_received))



# scatter is similar to broadcast but with one major difference.
# Whie broadcast sends same data to all the processes, scatter can send chunks
# of data in an array to different processes
# scatter sends 1st element 1st process, 2nd element to second process ....etc.
# mpiexec must be called with number of processors equal to the array size above