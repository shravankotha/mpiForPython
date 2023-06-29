from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
#print("My rank is : " + str(rank))
root_process_rank = 0

if rank == root_process_rank:
    data_to_send = [1,2,3]
else:
    data_to_send = None
    
variable_shared = comm.bcast(data_to_send, root = root_process_rank)    # shares the data to all processors including itself
print("Process : ", rank, " shared data : ",variable_shared)


# bcast is collective, i.e. all the processes must call it