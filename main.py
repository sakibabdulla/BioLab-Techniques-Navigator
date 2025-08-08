# main.py
import importlib

def show_menu():
    print("\n🔬 Welcome to the BioLab-Techniques-Navigator!")
    print("Choose a technique group to explore:\n")
    print("A. Molecular Biology & Recombinant DNA Methods")
    print("B. Histochemical & Immunotechniques")
    print("C. Biophysical Methods")
    print("D. Statistical Methods")
    print("E. Radiolabeling Techniques")
    print("F. Microscopic Techniques")
    print("G. Electrophysiological Methods")
    print("H. Methods in Field Biology")

    choice = input("\nEnter your choice (A-H): ").strip().upper()
    return choice

def launch_module(choice):
    try:
        if choice in "ABCDEFGH":
            module = importlib.import_module(f"techniques.enhanced_technique_{choice.lower()}")
            module.run()
        else:
            print("❌ Invalid choice. Please enter a letter between A and H.")
    except Exception as e:
        print(f"Error loading module: {e}")

def run_main_menu():
    choice = show_menu()
    launch_module(choice)

if __name__ == "__main__":
    run_main_menu()
