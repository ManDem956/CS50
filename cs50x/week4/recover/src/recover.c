#include <getopt.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef uint8_t BYTE;

#ifndef TEST
int main(int argc, char *argv[])
{

    if (argc < 2)
    {
        printf("Usage: recover [filename]\n");
        return 1;
    }

    char *infile = argv[optind];

    FILE *inptr = fopen(infile, "r");
    FILE *outptr = NULL;
    char filename[8];

    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    // Allocating read buffer in heap
    BYTE *READBUFFER = malloc(sizeof(BYTE) * 512);

    int counter = 0;
    while (fread(READBUFFER, sizeof(BYTE) * 512, 1, inptr) == 1)
    {
        // Check if the block is a start of a new jpeg file
        if (READBUFFER[0] == 0xFF && READBUFFER[1] == 0xD8 && READBUFFER[2] == 0xFF &&
            (READBUFFER[3] & 0xF0) == 0xE0)
        {
            if (outptr != NULL)
            {
                fclose(outptr);
            }

            sprintf(filename, "%03d.jpg", counter++);
            outptr = fopen(filename, "w");
        }

        if (outptr != NULL)
        {
            fwrite(READBUFFER, sizeof(BYTE) * 512, 1, outptr);
        }
    }

    // cleaning up
    free(READBUFFER);
    fclose(inptr);

    if (outptr != NULL)
    {
        fclose(outptr);
    }
}
#endif