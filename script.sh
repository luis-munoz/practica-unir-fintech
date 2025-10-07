#!/bin/bash

set -e

echo "======================================"
echo "Script de procesamiento de palabras"
echo "======================================"

WORDS_FILE=${1:-words.txt}

if [ ! -f "$WORDS_FILE" ]; then
    echo "Error: El archivo $WORDS_FILE no existe"
    exit 1
fi

echo "Procesando archivo: $WORDS_FILE"
echo ""

echo "Total de líneas:"
wc -l < "$WORDS_FILE"

echo ""
echo "Primeras 5 palabras:"
head -5 "$WORDS_FILE"

echo ""
echo "Ejecutando script Python..."
python3 main.py "$WORDS_FILE"

echo ""
echo "Proceso completado exitosamente"