from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("My rank is : " + str(rank))

if rank == 0:
    data_send = "a"
    destination_process = 1
    source_process = 1
    
    comm.send(data_send, dest = destination_process)    
    data_received = comm.recv(source = source_process)        
    print("sending data : " + str(data_send) + " to process : " + str(destination_process))
    print("received data : " + str(data_received) + " from process : " + str(source_process))

if rank == 1:
    data_send = "b"
    destination_process = 0
    source_process = 0
    
    comm.send(data_send, dest = destination_process)
    data_received = comm.recv(source = source_process)            
    print("sending data : " + str(data_send) + " to process : " + str(destination_process))
    print("received data : " + str(data_received) + " from process : " + str(source_process))
    
# Conditions that work or that does not work:
# processor 0: send() and receive() &&& processor 1: send() and receive() --> works (works in this implementation of mpi (for this mpi4py). but may not work with other implementations. see https://stackoverflow.com/questions/20448283/deadlock-with-mpi)
# processor 0: receive() and send() &&& processor 1: receive() and send() --> does not work (deadlock)
# processor 0: send() and receive() &&& processor 1: receive() and send() --> works
# processor 0: receive() and send() &&& processor 1: send() and receive() --> works
# Therefore, it is always advisable to write codes that do not lead to deadlocks 
# irrespective of the mpi implementation that we may use. For example, use only 
# cases 3 and 4 while coding and avoid case 1 and case 2 even though case 1 works here.
