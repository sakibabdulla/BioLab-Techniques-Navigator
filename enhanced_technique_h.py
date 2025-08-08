# enhanced_technique_h.py

def run():
    print("\n🌿 Methods in Field Biology")
    print("=" * 70)
    print("🔍 Techniques for studying organisms in their natural environments.\n")

    techniques = {
        1: ("Quadrat sampling for vegetation analysis", "⭐⭐☆☆☆ Beginner | ⏱️ 2-4 hours | 💰 $"),
        2: ("Mark-recapture method for population estimation", "⭐⭐⭐☆☆ Intermediate | ⏱️ 1-2 days | 💰 $$"),
        3: ("Radio telemetry tracking", "⭐⭐⭐⭐☆ Advanced | ⏱️ 1-3 days | 💰 $$$"),
        4: ("Transect and line intercept methods", "⭐⭐☆☆☆ Beginner | ⏱️ 2-5 hours | 💰 $"),
        5: ("Environmental sampling and biodiversity indexing", "⭐⭐⭐☆☆ Intermediate | ⏱️ 1 day | 💰 $$"),
        6: ("Remote sensing and drone surveys", "⭐⭐⭐⭐⭐ Expert | ⏱️ 2-4 days | 💰 $$$$")
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
            "Population surveys are conducted to estimate the abundance, density, and distribution of species in a given area. "
            "They involve systematically sampling plots or transects and recording the number of individuals. "
            "Such surveys are essential for monitoring wildlife populations, detecting changes over time, and informing conservation strategies. "
            "GPS mapping and statistical analyses help ensure accuracy and comparability between sites."
        ),
        2: (
            "Species identification is a fundamental step in ecological and biodiversity studies. "
            "It involves recognizing organisms based on morphological traits, sounds, or other distinctive features. "
            "Researchers often use field guides, dichotomous keys, or digital apps to aid identification. "
            "Accurate species ID is critical for ecological monitoring, conservation planning, and maintaining biodiversity records."
        ),
        3: (
            "Habitat assessment involves evaluating the environmental characteristics of an area to understand its suitability for various species. "
            "This includes analyzing soil type, moisture, temperature, and light availability, as well as mapping vegetation and landforms. "
            "Habitat assessments help identify critical areas for conservation, detect habitat degradation, and guide restoration projects."
        ),
        4: (
            "Biodiversity surveys aim to document the variety of life in a specific location. "
            "They record the richness, evenness, and abundance of species, often using standardized indices such as Shannon or Simpson. "
            "These surveys provide baseline data for ecological research, environmental impact assessments, and conservation programs."
        ),
        5: (
            "Behavioral observation is used to study the activities and interactions of animals in their natural environment. "
            "By minimizing disturbance and recording patterns such as feeding, mating, or aggression, researchers can gain insights into ecology and social structures. "
            "Ethograms and video recordings are often employed for systematic data collection."
        ),
        6: (
            "Mark-recapture is a method for estimating wildlife population sizes. "
            "Animals are safely captured, marked with tags or other identifiers, released, and then later recaptured. "
            "The proportion of marked to unmarked individuals in the second sample allows population estimation using models such as the Lincoln Index."
        ),
        7: (
            "Environmental sampling collects physical samples (e.g., water, air, soil) to analyze quality and detect pollutants or ecological changes. "
            "Measurements can also be taken in real-time using sensors and probes. "
            "This method is important for environmental monitoring, habitat assessment, and detecting trends over time."
        ),
        8: (
            "Field instrumentation involves the use of specialized tools to measure environmental parameters such as wind speed, soil pH, humidity, and temperature. "
            "Proper calibration and systematic recording are essential to ensure data accuracy. "
            "These measurements provide vital information for ecological research and environmental monitoring."
        )
    }
    return intros.get(option, "No description available.")


def get_workflow(option):
    workflows = {
        1: [
            "Define the study area and grid sampling zones using GPS or maps.",
            "Select sampling technique: quadrats, transects, or point counts.",
            "Record species number and abundance in selected plots.",
            "Analyze population structure, density, and diversity indices."
        ],
        2: [
            "Carry field guides or use mobile apps for real-time species identification.",
            "Observe morphological traits, call sounds, or other distinct features.",
            "Use dichotomous keys for taxonomic classification.",
            "Photograph and geo-tag specimens for records."
        ],
        3: [
            "Assess physical factors: soil type, moisture, temperature, light intensity.",
            "Identify dominant vegetation types and community structure.",
            "Map habitat zones using GIS tools or field sketches.",
            "Compare habitats across regions for ecological studies."
        ],
        4: [
            "List all observable flora and fauna within the sampling area.",
            "Use standardized biodiversity indices (e.g., Shannon, Simpson).",
            "Collect specimens only if ethically and legally permissible.",
            "Assess richness, evenness, and endemism."
        ],
        5: [
            "Select species and time period for observation.",
            "Minimize disturbance by using blinds or camouflage.",
            "Record behavior patterns (e.g., foraging, mating, aggression).",
            "Use ethograms or video recording tools."
        ],
        6: [
            "Capture individuals using traps or nets.",
            "Mark animals using safe, ethical tags or markers.",
            "Release animals and allow natural movement.",
            "Recapture and use Lincoln Index to estimate population size."
        ],
        7: [
            "Collect water, air, or soil samples for lab analysis.",
            "Use sensors or probes to monitor parameters in real-time.",
            "Log GPS coordinates and environmental conditions.",
            "Compare data over time to detect ecological changes."
        ],
        8: [
            "Use tools like anemometers, soil pH meters, hygrometers, etc.",
            "Calibrate instruments before use in the field.",
            "Record readings carefully and systematically.",
            "Maintain equipment and ensure accurate documentation."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
