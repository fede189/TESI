#include "cardio.hpp"
#include  <cstdio>
#include <stdio.h>

extern "C" {			// Klessydra dsp_libraries are written in C and so they're imported as extern:
#include "dsp_functions.h"
#include "functions.h"
}


int main(){
    __asm__("csrw 0x300, 0x8;"); // Enable interrupts for all threads
    sync_barrier_reset();
    sync_barrier_thread_registration();

    if (Klessydra_get_coreID() == 0) {
        printf("\n\e[93m--- CARDIO PRINT TEST ---\e[39m\n");
    for(int i = 0; i < ROWS; i+=2000){
        printf("riga %d:\t",i);
        for(int j = 0; j < COLS; j++){
            printf("%d, ",cardio_data[i][j]);
        }
        printf("\n");
    }
    }
    sync_barrier();
    return 0;
}