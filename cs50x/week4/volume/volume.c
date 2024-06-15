// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // read and write the wav header
    uint8_t header_buff[HEADER_SIZE];
    fread(&header_buff, sizeof(header_buff), 1, input);
    fwrite(&header_buff, sizeof(header_buff), 1, output);

    // read and write sample data
    int16_t data_buff;
    while (fread(&data_buff, sizeof(data_buff), 1, input))
    {
        data_buff = data_buff * factor;
        fwrite(&data_buff, sizeof(data_buff), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
