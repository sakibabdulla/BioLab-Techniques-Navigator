# enhanced_technique_b.py

def run():
    print("\n🧪 Histochemical & Immunotechniques")
    print("=" * 70)
    print("🔍 Techniques for detecting, visualizing, and localizing biomolecules in tissues.\n")

    techniques = {
        1: ("Antibody Generation", "⭐⭐⭐☆☆ Intermediate | ⏱️ 1-2 weeks | 💰 $$$"),
        2: ("ELISA", "⭐⭐☆☆☆ Beginner | ⏱️ 2-6 hours | 💰 $$"),
        3: ("RIA", "⭐⭐⭐☆☆ Intermediate | ⏱️ 1 day | 💰 $$$"),
        4: ("Western Blot", "⭐⭐⭐☆☆ Intermediate | ⏱️ 1-2 days | 💰 $$"),
        5: ("Immunoprecipitation", "⭐⭐⭐☆☆ Intermediate | ⏱️ 4-8 hours | 💰 $$"),
        6: ("Flow Cytometry", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1 day | 💰 $$$"),
        7: ("Immunofluorescence Microscopy", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-2 days | 💰 $$$"),
        8: ("FISH and GISH", "⭐⭐⭐⭐⭐ Expert | ⏱️ 2-3 days | 💰 $$$$")
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
            "Antibody generation is a process used to produce specific antibodies against a target "
            "antigen, such as a protein or peptide. The antigen is often modified or conjugated to "
            "a carrier protein to enhance its immunogenicity. Once injected into a host animal, "
            "the immune system produces antibodies against the antigen. These antibodies are later "
            "collected, purified, and validated for use in applications such as diagnostics, "
            "research assays, or therapeutic development."
        ),
        2: (
            "ELISA (Enzyme-Linked Immunosorbent Assay) is a widely used method for detecting and "
            "quantifying specific proteins or antigens in a sample. It relies on antigen–antibody "
            "binding and enzyme-driven color development for signal detection. This technique is "
            "highly sensitive and can measure low concentrations of targets in biological fluids. "
            "ELISA is essential for diagnostics, disease monitoring, and research applications. "
            "Its versatility includes formats like direct, indirect, sandwich, and competitive ELISA."
        ),
        3: (
            "RIA (Radioimmunoassay) is a highly sensitive technique for quantifying small amounts "
            "of antigens or hormones using radioactively labeled molecules. It works on the principle "
            "of competition between labeled and unlabeled antigens for binding to a specific antibody. "
            "The bound and free fractions are separated, and radioactivity is measured to determine "
            "concentration. Despite its precision, RIA use has declined due to safety concerns with "
            "radioisotopes, being replaced in many labs by ELISA."
        ),
        4: (
            "Western blotting is a gold-standard method for detecting specific proteins within a complex "
            "sample. It involves separating proteins by SDS-PAGE, transferring them to a membrane, and "
            "probing with specific antibodies. The bound antibodies are visualized through chemiluminescence "
            "or fluorescence. This technique allows both qualitative and semi-quantitative protein analysis. "
            "It is extensively used in molecular biology, diagnostics, and biomedical research."
        ),
        5: (
            "Immunoprecipitation is a targeted protein isolation method using antibodies bound to a "
            "solid support such as Protein A/G beads. The antibody captures the protein of interest, "
            "along with any bound molecules, from a complex mixture. After washing to remove nonspecific "
            "binding, the target protein is eluted and analyzed, often by Western blot or mass spectrometry. "
            "It is a key technique for studying protein–protein interactions, signaling pathways, and "
            "complex formation."
        ),
        6: (
            "Flow cytometry is a powerful analytical technique for measuring physical and chemical "
            "characteristics of cells or particles in suspension. It uses laser-based detection to "
            "analyze fluorescence from antibody-labeled cells. This allows high-throughput multiparametric "
            "analysis, including cell size, complexity, and marker expression. Flow cytometry is widely "
            "used in immunology, cancer research, and clinical diagnostics, including cell sorting (FACS)."
        ),
        7: (
            "Immunofluorescence microscopy is used to visualize the localization of proteins or "
            "other antigens within cells or tissues. Antibodies conjugated to fluorescent dyes bind "
            "specifically to the target molecule. This enables visualization under a fluorescence "
            "microscope, often with counterstaining to highlight nuclei or other structures. The method "
            "is valuable for studying cellular organization, protein localization, and changes under "
            "different experimental conditions."
        ),
        8: (
            "FISH (Fluorescence In Situ Hybridization) and GISH (Genomic In Situ Hybridization) are "
            "molecular cytogenetic techniques used to detect specific DNA sequences on chromosomes. "
            "FISH uses fluorescently labeled DNA probes to visualize gene locations or structural "
            "chromosome abnormalities, while GISH uses whole-genomic DNA as a probe to distinguish "
            "between genomes in hybrids. These techniques are vital in genetics, evolutionary biology, "
            "and clinical diagnostics for identifying chromosomal rearrangements or genome composition."
        )
    }
    return intros.get(option, "No description available.")



def get_workflow(option):
    """Return workflow steps for each technique"""
    workflows = {  # Fixed variable name
        1: [ 
            "Identify and select the target antigen (protein or peptide).",
            "Conjugate antigen with a carrier protein (e.g., KLH) if it's a small peptide.",
            "Inject antigen into host animal (e.g., rabbit, mouse) with an adjuvant (e.g., Freund's).",
            "Administer booster injections at regular intervals.",
            "Collect serum periodically to assess antibody production.",
            "Purify antibodies using affinity chromatography (Protein A/G).",
            "Validate antibody specificity using ELISA, Western blot, or immunostaining."
        ],
        2: [  
            "Coat ELISA plate wells with antigen (incubate overnight or 2 hours).",
            "Block non-specific binding with BSA or milk solution.",
            "Add primary antibody and incubate (1–2 hours).",
            "Wash wells with PBS-Tween to remove unbound antibody.",
            "Add enzyme-linked secondary antibody and incubate.",
            "Add substrate (e.g., TMB), allow color development.",
            "Stop reaction and measure absorbance (usually at 450 nm)."
        ],
        3: [  
            "Label antigen or antibody with a radioactive isotope (commonly Iodine-125).",
            "Incubate labeled antigen with specific antibody.",
            "Add sample with unlabeled antigen to compete binding.",
            "Separate bound from free antigens (e.g., via filtration or precipitation).",
            "Measure radioactivity using a gamma counter.",
            "Compare with standard curve to quantify antigen concentration."
        ],
        4: [  
            "Extract protein from cells or tissues using lysis buffer.",
            "Separate proteins using SDS-PAGE.",
            "Transfer proteins to membrane (e.g., PVDF).",
            "Block non-specific sites with milk or BSA.",
            "Incubate with primary antibody specific to the target.",
            "Wash and add HRP- or fluorophore-conjugated secondary antibody.",
            "Visualize using chemiluminescence or fluorescence imaging."
        ],
        5: [
            "Lyse cells under gentle, non-denaturing conditions.",
            "Add antibody to lysate to bind the target protein.",
            "Capture complexes with Protein A/G beads.",
            "Wash beads to remove unbound proteins.",
            "Elute bound proteins by boiling in SDS buffer.",
            "Analyze by SDS-PAGE and Western blot."
        ],
        6: [  
            "Prepare single-cell suspension from blood/tissue.",
            "Stain cells with fluorophore-conjugated antibodies.",
            "Wash and resuspend in FACS buffer.",
            "Run sample through flow cytometer.",
            "Analyze data for marker expression using software."
        ],
        7: [  
            "Fix cells or tissue with paraformaldehyde.",
            "Permeabilize if targeting intracellular proteins.",
            "Block with serum to prevent non-specific binding.",
            "Incubate with primary antibody.",
            "Add fluorophore-conjugated secondary antibody.",
            "Counterstain (e.g., DAPI for nuclei).",
            "Mount and observe under fluorescence microscope."
        ],
        8: [  
            "Prepare chromosome/tissue spread and fix on slide.",
            "Denature DNA with heat or alkaline solution.",
            "Apply fluorescent-labeled DNA probe and hybridize.",
            "Wash off unbound probe under stringent conditions.",
            "Counterstain with DAPI.",
            "Mount and visualize using fluorescence microscopy.",
            "For GISH, use labeled whole-genomic DNA as probe."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
