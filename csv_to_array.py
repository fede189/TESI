#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        print("Uso: python csv_to_array input.csv output.hpp")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_hpp = sys.argv[2]

    if not os.path.isfile(input_csv):
        print("Il file input CSV non esiste: {}".format(input_csv))
        sys.exit(1)
    
    # Legge il CSV
    rows = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # Convertiamo in float
            float_row = []
            for val in row:
                val = val.strip()
                if val == "":
                    # Se la cella è vuota, metti 0.0 oppure gestiscila diversamente.
                    float_row.append(0.0)
                else:
                    float_row.append(float(val))
            rows.append(float_row)
    
    if len(rows) == 0:
        print("Il file CSV è vuoto.")
        sys.exit(1)
    
    num_rows = len(rows)
    num_cols = len(rows[0])
    
    # Verifica che tutte le righe abbiano la stessa lunghezza
    for r in rows:
        if len(r) != num_cols:
            print("Le righe del CSV hanno lunghezze diverse. Non si può creare un array regolare.")
            sys.exit(1)
    
    # Genera il contenuto dell'header
    header_guard = "CARDIO_HPP"
    array_name = "cardio_data"
    
    lines = []
    lines.append("#ifndef {0}".format(header_guard))
    lines.append("#define {0}".format(header_guard))
    lines.append("")
    lines.append("static const float {0}[{1}][{2}] = {{".format(array_name, num_rows, num_cols))
    
    for row in rows:
        # Formattazione: {val1, val2, ...}
        row_str = ", ".join("{0:.19f}f".format(v) for v in row)
        lines.append("    {" + row_str + "},")
    
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
