from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("My rank is : " + str(rank))

if rank == 0:
    data_send = "a"
    destination_process = 1
    source_process = 1
    
    data_received = comm.sendrecv(data_send, dest = destination_process, source=source_process)
    print("sending data : " + str(data_send) + " to process : " + str(destination_process))
    print("received data : " + str(data_received) + " from process : " + str(source_process))

if rank == 1:
    data_send = "b"
    destination_process = 0
    source_process = 0
    
    data_received = comm.sendrecv(data_send, dest = destination_process, source=source_process)
    
    print("sending data : " + str(data_send) + " to process : " + str(destination_process))
    print("received data : " + str(data_received) + " from process : " + str(source_process))


# the above code always avoids deadlocks as it uses two different buffers for send and receive data