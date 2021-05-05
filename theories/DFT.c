//#include <iostream>
//using namespace std ;
#include <stdlib.h>
#include <math.h>
void DFT(int size, double* signal_real , double* imaginary);
void DFT(int size, double* signal_real , double* imaginary) 
{
    //double* imaginary = (double*)malloc(size * sizeof(double));
    double in_cosine;
    double cosine, sine;
    double* real = (double*)malloc(size * sizeof(double));
    double* img = (double*)malloc(size * sizeof(double));

    // if (real == NULL || img == NULL)
    //     return(0);

    for (int index = 0; index < size; index++) {
        real[index] = 0;
        img[index] = 0;
        in_cosine =   2.0 * 3.141592654 * (double)index / (double)size;
        for (long k = 0; k < size; k++) {
            cosine = cos(k * in_cosine);
            sine = sin(k * in_cosine);
            
            real[index] += (signal_real[k] * cosine);
            img[index] += (signal_real[k] * sine);
            
            
        }
    }

    for (int i = 0; i < size; i++) {
        signal_real[i] = real[i] ;
        imaginary[i] = img[i] ;
    }
    free(real);
    free(img);
    //return(1);
};
