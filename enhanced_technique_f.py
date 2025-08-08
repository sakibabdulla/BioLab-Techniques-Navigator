# enhanced_technique_f.py

def run():
    print("\n🔬 Microscopic Techniques")
    print("=" * 70)
    print("🔍 Techniques for visualizing cells, tissues, and molecular structures.\n")

    techniques = {
        1: ("Bright-field and phase-contrast microscopy", "⭐⭐☆☆☆ Beginner | ⏱️ 1-2 hours | 💰 $"),
        2: ("Fluorescence microscopy and imaging", "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-3 hours | 💰 $$"),
        3: ("Confocal microscopy for 3D visualization", "⭐⭐⭐⭐☆ Advanced | ⏱️ 3-5 hours | 💰 $$$"),
        4: ("Electron microscopy (SEM and TEM)", "⭐⭐⭐⭐⭐ Expert | ⏱️ 1-2 days | 💰 $$$$"),
        5: ("Live-cell imaging and time-lapse microscopy", "⭐⭐⭐⭐☆ Advanced | ⏱️ 4-6 hours | 💰 $$$")
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
            "Basic light microscopy is one of the most widely used tools for observing biological specimens. "
            "It allows visualization of cells, tissues, and microorganisms by magnifying them through a series of lenses. "
            "Samples are typically prepared on glass slides and may be stained to enhance contrast. "
            "Depending on the sample type, different imaging modes such as bright-field, phase-contrast, or fluorescence can be applied. "
            "This technique is essential for teaching, research, and diagnostic applications."
        ),
        2: (
            "Resolution in microscopy determines the smallest details that can be distinguished in an image. "
            "It depends on factors such as the wavelength of light or electrons used and the numerical aperture (NA) of the objective lens. "
            "Light microscopes typically achieve ~200 nm resolution, while confocal microscopy improves this with optical sectioning. "
            "Electron microscopy offers much higher resolution, reaching sub-nanometer scales for ultrastructural studies. "
            "Understanding resolution is critical for selecting the appropriate imaging method for a given research question."
        ),
        3: (
            "Live-cell imaging enables observation of biological processes as they occur in real time. "
            "Specialized microscopes equipped with environmental control chambers maintain cells under physiological conditions. "
            "Fluorescent tags such as GFP allow specific molecules or organelles to be tracked dynamically. "
            "Minimizing phototoxicity and photobleaching is important for preserving cell health during imaging. "
            "This technique is invaluable for studying cell division, signaling pathways, and intracellular transport."
        ),
        4: (
            "Scanning Electron Microscopy (SEM) is a high-resolution technique for examining surface structures. "
            "Samples are coated with a conductive material and scanned with a focused electron beam. "
            "Secondary electrons emitted from the sample surface produce detailed, three-dimensional-like images. "
            "SEM is widely used in biology, materials science, and nanotechnology to analyze topography and morphology. "
            "Its ability to provide surface detail at the nanometer scale makes it a powerful characterization tool."
        ),
        5: (
            "Transmission Electron Microscopy (TEM) is used to visualize internal structures of cells and materials at atomic resolution. "
            "Samples must be ultra-thin and stained with heavy metals to enhance contrast. "
            "An electron beam passes through the specimen, producing highly detailed two-dimensional images. "
            "TEM is essential for studying viruses, organelles, and macromolecular complexes. "
            "Its unparalleled resolution makes it a cornerstone technique in structural biology and nanoscience."
        ),
        6: (
            "Sample preparation is a critical step in microscopy that ensures high-quality imaging and preservation of structures. "
            "Processes such as fixation, dehydration, staining, and embedding stabilize biological materials for observation. "
            "Chemical fixatives preserve fine details, while stains or heavy metals improve contrast. "
            "Embedding in resin supports delicate specimens for ultrathin sectioning. "
            "Well-prepared samples are essential for obtaining accurate and reproducible microscopy results."
        ),
        7: (
            "Freeze-fracture microscopy is a specialized method for studying the organization of membranes and other internal structures. "
            "Samples are rapidly frozen to preserve their native state, then fractured to reveal internal planes. "
            "Metal shadowing and electron microscopy are used to visualize the fracture surfaces. "
            "This technique provides unique insights into membrane architecture and macromolecular arrangements. "
            "It is particularly valuable for examining cell membranes and structural complexes in situ."
        ),
        8: (
            "Image analysis in microscopy transforms raw data into quantitative and interpretable results. "
            "Software tools such as ImageJ and Fiji allow adjustments for contrast, noise, and color mapping. "
            "Advanced analysis includes co-localization studies, 3D reconstruction, and deconvolution for improved clarity. "
            "Post-processing enhances visualization and enables accurate measurement of structures. "
            "These tools are critical for extracting meaningful biological insights from microscopy data."
        )
    }
    return intros.get(option, "No description available.")


def get_workflow(option):
    workflows = {
        1: [
            "Prepare a thin sample on a clean glass slide and cover with a coverslip.",
            "Use appropriate stains (e.g., methylene blue, crystal violet) to enhance contrast.",
            "Place slide on stage and focus with low to high magnification objectives.",
            "Use bright-field, phase-contrast, or fluorescence microscopy depending on sample."
        ],
        2: [
            "Understand that resolution = λ / (2 * NA), where NA = numerical aperture.",
            "Light Microscopes: ~200 nm resolution.",
            "Confocal Microscopes: ~150 nm with optical sectioning.",
            "Electron Microscopes: TEM ~0.2 nm; SEM ~1–5 nm resolution."
        ],
        3: [
            "Use temperature-controlled chambers to maintain physiological conditions.",
            "Apply fluorescent protein tags (e.g., GFP) for real-time visualization.",
            "Minimize phototoxicity and bleaching using short exposures.",
            "Record time-lapse images for dynamic observations."
        ],
        4: [
            "Fix the specimen and coat it with conductive material (e.g., gold).",
            "Place sample inside vacuum chamber of SEM.",
            "Scan surface with electron beam and detect secondary electrons.",
            "Visualize surface topology in high detail (3D appearance)."
        ],
        5: [
            "Fix, dehydrate, and embed specimen in resin.",
            "Cut ultra-thin sections (~70–90 nm) using an ultramicrotome.",
            "Stain with heavy metals (e.g., uranyl acetate, lead citrate).",
            "Observe internal structures at atomic resolution using TEM."
        ],
        6: [
            "Chemical fixation: Use agents like glutaraldehyde or formaldehyde.",
            "Dehydration: Replace water with ethanol or acetone gradually.",
            "Staining: Use heavy metals for EM contrast or dyes for LM.",
            "Embedding: Resin embedding stabilizes specimen for sectioning."
        ],
        7: [
            "Rapidly freeze biological sample to preserve native structure.",
            "Fracture frozen sample under vacuum to reveal internal planes.",
            "Etch surface by sublimation and coat with metal shadowing.",
            "Examine fracture surface using TEM or SEM for subcellular detail."
        ],
        8: [
            "Use software (e.g., ImageJ, Fiji) to analyze images post-capture.",
            "Apply contrast enhancement, noise reduction, and pseudo-coloring.",
            "Quantify intensity, co-localization, and 3D reconstruction if needed.",
            "Use deconvolution or stitching tools for improved clarity."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
