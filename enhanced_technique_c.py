# enhanced_technique_c.py


def run():
    print("\n🧪 Biophysical Methods")
    print("=" * 70)
    print("🔍 Tools and techniques used to study physical properties of biological systems.\n")

    techniques = {
        1: ("UV, visible and fluorescence spectroscopy", "⭐⭐☆☆☆ Beginner | ⏱️ 2-4 hours | 💰 $"),
        2: ("Circular dichroism", "⭐⭐⭐☆☆ Intermediate | ⏱️ 3-5 hours | 💰 $$"),
        3: ("Chromatographic methods for macromolecular separation", "⭐⭐⭐☆☆ Intermediate | ⏱️ 5-8 hours | 💰 $$"),
        4: ("Analysis using NMR, X-ray, light and electron diffraction", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-3 days | 💰 $$$$"),
        5: ("Molecular interaction analysis using surface plasmon resonance", "⭐⭐⭐⭐☆ Advanced | ⏱️ 4-6 hours | 💰 $$$"),
        6: ("Isothermal titration calorimetry", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1 day | 💰 $$$"),
        7: ("Differential scanning calorimetry", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1 day | 💰 $$$")
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
            "UV-Vis spectroscopy is a widely used analytical method for measuring the absorbance of "
            "molecules across the ultraviolet and visible light spectrum. It is based on the principle "
            "that molecules absorb specific wavelengths depending on their electronic structure. "
            "This technique is used to determine concentration, identify compounds, and study reaction "
            "kinetics. It is non-destructive and applicable to a wide range of chemical and biological "
            "samples, making it an essential tool in both research and industry."
        ),
        2: (
            "Fluorescence spectroscopy measures the emission of light by molecules after excitation "
            "with a specific wavelength. It is highly sensitive and can detect minute quantities of "
            "fluorophores in a sample. This technique is widely used for studying biomolecular "
            "interactions, protein folding, and environmental sensing. Fluorescence measurements can "
            "be steady-state or time-resolved, allowing both quantitative and qualitative analysis. "
            "Careful sample handling is crucial to avoid photobleaching or quenching effects."
        ),
        3: (
            "Circular Dichroism (CD) spectroscopy is a powerful technique for studying the secondary "
            "and tertiary structures of chiral biomolecules, especially proteins and nucleic acids. "
            "It measures the differential absorption of left- and right-circularly polarized light. "
            "Far-UV CD provides information on α-helices and β-sheets, while near-UV CD reveals tertiary "
            "folding and environment of aromatic residues. CD is widely used in protein folding studies, "
            "structural comparison, and stability analysis."
        ),
        4: (
            "Nuclear Magnetic Resonance (NMR) spectroscopy is a non-destructive technique for determining "
            "the structure, dynamics, and interactions of molecules. It detects the magnetic properties "
            "of atomic nuclei, most commonly hydrogen (1H) and carbon (13C). NMR provides detailed "
            "chemical shift information for structure elucidation in solution. It is widely used in "
            "organic chemistry, biochemistry, and drug design. Advanced 2D and 3D NMR experiments enable "
            "complex biomolecular structural studies."
        ),
        5: (
            "Electron Paramagnetic Resonance (EPR) spectroscopy, also known as ESR, is a technique for "
            "studying species with unpaired electrons, such as free radicals and transition metal complexes. "
            "It measures transitions between electron spin states in a magnetic field using microwave radiation. "
            "EPR provides information on g-values, hyperfine splitting, and the electronic environment. "
            "It is widely applied in materials science, bioinorganic chemistry, and radical reaction studies. "
            "The technique is extremely sensitive to the presence of paramagnetic species."
        ),
        6: (
            "X-ray crystallography is the primary method for determining the three-dimensional structure "
            "of biomolecules at atomic resolution. It involves diffracting X-rays through a crystalline "
            "sample and analyzing the resulting patterns to generate an electron density map. "
            "From this, an atomic model of the molecule is built and refined. This method has been "
            "instrumental in structural biology, drug design, and enzyme mechanism studies. "
            "High-quality crystals are essential for accurate results."
        ),
        7: (
            "Light scattering techniques, including Dynamic Light Scattering (DLS) and Static Light Scattering (SLS), "
            "are used to measure the size, distribution, and molecular weight of particles or macromolecules in solution. "
            "DLS determines hydrodynamic radius from fluctuations in scattered light, while SLS measures absolute molecular weight. "
            "These methods are non-destructive and require minimal sample preparation. They are widely used in protein aggregation studies, "
            "nanoparticle characterization, and polymer analysis."
        ),
        8: (
            "Mass spectrometry (MS) is a highly sensitive analytical technique that measures the mass-to-charge "
            "ratio of ionized molecules. It enables precise identification of compounds, quantification, and "
            "structural analysis. Common ionization methods include Electrospray Ionization (ESI) and Matrix-Assisted "
            "Laser Desorption/Ionization (MALDI). Tandem MS (MS/MS) provides fragmentation patterns for peptide sequencing "
            "and metabolite identification. MS is essential in proteomics, metabolomics, and drug discovery."
        ),
        9: (
            "Surface Plasmon Resonance (SPR) is a label-free, real-time method for studying biomolecular interactions. "
            "It detects changes in the refractive index near a sensor surface as molecules bind or dissociate. "
            "SPR provides kinetic parameters such as association and dissociation rates, as well as affinity constants. "
            "It is widely used in drug screening, antibody characterization, and binding mechanism studies. "
            "The technique is highly sensitive and does not require labeling of analytes."
        )
    }
    return intros.get(option, "No description available.")


def get_workflow(option):
    workflows = {
        1: ["Prepare sample solution in appropriate solvent (e.g., water, ethanol).",
            "Turn on spectrophotometer and allow it to warm up (if required).",
            "Blank the instrument using the solvent to calibrate baseline absorbance.",
            "Place the sample in a quartz or plastic cuvette.",
            "Scan absorbance across desired wavelength range (typically 200–800 nm).",
            "Record absorbance spectrum and analyze peak wavelengths for concentration or functional group analysis."],

        2: ["Dilute fluorescent sample to avoid quenching; protect from light.",
            "Calibrate spectrofluorometer using blank and standard (e.g., quinine sulfate).",
            "Excite the sample at a specific wavelength and record emission spectra.",
            "Analyze emission peaks for fluorophore identification or quantification.",
            "For time-resolved studies, measure fluorescence lifetime decay."],

        3: ["Prepare protein sample in buffer with minimal absorbance in far-UV (avoid chloride, phosphate).",
            "Load sample into CD cuvette (quartz, pathlength ~0.1 cm).",
            "Record far-UV CD spectrum (190–250 nm) for secondary structure.",
            "Optional: Record near-UV CD (250–320 nm) for tertiary structure.",
            "Analyze spectra using software to estimate α-helix, β-sheet content."],

        4: ["Dissolve sample in deuterated solvent (e.g., D2O, CDCl3).",
            "Transfer to NMR tube and cap properly.",
            "Place tube in NMR instrument; shim magnetic field for uniformity.",
            "Select 1H or 13C NMR experiment and start acquisition.",
            "Process data using Fourier transformation and assign chemical shifts.",
            "Optional: Perform 2D NMR (COSY, HSQC) for structure elucidation."],

        5: ["Prepare paramagnetic sample in suitable solvent.",
            "Load sample into EPR (ESR) tube.",
            "Insert into resonator cavity and adjust microwave frequency.",
            "Sweep magnetic field and detect resonance signal.",
            "Analyze g-values and hyperfine splitting for radical or metal ion information."],

        6: ["Crystallize purified biomolecule (e.g., protein, DNA).",
            "Mount crystal on X-ray diffractometer goniometer.",
            "Cool crystal to cryo-temperature (~100 K) to reduce radiation damage.",
            "Collect diffraction pattern by rotating crystal in X-ray beam.",
            "Process data to generate electron density map.",
            "Build atomic model using refinement software (e.g., Phenix, CCP4)."],

        7: ["Prepare monodisperse sample and filter to remove aggregates.",
            "Set up light scattering instrument (e.g., DLS, SLS).",
            "Insert cuvette and perform baseline correction.",
            "Measure scattered light intensity at multiple angles.",
            "Analyze hydrodynamic radius (DLS) or molecular weight (SLS)."],

        8: ["Dissolve/analyze sample in suitable buffer or solvent.",
            "Ionize molecules using appropriate technique (e.g., MALDI, ESI).",
            "Inject sample into mass spectrometer.",
            "Select ionization mode (positive/negative) and m/z range.",
            "Record mass spectrum and identify peaks.",
            "Perform MS/MS for peptide or metabolite sequencing."],

        9: ["Immobilize ligand on SPR sensor chip surface (e.g., via amine coupling).",
            "Prime the system with running buffer.",
            "Inject analyte over sensor surface at varying concentrations.",
            "Record changes in SPR angle (response units) in real-time.",
            "Analyze binding kinetics (association/dissociation rates) and affinity constants."]
    }
    return workflows.get(option, ["Workflow not available yet."])
