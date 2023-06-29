from mpi4py import MPI
import time

def main():
    comm = MPI.COMM_WORLD
    size_comm = comm.Get_size()
    rank = comm.rank
    passCommunicator(comm)
    rank_returned, time_ = computeParallel(rank)
    
    print('Processor:',rank,' -- time: ',time_)

def passCommunicator(comm):
    rank = comm.rank
    for iRank in range(0,comm.Get_size()):
        print('Printing from processor :',iRank)
    return

def computeParallel(rank):
    time_start = MPI.Wtime()
    print('Printing individually from processor :',rank)
    time.sleep(rank)
    return rank, MPI.Wtime()-time_start
    
if __name__ == "__main__":
    main()    