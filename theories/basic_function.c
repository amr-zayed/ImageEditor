#include <stdlib.h>
#include <math.h>
#include<stdio.h>
void FFT( long m, double* x, double* y);
double DFT(int size, double* S_Real, double* S_imaginary , double * real , double *img);

double DFT(int size, double* S_Real, double* S_imaginary ,  double * real , double *img)
{
    //double* imaginary = (double*)malloc(size * sizeof(double));
    double in_cosine;
    double cosine, sine;
    // double* real = (double*)malloc(size * sizeof(double));
    // double* img = (double*)malloc(size * sizeof(double));

    // if (real == NULL || img == NULL)
    //     return(0);
    for (int index = 0; index < size; index++) {
        real[index] = 0;
        img[index] = 0;
        in_cosine = 2.0 * 3.141592654 * (double)index / (double)size;
        for (long k = 0; k < size; k++) {
            cosine = cos(k * in_cosine);
            sine = sin(k * in_cosine);
            //printf("cos = %d and sin = %d \n", cosine, sine);
            real[index] += (S_Real[k] * cosine);
            img[index] += (S_Real[k] * sine);


        }
        
    }
    for (int i = 0; i < size; i++) {
        S_Real[i] = real[i];
        S_imaginary[i] = img[i];

    }
    // free(real);
    // free(img);
    return(real[0]);
}

// double DFT(int size, double* signal, double* Real , double* imaginary , double * real , double *img);
// double DFT(int size, double* signal , double* Real, double* imaginary , double * real , double *img) 
// {
//     //double* imaginary = (double*)malloc(size * sizeof(double));
//     //long index,k,i=0;
//     double in_cosine;
//     double cosine, sine;
//     // double* real = (double*)malloc(size * sizeof(double));
//     // double* img = (double*)malloc(size * sizeof(double));
//     real[0]=7.7;

//     // if (real == NULL || img == NULL)
//     //     return(0);
//     for (int index = 0; index < size; index+=1) {
//         real[index] = 0;
//         img[index] = 0;
//         in_cosine =   2.0 * 3.141592654 * (double)index / (double)size;
//         for (int k = 0; k < size; k+=1) {
            
//             cosine = cos(k * in_cosine);
//             sine = sin(k * in_cosine);
//             real[index] += (signal[k] * cosine);
            
//             img[index] += (signal[k] * sine);
            
            
//         }

//     }

//     for (int i = 0; i < size; i++) {
//         Real[i] = real[i] ;
//         imaginary[i] = img[i] ;
        
//     }
//     // free(real);
//     // free(img);
//     return(real[0]);
// }

void FFT( long m, double* x, double* y)
{
    long noOfSamples, i, i1, j, k, half_N, l, l1, l2;
    double c1, c2, tempx, t1, t2, u1, u2, z;

    /* Calculate the number of points because they dont know the power*/
    
    noOfSamples = 1;
    for (i = 0; i < m; i++)
        noOfSamples *= 2;
    

    /* Do the bit reversal */
   
    
    half_N = noOfSamples >> 1;

    j = 0;
    for (i = 0; i < noOfSamples - 1; i++) {
        if (i < j) {
            tempx = x[i];
            //ty = y[i];
            x[i] = x[j];
            //y[i] = y[j];
            x[j] = tempx;
            //y[j] = ty;
        }
        k = half_N;
        while (k <= j) {
            j -= k;
            k >>= 1;
        }
        j += k;
    }

    /* Compute the FFT */
    c1 = -1.0;
    c2 = 0.0;
    l2 = 1;
    for (l = 0; l < m; l++) {
        l1 = l2;
        l2 <<= 1;
        u1 = 1.0;
        u2 = 0.0;
        for (j = 0; j < l1; j++) {
            for (i = j; i < noOfSamples; i += l2) {
                i1 = i + l1;
                /*t1 = u1 * x[i1];
                t2 = u2 * x[i1];*/
                t1 = u1 * x[i1] - u2 * y[i1];
                t2 = u1 * y[i1] + u2 * x[i1];
                x[i1] = x[i] - t1;
                y[i1] = y[i] - t2;
                x[i] += t1;
                y[i] += t2;
                //y[i] = -y[i];
            }
            //y[j] = -y[j];
            z = u1 * c1 - u2 * c2;
            //cout << u1 << " and " << u2 << "\n";
            u2 = u1 * c2 + u2 * c1;
            u1 = z;

        }
        c2 = sqrt((1.0 - c1) / 2.0);
        
        c2 = -c2;
        c1 = sqrt((1.0 + c1) / 2.0);
    }

}

int c_square(int n, double *array_in_out)
{ //return the square of array_in of length n in array_out
    int i;
    
    for (i = 0; i < n; i++)
    {
        array_in_out[i] = array_in_out[i] * array_in_out[i];
    }
    return(7);
}
// int c_square(int n, double *array_in, double *array_out)
// { //return the square of array_in of length n in array_out
//     int i;
    
//     for (i = 0; i < n; i++)
//     {
//         array_out[i] = array_in[i] * array_in[i];
//     }
//     return(7);
// }