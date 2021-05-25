import time
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QWidget
from ctypes import c_double, c_int, CDLL
import sys

#def Open_Lib():
class C_Functions(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        lib_path = 'basic_function_%s.so' % (sys.platform)
        try:
            self.basic_function_lib = CDLL(lib_path)
        except:
            print('OS %s not recognized' % (sys.platform))
            print(lib_path)

        
        self.python_c_DFT = self.basic_function_lib.DFT
        self.python_c_DFT.restype = c_double

        self.python_c_FFT = self.basic_function_lib.FFT
        self.python_c_FFT.restype = None




    def c_DFT(self,signal):
        size = len(signal)
        Signal_real = (c_double * size)(*signal)
        img = (c_double * size)()
        img2 = (c_double * size)()
        real2 = (c_double * size)()

        out=self.python_c_DFT(c_int(size),Signal_real, img ,real2,img2)
        
        return  Signal_real[:],img[:]

    def c_FFT(self,signal):
        size=len(signal)
        order = int(np.log2(len(signal)))
        s_img=np.zeros(size)
        c_arr_in = (c_double * size)(*signal)
        c_arr_out = (c_double * size)(*s_img)

        self.python_c_FFT(c_int(order), c_arr_in , c_arr_out)
        
        return c_arr_in[:], c_arr_out[:]


    def c_graphs(self):
        #Open_Lib()
        _,_,array = np.loadtxt("Signals\ECG.txt",unpack=True)

        n=0
        dftarr=[]
        fftarr=[]
        Funcs_Err=[]
        imgErr=[]
        #samplearr=[2^0,2^1,2^2,2^3,2^4,2^5,2^6,2^7,2^8,2^9,2^10]
        samplearr=[0,2,4,8,16,32,64,128,256,512,1024]
        #print(samplearr)
        for n in range(11):
            Magnitude=array[0:pow(2,n)]
            print(pow(2,n))
            tic1=time.perf_counter()
            #awl function
            real_DFT,img_DFT=self.c_DFT(Magnitude)
            toc1=time.perf_counter()
            calct1=toc1-tic1
            dftarr.append(calct1)
            tic2=time.perf_counter()
            #tany function
            real_FFT,img_FFT=self.c_FFT(Magnitude)

            toc2=time.perf_counter()
            calct2=toc2-tic2
            fftarr.append(calct2)

            difference_real = np.subtract(real_DFT, real_FFT)
            squared_real = np.square(difference_real)
            real_Error = squared_real.mean()
            difference_img = np.subtract(img_DFT, img_FFT)
            squared_img = np.square(difference_img)
            img_Error = squared_img.mean()
            Funcs_Err.append(((real_Error-img_Error)*(real_Error-img_Error))/2)
            #print(Realerr,Imgerr,mse)

        #print(dftarr)
        fig = plt.figure()
        dftpl = fig.add_subplot(131)
        fftpl = fig.add_subplot(132)
        Error_graph = fig.add_subplot(133)
        dftpl.set_title('DFT')
        dftpl.set_xlabel('sample no.')
        dftpl.set_ylabel('time')
        dftpl.plot(samplearr[1:],dftarr[1:])

        Error_graph.set_title('Mean Squared Error')
        Error_graph.set_xlabel('sample no.')
        Error_graph.set_ylabel('Error')
        Error_graph.plot(samplearr,Funcs_Err)

        dftpl.set_ylim(0,max(dftarr))
        fftpl.set_ylim(0,max(dftarr))
        


        fftpl.set_title('FFT')
        fftpl.set_xlabel('sample no.')
        fftpl.set_ylabel('time')
        fftpl.plot(samplearr[1:],fftarr[1:])

        plt.show()

#c_graphs()

# def do_square_using_c(list_in):
    
#     n = len(list_in)
#     c_arr_in = (c_double * n)(*list_in)

#     out=python_c_square(c_int(n), c_arr_in)
#     print((out))
#     return c_arr_in[:]

# my_list = np.arange(10,dtype=c_double)
# squared_list = do_square_using_c(my_list)
# print(squared_list)
# Try_signal = [0.0, 3219.0, 3035.0, 3346.0, 1006.0, 1797.0, 2456.0 , 1307.0 ]
# S_real,S_img = c_FFT(Try_signal)
# print(S_real,S_img)
# R,I = c_DFT(Try_signal) 
# print(R,I)
