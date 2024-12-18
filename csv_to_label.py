#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Uso: python csv_to_label.py input.csv label_cardio.hpp")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_hpp = sys.argv[2]

    if not os.path.isfile(input_csv):
        print("Il file di input non esiste: {}".format(input_csv))
        sys.exit(1)
    
    # Legge le label dal file
    labels = []
    with open(input_csv, 'r') as f:
        for line in f:
            val = line.strip()
            if val != "":
                # Converte in intero
                val_int = int(val)
                # Verifica che val_int sia 0, 1 o 2
                if val_int not in [0, 1, 2]:
                    print("Valore non valido nel file CSV: {}".format(val_int))
                    sys.exit(1)
                labels.append(val_int)
    
    if len(labels) == 0:
        print("Il file CSV non contiene label.")
        sys.exit(1)
    
    header_guard = "LABEL_CARDIO_HPP"
    array_name = "cardio_labels"
    
    lines = []
    lines.append("#ifndef {0}".format(header_guard))
    lines.append("#define {0}".format(header_guard))
    lines.append("")
    lines.append("#include <stdint.h>")
    lines.append("")
    lines.append("static const uint8_t {0}[] = {{".format(array_name))
    
    for l in labels:
        lines.append("    {0},".format(l))
    
    lines.append("};")
    lines.append("")
    lines.append("#endif")
    lines.append("")

    # Scrive il file di output
    with open(output_hpp, 'w') as out_f:
        for line in lines:
            out_f.write(line + "\n")

if __name__ == "__main__":
    main()
