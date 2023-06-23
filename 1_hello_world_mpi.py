from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank==0:
    print('communication ize: ',size)
print("hello world from processor : ", rank)