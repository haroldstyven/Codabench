import os
import zipfile

def zip_directory(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), folder_path)
                zipf.write(os.path.join(root, file), rel_path.replace('\\', '/'))
    print(f"Created: {zip_name}")

def create_competition_bundle(source_dir, output_zip, html_folder):
    """Generates a zip bundle for a Codabench challenge."""
    sub_zips = ['ingestion_program', 'scoring_program', 'public_data', 'reference_data']
    
    original_dir = os.getcwd()
    if source_dir != ".":
        os.chdir(source_dir)
    
    # 1. Crear los zips internos
    for folder in sub_zips:
        if os.path.exists(folder):
            zip_directory(folder, f"{folder}.zip")

    # 2. Crear el bundle raíz
    print(f"\nGenerating {output_zip}...")
    output_path = os.path.join(original_dir, output_zip) if source_dir != "." else output_zip
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as bundle:
        # Archivos raíz
        for f in ['competition.yaml', 'logo.png']:
            if os.path.exists(f):
                bundle.write(f)
        
        # Carpetas de páginas e imágenes
        for folder in [html_folder, 'img']:
            if os.path.exists(folder):
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, folder)
                        bundle.write(full_path, f"{folder}/{rel_path}")

        # Los zips internos
        for folder in sub_zips:
            z = f"{folder}.zip"
            if os.path.exists(z):
                bundle.write(z)
                os.remove(z) # Cleanup internal zip

    if source_dir != ".":
        os.chdir(original_dir)
    print(f"All set! Bundle created at '{output_zip}'\n")

if __name__ == "__main__":
    print("=== Constructing Task 1: NALEF Food Safety ===")
    create_competition_bundle("challenge-plant", "challenge-plant.zip", "pages")
    
    print("=== Constructing Task 2: GastroCorp NER 2026 ===")
    create_competition_bundle("challenge_gastro", "challenge_gastro.zip", "pages")