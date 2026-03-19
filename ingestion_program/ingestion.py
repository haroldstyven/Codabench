import os
import sys
import pandas as pd

def run():
    input_dir = sys.argv[1]    # Datos públicos (public_data)
    output_dir = sys.argv[2]   # Resultados de la predicción
    program_dir = sys.argv[3]  # Scripts del organizador
    submission_dir = sys.argv[4] # Código del participante (model.py)

    sys.path.append(submission_dir)

    try:
        from model import Model
        m = Model()
        
        # Cargar datos de prueba
        data = pd.read_csv(os.path.join(input_dir, 'test_data.csv'))
        
        # Predicción
        predictions = m.predict(data)
        
        # Guardar resultados
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, 'results.txt'), 'w') as f:
            for p in predictions:
                f.write(f"{p}\n")
        print("Ingestión completada con éxito.")
        
    except Exception as e:
        print(f"Error en la ingestión: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()