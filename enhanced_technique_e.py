# enhanced_technique_e.py


def run():
    print("\n☢️ Radiolabeling Techniques")
    print("=" * 70)
    print("🔍 Techniques involving radioactive isotopes to trace biological molecules.\n")

    techniques = {
        1: ("Use of 32P, 35S, 3H, and 14C isotopes in biological experiments", "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-4 hours | 💰 $$"),
        2: ("Radiolabeling of nucleic acids and proteins", "⭐⭐⭐⭐☆ Advanced | ⏱️ 4-6 hours | 💰 $$$"),
        3: ("Detection using autoradiography and scintillation counting", "⭐⭐⭐☆☆ Intermediate | ⏱️ 3-5 hours | 💰 $$"),
        4: ("Pulse-chase experiments to study biosynthetic pathways", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-2 days | 💰 $$$"),
        5: ("Safety and disposal protocols for radiolabeled materials", "⭐⭐☆☆☆ Beginner | ⏱️ 1-2 hours | 💰 $")
    }

    while True:
        print("\n📘 Choose a technique to explore:")
        for key, (title, meta) in techniques.items():
            print(f" {key:2d}. {title}\n     {meta}")

        try:
            choice = int(input("\nEnter the number of the technique: "))
            if choice not in techniques:
                print("❌ Invalid choice.")
                continue

            title, _ = techniques[choice]
            print(f"\n🧪 Step-by-Step Workflow: {title}")
            print("=" * 80)
            print(f"\n📖 Intro: {get_intro(choice)}\n")


            steps = get_workflow(choice)
            total = len(steps)
            for i, step in enumerate(steps, 1):
                print(f"\n📌 Step {i}/{total}: {step}")
                progress = "█" * (i * 25 // total) + "░" * (25 - i * 25 // total)
                print(f"Progress: [{progress}] {i * 100 // total}%")
                if i < total:
                    cont = input("   Press Enter to continue (or 'q' to stop): ")
                    if cont.lower() == 'q':
                        break

            again = input("\n🔁 Do you want to try another technique from this section? (y/n): ").strip().lower()
            if again == 'y':
                continue

            switch = input("\n📚 Do you want to switch to another section (A–H)? (y/n): ").strip().lower()
            if switch == 'y':
                from main import run_main_menu
                run_main_menu()
                return
            else:
                print("\n👋 Exiting the tool. Thank you!")
                return

        except ValueError:
            print("❌ Please enter a valid number.")

def get_intro(option):
    intros = {
        1: (
            "Radioisotope quantification is essential for measuring the activity of radioactive samples "
            "in research, diagnostics, and environmental monitoring. The choice of isotope depends on its emission type "
            "and the biological or chemical process being studied. Instruments like scintillation counters for β-emitters "
            "and gamma counters for γ-emitters allow precise detection. Calibration with standards ensures accurate "
            "quantification in units like becquerels (Bq) or curies (Ci). This technique forms the basis for many tracer "
            "and metabolic studies in molecular biology."
        ),
        2: (
            "Radioisotope incorporation techniques allow researchers to track specific molecules inside cells or tissues. "
            "By introducing radiolabeled precursors, such as ³²P-ATP for DNA synthesis, scientists can monitor their uptake "
            "and integration into biomolecules. After incubation, unincorporated isotopes are removed through thorough washing. "
            "The labeled molecules can then be analyzed using autoradiography or scintillation counting. "
            "This method is widely used in gene expression, metabolic pathway, and molecular turnover studies."
        ),
        3: (
            "Radioisotope imaging provides powerful tools for visualizing molecular and physiological processes in living systems. "
            "Techniques like PET (Positron Emission Tomography) and SPECT (Single Photon Emission Computed Tomography) allow "
            "dynamic tracking of radiolabeled molecules in real time. These imaging methods are often combined with CT or MRI "
            "to provide both functional and anatomical information. Targeted labeling of antibodies, ligands, or drugs enables "
            "precise localization of tissues, tumors, or biochemical pathways in both research and medical diagnostics."
        ),
        4: (
            "Radiation safety is a critical aspect of working with radioisotopes to protect researchers and the environment. "
            "Basic precautions include wearing lab coats, gloves, and personal dosimeters, and using appropriate shielding "
            "such as plexiglass for β-particles or lead for γ-rays. Work should be carried out in designated radiation areas "
            "with minimal exposure time and maximum distance from sources. Proper waste disposal, regular decontamination, "
            "and adherence to institutional and international safety regulations (e.g., IAEA, AERB) are mandatory for safe handling."
        )
    }
    return intros.get(option, "No description available.")
        

def get_workflow(option):
    workflows = {
        1: [
            "Select appropriate radioisotope (e.g., ³H, ¹⁴C, ³²P, ¹²⁵I) based on experimental needs.",
            "Use scintillation counters for β-emitters (³H, ¹⁴C) or gamma counters for γ-emitters (¹²⁵I).",
            "Calibrate instruments and measure background radiation to improve accuracy.",
            "Use standards and known concentrations to quantify isotope activity (in Bq or Ci)."
        ],
        2: [
            "Introduce radioisotopes via metabolic labeling (e.g., ³²P-ATP for DNA synthesis).",
            "Incubate cells/tissues with radiolabeled precursors for specific uptake.",
            "Wash thoroughly to remove unincorporated isotopes.",
            "Harvest cells or isolate molecules (RNA, protein) to analyze incorporation via autoradiography or scintillation counting."
        ],
        3: [
            "Use radiotracers in vivo or in vitro to visualize molecular processes.",
            "Techniques include PET (Positron Emission Tomography) and SPECT (Single Photon Emission Computed Tomography).",
            "Combine with CT/MRI for anatomical resolution.",
            "Label molecules (e.g., antibodies, ligands) with radioisotopes for targeted imaging of tissues or tumors."
        ],
        4: [
            "Always wear lab coats, gloves, and dosimeters when handling radioactive material.",
            "Use shielding (plexiglass for β, lead for γ emitters) and work in designated areas (radiation hoods or fume hoods).",
            "Minimize exposure time, maximize distance, and use protective barriers.",
            "Properly dispose of radioactive waste and decontaminate workspaces regularly.",
            "Follow institutional and regulatory body guidelines (e.g., IAEA, AERB)."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
