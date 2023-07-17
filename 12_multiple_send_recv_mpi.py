from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.rank
size_comm = comm.Get_size()

if rank == 0:    
    for host_processor in range(1,size_comm):
        data1=comm.recv(source = host_processor)
        print("receiving data from processor : " + str(host_processor)  + " @ time :" + str(time.time()) + " data1 : " + str(data1))
    for host_processor in range(1,size_comm):
        data1=comm.recv(source = host_processor)
        print("receiving data from processor : " + str(host_processor)  + " @ time :" + str(time.time()) + " data1 : " + str(data1))        
else:        
    destination_process = 0
    data1 = rank*[1,2,3,4]      
    comm.send(data1,dest=destination_process)
    print("sending data from processor : " + str(rank)  + " @ time :" + str(time.time()) + " data1 : " + str(data1))
    data1 = rank
    comm.send(data1,dest=destination_process)
    print("sending data from processor : " + str(rank)  + " @ time :" + str(time.time()) + " data1 : " + str(data1))