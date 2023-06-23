# caution : bugs exist in this code !!!!
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
root_process_rank = 0
myvalue = np.array([rank+1])
value_prod = np.zeros(1)

print('rank: ',rank,' myvalue: ',myvalue)

comm.Reduce(myvalue,value_prod,MPI.PROD)   # comm.reduce won't work
if rank == 0: 
    print("product of received Data: ",value_prod)
    
value_sum = np.zeros(1)
comm.reduce(myvalue,op=MPI.SUM,root=0)    

if rank == 0: 
    print("sum of received Data: ",value_sum)
