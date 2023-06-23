from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 4:
    host_process = 0
    data = comm.recv(source = host_process)
    print("data received in process : " + str(rank) + " @ time :" + str(time.time()) + " data: " + str(data))

if rank == 0:
    time.sleep(5)
    data = 10000000
    host_process = 5
    data = comm.recv(source = host_process)
    destination_process = 4    
    comm.send(data, dest=destination_process)
    print("sending data from processor : " + str(rank)  + " @ time :" + str(time.time()) + " data : " + str(data))
    
if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data,dest=destination_process)
    print("sending data from processor : " + str(rank)  + " @ time :" + str(time.time()) + " data : " + str(data))
    
if rank == 8:
    host_process = 1
    data = comm.recv(source = host_process)
    print("data received in process : " + str(rank)  + " @ time :" + str(time.time())+ " data: " + str(data))
    
if rank == 5:
    data = 5000000
    destination_process = 0 #1
    comm.send(data, dest=destination_process)
    print("sending data from processor : " + str(rank)  + " @ time :" + str(time.time()) + " data : " + str(data))
    
# send() hangs if the message is not received by the destination process i.e. the host process keeps waiting forever. This
# happens if there is no matching recv() function in the destiantion processor
# recv() process keeps waiting for a message from host process. If there is no message from host process, it keeps waiting.
# The send-receive protocol involves the following:
# 1. First the send() process requests recv() process to send
# 2. recv() process permits the send() process to send
# 3. send() process now sends the data to recv() process
# i.e. send() and recv() are called blocking communications (i.e. the calling process waits for thrir completion)
# IMPORTANT NOTE: In some implementations of mpi, send() buffer is stored in some other place and some situations that we 
# think should lead to deadlock situations will not arise. For example, see send_recv_deadlock_mpi.py file for an example 
# of this situation.
    