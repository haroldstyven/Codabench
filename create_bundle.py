import os
import zipfile

def zip_directory(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), folder_path)
                zipf.write(os.path.join(root, file), rel_path.replace('\\', '/'))
    print(f"✅ Creado: {zip_name}")

def create_competition_bundle():
    sub_zips = ['ingestion_program', 'scoring_program', 'public_data', 'reference_data']
    final_bundle_name = 'bundle_reto.zip'
    
    # 1. Crear los zips internos
    for folder in sub_zips:
        if os.path.exists(folder):
            zip_directory(folder, f"{folder}.zip")

    # 2. Crear el bundle raíz
    print(f"\n📦 Generando {final_bundle_name}...")
    with zipfile.ZipFile(final_bundle_name, 'w', zipfile.ZIP_DEFLATED) as bundle:
        # Archivos raíz
        for f in ['competition.yaml', 'logo.png']:
            if os.path.exists(f):
                bundle.write(f)
        
        # Carpeta html
        if os.path.exists('html'):
            for root, dirs, files in os.walk('html'):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, 'html')
                    bundle.write(full_path, f"html/{rel_path}")

        # Los zips internos
        for folder in sub_zips:
            z = f"{folder}.zip"
            if os.path.exists(z):
                bundle.write(z)

    print(f"\n🚀 ¡Todo listo! Sube el archivo '{final_bundle_name}'")

if __name__ == "__main__":
    create_competition_bundle()