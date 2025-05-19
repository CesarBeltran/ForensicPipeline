import os
import subprocess

# Configuración inicial
VOLATILITY_PATH = "vol.py"  # Asumiendo que estás en el folder correcto
MEMORY_IMAGE = "/home/kali/Desktop/LLMForensics/wcry.raw"
OUTPUT_DIR = "/home/kali/Desktop/LLMForensics/output/volatility"

# Lista de plugins a ejecutar
PLUGINS = [
    "windows.info.Info",
    "windows.pslist.PsList",
    "windows.pstree.PsTree",
    "windows.psscan.PsScan",
    "windows.psxview.PsXView",
    "windows.malfind.Malfind",
    # OpcionalesdS
    "windows.netscan.NetScan",
    "windows.hashdump.Hashdump",
    "windows.lsadump.Lsadump",
    "windows.dumpfiles.DumpFiles",

]

def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def run_plugin(plugin):
    output_file = os.path.join(OUTPUT_DIR, f"{plugin.replace('.', '_')}.json")
    print(f"[*] Ejecutando {plugin}...")
    
    try:
        with open(output_file, "w") as outfile:
            subprocess.run([
                "python", VOLATILITY_PATH,
                "-f", MEMORY_IMAGE,
                "-r", "json",
                plugin
            ], stdout=outfile, stderr=subprocess.DEVNULL)
        print(f"[+] Resultado guardado en {output_file}\n")
    except Exception as e:
        print(f"[!] Error ejecutando {plugin}: {str(e)}\n")

def main():
    ensure_output_dir(OUTPUT_DIR)

    for plugin in PLUGINS:
        run_plugin(plugin)

if __name__ == "__main__":
    main()

