# enhanced_technique_a.py

def run():
    print("\n🧬 Molecular Biology & Recombinant DNA Methods")
    print("=" * 70)
    print("🔍 Explore foundational tools in gene manipulation and molecular analysis.\n")


    techniques = {
        1: ("Isolation and purification of RNA, DNA (genomic and plasmid), and proteins",
            "⭐⭐☆☆☆ Beginner | ⏱️ 2-4 hours | 💰 $"),
        2: ("Analysis of RNA, DNA and proteins by one- and two-dimensional gel electrophoresis, Isoelectric focusing gels",
            "⭐⭐☆☆☆ Beginner | ⏱️ 3-6 hours | 💰 $"),
        3: ("Molecular cloning of DNA or RNA fragments in bacterial and eukaryotic systems",
            "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-3 days | 💰 $$"),
        4: ("Expression of recombinant proteins using bacterial, animal and plant vectors",
            "⭐⭐⭐⭐☆ Advanced | ⏱️ 3-5 days | 💰 $$$"),
        5: ("Isolation of specific nucleic acid sequences",
            "⭐⭐⭐☆☆ Intermediate | ⏱️ 4-8 hours | 💰 $$"),
        6: ("Generation of genomic and cDNA libraries in plasmid, phage, cosmid, BAC and YAC vectors",
            "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-2 weeks | 💰 $$$"),
        7: ("In vitro mutagenesis and deletion techniques, gene knock-out in bacterial and eukaryotic organisms",
            "⭐⭐⭐⭐⭐ Expert | ⏱️ 1-3 weeks | 💰 $$$$"),
        8: ("Protein sequencing methods and detection of post-translational modifications",
            "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-2 days | 💰 $$$"),
        9: ("DNA sequencing methods and genome sequencing strategies",
            "⭐⭐⭐☆☆ Intermediate | ⏱️ 1-3 days | 💰 $$"),
        10: ("Methods for gene expression analysis at RNA and protein levels, including microarray-based techniques",
             "⭐⭐⭐⭐☆ Advanced | ⏱️ 2-5 days | 💰 $$$"),
        11: ("Isolation, separation and analysis of carbohydrate and lipid molecules",
             "⭐⭐⭐☆☆ Intermediate | ⏱️ 4-8 hours | 💰 $$"),
        12: ("RFLP, RAPD and AFLP techniques",
             "⭐⭐☆☆☆ Beginner | ⏱️ 1-2 days | 💰 $")
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
            "This technique is essential for obtaining high-quality nucleic acids and proteins, "
            "which form the foundation for numerous downstream applications. The integrity and "
            "purity of these biomolecules are crucial for ensuring reliable experimental results. "
            "It involves careful extraction and purification steps to minimize degradation or contamination. "
            "Applications include cloning, sequencing, and detailed protein analysis in functional studies."
        ),
        2: (
            "Electrophoretic methods help separate biomolecules by size or charge, making them vital "
            "for analyzing molecular composition. They allow researchers to assess purity, detect "
            "variations in expression, and confirm the presence of target molecules. By using gel or "
            "capillary formats, these techniques can resolve complex mixtures. They are also widely used "
            "in diagnostics, research, and comparative studies of gene or protein profiles."
        ),
        3: (
            "Cloning enables the amplification of genetic material, allowing scientists to generate "
            "multiple copies for study or manipulation. It plays a central role in genetic engineering, "
            "synthetic biology, and the production of recombinant proteins. The process involves inserting "
            "a DNA fragment into a vector, followed by propagation in a host system. Cloning supports "
            "gene function studies, mutant analysis, and large-scale genetic screening."
        ),
        4: (
            "Recombinant protein expression allows the production of specific proteins in controlled "
            "quantities, often using bacterial, yeast, insect, or mammalian systems. This technique is "
            "essential for structural biology, drug development, and functional assays. It involves "
            "introducing the gene of interest into an expression vector, followed by host cell cultivation. "
            "Purified recombinant proteins are used in research, therapeutics, and industrial applications."
        ),
        5: (
            "Specific sequence isolation is performed to retrieve desired DNA fragments from a complex "
            "genomic mixture. It is a critical step in cloning, gene identification, and targeted "
            "amplification techniques such as PCR. This process ensures that only the required region "
            "is studied, reducing background noise in experiments. It forms the basis for downstream "
            "sequencing, functional studies, and genetic diagnostics."
        ),
        6: (
            "Library generation involves creating a collection of genetic material that represents the "
            "entire genome or transcriptome of an organism. These libraries can be screened for genes "
            "of interest, used for sequencing projects, or studied to understand genetic diversity. "
            "They are essential for large-scale genomics, drug discovery, and functional annotation. "
            "The diversity of a library ensures a comprehensive resource for biological research."
        ),
        7: (
            "Targeted genetic modification techniques enable precise changes in the genome to study "
            "gene function or create specific phenotypes. This includes methods like CRISPR, TALENs, "
            "and site-directed mutagenesis. These approaches are essential for functional genomics, "
            "disease modeling, and the development of genetically engineered organisms. They allow "
            "scientists to investigate biological pathways with high specificity."
        ),
        8: (
            "Studying post-translational modifications and amino acid sequences provides critical "
            "insights into protein structure and function. These modifications influence stability, "
            "activity, localization, and interaction networks. Techniques such as mass spectrometry "
            "and peptide mapping are often employed for detailed analysis. Understanding protein "
            "modifications aids in drug design and biomarker discovery."
        ),
        9: (
            "DNA sequencing determines the exact order of nucleotides in a DNA molecule, providing "
            "essential data for gene identification, mutation detection, and evolutionary studies. "
            "Modern high-throughput sequencing methods allow rapid and large-scale analysis of genomes. "
            "It plays a crucial role in diagnostics, personalized medicine, and biodiversity research. "
            "Sequence data forms the basis for bioinformatics-driven biological insights."
        ),
        10: (
            "Gene expression analysis reveals how genes are regulated and expressed under different "
            "conditions. It helps uncover disease mechanisms, treatment responses, and developmental "
            "pathways. Techniques such as qPCR, RNA-Seq, and microarrays are commonly used. This "
            "information guides drug target identification and biomarker discovery. Understanding gene "
            "expression patterns is central to systems biology."
        ),
        11: (
            "Characterizing carbohydrates and lipids is key to understanding their roles in metabolism, "
            "cell structure, and signaling. These biomolecules influence membrane composition, energy "
            "storage, and communication between cells. Analytical methods like chromatography and "
            "mass spectrometry are used for detailed profiling. Insights into these molecules aid in "
            "nutrition science, disease research, and biotechnology applications."
        ),
        12: (
            "Molecular marker techniques are used to detect specific genetic variations, supporting "
            "studies in genetic mapping, biodiversity, and evolutionary biology. They include methods "
            "such as RFLP, AFLP, SSR, and SNP analysis. These approaches help identify species, track "
            "heritage, and assess population genetics. Molecular markers are widely used in agriculture, "
            "conservation, and forensic science."
        )
    }
    return intros.get(option, "No description available.")


def get_workflow(option):
    """Original workflow function with enhancements"""
    workflows = {
        1: [
            "Collect fresh tissue or cell pellet and keep on ice.",
            "Add lysis buffer (e.g., guanidinium isothiocyanate for RNA; SDS + Proteinase K for DNA).",
            "Homogenize the sample (e.g., vortexing, pipetting, or mechanical disruption).",
            "For RNA: Add phenol:chloroform and centrifuge; collect aqueous phase.",
            "For DNA: Use silica column or alcohol precipitation to bind and isolate DNA.",
            "Wash with ethanol-based buffer to remove impurities.",
            "Elute purified RNA/DNA in nuclease-free water or TE buffer.",
            "Quantify using NanoDrop/Qubit; check integrity via agarose gel or Bioanalyzer.",
            "For protein: Lyse cells, centrifuge to collect supernatant, and purify using affinity or column chromatography."
        ],
        2: [
            "Prepare agarose gel (0.8–2%) in TAE or TBE buffer for nucleic acids.",
            "Add staining dye (e.g., ethidium bromide or SYBR Safe).",
            "Load DNA/RNA with loading dye into wells; use ladder for size reference.",
            "Run the gel at 80–120V; visualize bands using UV or blue-light transilluminator.",
            "For proteins: Prepare SDS-PAGE gel for denatured separation or native-PAGE.",
            "Load protein samples with buffer, run at constant current.",
            "Stain gel with Coomassie Blue or silver stain to visualize bands.",
            "For isoelectric focusing: Use pH gradient gel and focus proteins by pI.",
            "Optional: Use 2D gels combining IEF and SDS-PAGE."
        ],
        3: [
            "Design primers for gene of interest and amplify using high-fidelity PCR.",
            "Digest PCR product and vector with compatible restriction enzymes.",
            "Purify digested products using gel extraction or column-based kits.",
            "Ligate insert and vector using T4 DNA ligase at 16°C overnight or 25°C for 1 hour.",
            "Transform competent cells (e.g., E. coli DH5α) with ligation product.",
            "Plate on selective media (e.g., ampicillin, kanamycin) and incubate overnight.",
            "Screen colonies using colony PCR, digestion, or blue-white screening.",
            "Confirm correct clone via plasmid prep and Sanger sequencing.",
            "Use confirmed clones for expression or downstream applications."
        ],
        4: [
            "Clone target gene into an expression vector with appropriate promoter (e.g., T7 for bacteria).",
            "Transform the vector into expression host (E. coli, HEK293, or plant cells).",
            "Induce protein expression (e.g., IPTG in bacteria, transient expression in plants).",
            "Harvest cells and lyse using mechanical or chemical methods.",
            "Purify recombinant protein using affinity chromatography (e.g., His-tag, GST-tag).",
            "Analyze expression levels via SDS-PAGE and Western blot.",
            "Store proteins at appropriate conditions (with protease inhibitors if needed)."
        ],
        5: [
            "Design probe or primers specific to your nucleic acid sequence.",
            "Use PCR or hybridization methods to isolate or amplify sequence.",
            "Use capture methods (e.g., biotinylated probes with magnetic beads) to pull down targets.",
            "Validate isolated sequences by gel electrophoresis or qPCR.",
            "Optional: Clone or sequence the isolated product for confirmation."
        ],
        6: [
            "Isolate high-quality mRNA or genomic DNA.",
            "Fragment DNA (via sonication or enzymatic digestion) for library construction.",
            "Ligate into vectors (plasmid, phage, BAC, YAC, cosmid).",
            "Transform host cells and plate on selective media.",
            "Screen colonies and store library as glycerol stocks.",
            "For cDNA: Reverse transcribe mRNA to cDNA, then ligate into cloning vectors.",
            "Quantify and validate library using PCR or sequencing."
        ],
        7: [
            "Design primers or synthetic constructs for point mutation or deletion.",
            "Use site-directed mutagenesis kit or overlapping PCR strategy.",
            "Transform into competent bacterial or eukaryotic cells.",
            "Select mutants using antibiotics or markers.",
            "Confirm mutagenesis via sequencing.",
            "For knockouts: Use CRISPR/Cas9 or homologous recombination.",
            "Screen for knockouts via PCR and phenotype."
        ],
        8: [
            "Purify protein of interest using chromatography or precipitation.",
            "Digest protein with specific proteases (e.g., trypsin).",
            "Analyze fragments using Edman degradation or mass spectrometry.",
            "Detect post-translational modifications (PTMs) via specific stains or MS.",
            "Map PTMs using phospho-specific antibodies or LC-MS/MS analysis."
        ],
        9: [
            "Choose suitable DNA sequencing platform (Sanger, NGS).",
            "For Sanger: Prepare template DNA and sequencing primers.",
            "Perform cycle sequencing with labeled ddNTPs.",
            "Run on capillary electrophoresis platform.",
            "For NGS: Construct DNA libraries, attach adaptors, and perform bridge amplification.",
            "Run sequencing on Illumina or similar platforms.",
            "Analyze raw data using bioinformatics pipelines."
        ],
        10: [
            "Extract RNA and synthesize cDNA using reverse transcriptase.",
            "Quantify expression using qRT-PCR or Northern blot.",
            "For protein expression: Use Western blot, ELISA, or mass spectrometry.",
            "For large-scale analysis: Use microarray or RNA-Seq.",
            "Analyze differential expression using software tools (e.g., DESeq2, limma, edgeR)."
        ],
        11: [
            "Extract samples using appropriate solvents (methanol/chloroform for lipids).",
            "Purify compounds using column chromatography or TLC.",
            "Analyze structure using NMR, MS, or enzymatic assays.",
            "Quantify using colorimetric assays or HPLC.",
            "Validate results with standards and controls."
        ],
        12: [
            "Extract high-quality genomic DNA from samples.",
            "For RFLP: Digest DNA with restriction enzymes and run on gel.",
            "For RAPD: Use random primers in PCR amplification.",
            "For AFLP: Digest DNA, ligate adaptors, and perform selective PCR.",
            "Analyze banding patterns for genetic diversity or mapping."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
