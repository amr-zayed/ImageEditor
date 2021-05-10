#include <stdlib.h>
#include <math.h>
#include<stdio.h>
void FFT( long m, double* x, double* y);
double DFT(int size, double* S_Real, double* S_imaginary , double * real , double *img);

double DFT(int size, double* S_Real, double* S_imaginary ,  double * real , double *img)
{
    double in_cosine;
    double cosine, sine;
    
    for (int index = 0; index < size; index++) {
        real[index] = 0;
        img[index] = 0;
        in_cosine = 2.0 * 3.141592654 * (double)index / (double)size;
        for (long k = 0; k < size; k++) {
            cosine = cos(k * in_cosine);
            sine = sin(k * in_cosine);
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


void FFT( long S_power, double* x, double* y)
{
    long noOfSamples, i, span, j,matrixNO, k, half_N, counter, n_submatrix, step;
    double c1, c2, temp1,temp2, u1, u2, z;

    /* Calculate the number of points because they dont know the power*/
    
    noOfSamples = 1;
    for (i = 0; i < S_power; i++)
        noOfSamples *= 2;
    

    /* Do the bit reversal */
    half_N = noOfSamples >> 1;

    j = 0;
    for (i = 0; i < noOfSamples - 1; i++) {
        if (i < j) {
            temp1 = x[i];
            x[i] = x[j];
            x[j] = temp1;
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
    step = 1;
    for (counter = 0; counter < S_power; counter++) {
        n_submatrix = step;
        step <<= 1;
        u1 = 1.0;
        u2 = 0.0;
        for (matrixNO = 0; matrixNO < n_submatrix; matrixNO++) {
            for (i = matrixNO; i < noOfSamples; i += step) {
                span = i + n_submatrix;
                
                temp1 = u1 * x[span] - u2 * y[span];
                temp2 = u1 * y[span] + u2 * x[span];
                x[span] = x[i] - temp1;
                y[span] = y[i] - temp2;
                x[i] += temp1;
                y[i] += temp2;
            }
            z = u1 * c1 - u2 * c2;
            u2 = u1 * c2 + u2 * c1;
            u1 = z;

        }
        c2 = sqrt((1.0 - c1) / 2.0);
        
        c2 = -c2;
        c1 = sqrt((1.0 + c1) / 2.0);
    }
    for (i = 0; i < noOfSamples; i++)
    {
        y[i] = -y[i];
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
