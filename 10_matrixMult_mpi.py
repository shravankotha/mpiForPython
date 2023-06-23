from mpi4py import MPI
import numpy as np
import time
import inspect

def main():
    comm = MPI.COMM_WORLD
    size_comm = comm.Get_size()
    rank = comm.Get_rank()

    listNodes = [2,3,4,5,7,8,9,10, 13,14,15,16,19,20,21,22, 26,27,28,29,33,34,35,36, 41,42,43,44,49,50,51,52]
    listConnectivity = []
    for iElement in range(0,int(len(listNodes)/8)):
        listConnectivity.append([])
        index_start = iElement*8
        index_end = (iElement+1)*8
        for index in range(index_start,index_end):
            listConnectivity[iElement].append(listNodes[index])

    startIndicesPartition, endIndicesPartition = performLinearPartitioning(len(listConnectivity),size_comm)
    #comm.barrier()
    #iErrorAll = 0
    #comm.reduce(iError,iErrorAll,op=MPI.SUM,root=0)
    #print(type(iErrorAll),iErrorAll)
    #if sum(iErrorAll) < size_comm:
    #    if rank == 0:
    #        
    #    comm.finalize()    
       
    if rank == 0:
        print('startIndicesPartition: ', startIndicesPartition)
        print('endIndicesPartition: ', endIndicesPartition)
    listConnectivity_ = listConnectivity[startIndicesPartition[rank]:endIndicesPartition[rank]+1]  
    print('rank: ',rank, '  listConnectivity_: ',listConnectivity_)    
    listConnectivityRenumbered_ = renumberConnectivity(listConnectivity_,listNodes)
    comm.barrier()
    
    if rank ==0:
        listConnectivityRenumberedFinal = []
        for iData in range(0,len(listConnectivityRenumbered_)):
            listConnectivityRenumberedFinal.append(listConnectivityRenumbered_[iData])
        for iRank in range(1,size_comm):
            data = comm.recv(source=iRank)
            print('iRank: ',iRank, ' data:',data)
            for iData in range(0,len(data)):
                listConnectivityRenumberedFinal.append(data[iData])
        print('listConnectivityRenumberedFinal: ',listConnectivityRenumberedFinal)
    else:    
        comm.send(listConnectivityRenumbered_,dest=0)
    
def performLinearPartitioning(problemSize,nProcessors):    
    startIndicesPartition = []
    endIndicesPartition = []
    iError = 1
    error_tag = None
    if nProcessors > problemSize:
        iError = 0        
        error_tag = 'In function: ' + str(inspect.currentframe().f_code.co_name) + '\n       No of processors is > length of data to be partitioned' 
        raise RuntimeError(error_tag)

    leftOverProblemSize = problemSize%nProcessors
    equallyPartionedChunkSize = int((problemSize-leftOverProblemSize)/nProcessors)
    startIndicesPartition.append(0)
    endIndicesPartition.append(equallyPartionedChunkSize + leftOverProblemSize - 1)
    if nProcessors > 1:
        for iProcessor in range(1,nProcessors):
            startIndicesPartition.append(endIndicesPartition[iProcessor-1] + 1)
            endIndicesPartition.append(startIndicesPartition[iProcessor] + equallyPartionedChunkSize - 1)
    
    return startIndicesPartition, endIndicesPartition
    

def renumberConnectivity(listConnectivity,listNodes):
    arrayConnectivityRenumbered = np.array(listConnectivity)
    start = time.time()
    for iNodeActual in range(0,len(listNodes)):
        arrayConnectivityRenumbered[arrayConnectivityRenumbered == listNodes[iNodeActual]] = iNodeActual + 1                        
    return arrayConnectivityRenumbered.tolist()
    
if __name__ == "__main__":
    main()    