#include <stdlib.h>
#include <math.h>
#include<stdio.h>
double DFT(int size, double* signal, double* Real , double* imaginary);
double DFT(int size, double* signal , double* Real, double* imaginary ) 
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
            real[index] += (signal[k] * cosine);
            img[index] += (signal[k] * sine);
            
            
        }
    }

    return(real[0]);
    for (int i = 0; i < size; i++) {
        Real[i] = real[i] ;
        imaginary[i] = img[i] ;
        
    }
    free(real);
    free(img);
}
int main() {
    double  signal[8] = {0.0, 3219.0, 3035.0, 3346.0, 1006.0, 1797.0, 2456.0 , 1307.0 };
    
    printf("Hello") ;
    double *real;
    double *img;
    DFT( 8, signal, real, img);
    // for (int i = 0; i < 8; i++) {
    //     printf((char)real[i]);

    // }
    return(1);
};