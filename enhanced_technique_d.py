# enhanced_technique_d.py

def run():
    print("\n📊 Statistical Methods")
    print("=" * 70)
    print("🔍 Analytical approaches used to interpret biological data quantitatively.\n")

    techniques = {
        1: ("Descriptive statistics (mean, median, mode, SD, variance)", "⭐⭐☆☆☆ Beginner | ⏱️ 1-2 hours | 💰 $"),
        2: ("T-tests, ANOVA, chi-square test", "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-4 hours | 💰 $"),
        3: ("Correlation and regression analysis", "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-3 hours | 💰 $"),
        4: ("Probability distributions (binomial, normal, Poisson)", "⭐⭐⭐☆☆ Intermediate | ⏱️ 2-4 hours | 💰 $"),
        5: ("Non-parametric tests (Mann-Whitney, Kruskal-Wallis)", "⭐⭐⭐⭐☆ Advanced | ⏱️ 3-5 hours | 💰 $$"),
        6: ("Bioinformatics statistical tools (R, Bioconductor, Python libs)", "⭐⭐⭐⭐⭐ Expert | ⏱️ 1-3 days | 💰 $$")
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
            "Measures of central tendency and dispersion are fundamental in descriptive statistics. "
            "The mean, median, and mode summarize the center of a dataset, while variance, standard deviation, "
            "and range describe how spread out the data is. Together, they provide a snapshot of the dataset’s "
            "distribution. Visual tools like histograms and boxplots help in understanding these patterns. "
            "These metrics form the basis for more advanced statistical analysis."
        ),
        2: (
            "Probability distributions describe how values of a variable are expected to occur in a dataset. "
            "The binomial distribution models discrete success/failure events, the Poisson distribution describes "
            "rare events over time or space, and the normal distribution represents continuous variables with a bell-shaped curve. "
            "Understanding these distributions is essential for hypothesis testing, simulations, and predictive modeling. "
            "They allow researchers to make inferences about population behavior based on sample data."
        ),
        3: (
            "A sampling distribution is the distribution of a statistic, such as the mean, over repeated samples "
            "from the same population. The Central Limit Theorem explains why sample means tend to follow a normal distribution "
            "regardless of the population’s shape, given a large enough sample size. Sampling distributions are used to "
            "construct confidence intervals and estimate sampling errors. They are critical in determining the reliability "
            "and precision of statistical estimates."
        ),
        4: (
            "Statistical tests can be broadly divided into parametric and non-parametric methods. Parametric tests, such as t-tests "
            "and ANOVA, assume the data follows a normal distribution and meet certain conditions. Non-parametric tests, like "
            "Mann-Whitney U or Kruskal-Wallis, do not require such assumptions and are used for ordinal or non-normal data. "
            "Choosing the correct test depends on data type, sample size, and distribution characteristics. "
            "This choice directly affects the validity of research conclusions."
        ),
        5: (
            "Confidence intervals provide a range of values within which the true population parameter is expected to lie. "
            "They are calculated using the sample estimate, standard error, and the chosen confidence level (e.g., 95%). "
            "The width of the interval reflects the precision of the estimate—narrower intervals indicate higher precision. "
            "Confidence intervals are widely used to interpret experimental results in a probabilistic context. "
            "They complement p-values by providing more information about effect size and certainty."
        ),
        6: (
            "Hypothesis testing is a structured approach to making decisions based on data. It begins with defining a null hypothesis "
            "and an alternative hypothesis. The researcher then selects a significance level, calculates a test statistic, and determines "
            "a p-value. If the p-value is less than the significance level, the null hypothesis is rejected. "
            "This process is fundamental in scientific research to assess whether observed effects are statistically significant."
        ),
        7: (
            "Correlation and regression are key tools for analyzing relationships between variables. Correlation measures the strength "
            "and direction of an association, while regression models how one variable predicts another. Simple linear regression uses "
            "one predictor to estimate the dependent variable, producing coefficients and an R-squared value. "
            "These methods are widely used in science, economics, and engineering. "
            "However, correlation does not imply causation—careful interpretation is needed."
        ),
        8: (
            "The t-test is a statistical method for comparing the means of two groups to determine if they are significantly different. "
            "There are different types of t-tests, such as independent, paired, and one-sample, depending on the study design. "
            "They assume data is normally distributed and variances are equal. A p-value determines whether the observed difference "
            "is likely due to chance. T-tests are among the most commonly used inferential statistics in research."
        ),
        9: (
            "ANOVA (Analysis of Variance) is used to compare means across three or more groups to determine if at least one group differs significantly. "
            "It tests the hypothesis that all group means are equal while considering variability within and between groups. "
            "When ANOVA shows significant results, post hoc tests like Tukey’s are used to identify which groups differ. "
            "It assumes normality and homogeneity of variances. ANOVA is widely applied in experimental and observational studies."
        ),
        10: (
            "The Chi-square test is used to examine associations between categorical variables. It compares the observed frequencies "
            "in a contingency table to the frequencies expected if there were no association. A significant Chi-square statistic "
            "suggests a relationship between the variables. This test is non-parametric and does not require normal distribution assumptions. "
            "It is widely used in genetics, survey analysis, and epidemiology."
        ),
        11: (
            "Multivariate analysis involves examining more than two variables simultaneously to understand complex relationships. "
            "Principal Component Analysis (PCA) reduces data dimensionality while retaining most of the variance. Clustering groups "
            "similar observations together, and MANOVA or discriminant analysis compare multiple dependent variables across groups. "
            "These methods are essential for big data, pattern recognition, and classification problems. "
            "They allow researchers to uncover hidden structures in complex datasets."
        )
    }
    return intros.get(option, "No description available.")

def get_workflow(option):
    workflows = {
        1: [
            "Calculate mean, median, and mode to understand central tendency of the dataset.",
            "Use variance, standard deviation, and range to assess data dispersion.",
            "Visualize using boxplots and histograms for summary distribution insights."
        ],
        2: [
            "Binomial: Discrete distribution for success/failure (e.g., coin toss).",
            "Poisson: Models rare events per interval (e.g., mutations per gene).",
            "Normal: Bell-shaped curve for continuous variables, defined by mean and SD.",
            "Use these distributions to model and simulate experimental variability."
        ],
        3: [
            "Understand that a sampling distribution is the distribution of a statistic over many samples.",
            "Apply the Central Limit Theorem to justify normality of sample means.",
            "Use it to construct confidence intervals and estimate sampling errors."
        ],
        4: [
            "Parametric tests: Assume data follows a normal distribution (e.g., t-test, ANOVA).",
            "Non-parametric tests: Do not rely on distribution (e.g., Mann-Whitney U, Kruskal-Wallis).",
            "Select based on sample size, data distribution, and measurement scale."
        ],
        5: [
            "Define the desired confidence level (e.g., 95%).",
            "Calculate standard error and margin of error.",
            "Interpret confidence intervals in the context of the research question."
        ],
        6: [
            "Formulate null and alternative hypotheses clearly.",
            "Set significance level (typically 0.05).",
            "Use test statistic and p-value to accept or reject null hypothesis."
        ],
        7: [
            "Use correlation (Pearson/Spearman) to measure relationship between variables.",
            "Apply simple linear regression to model relationship between X and Y.",
            "Interpret regression coefficients and R-squared values."
        ],
        8: [
            "Select appropriate t-test based on study design.",
            "Check assumptions: normality and equal variances.",
            "Perform test using statistical software or formula, interpret p-value."
        ],
        9: [
            "Use ANOVA to compare means across multiple groups.",
            "Check assumptions: normality, homogeneity of variances.",
            "Use post hoc tests (e.g., Tukey) to pinpoint group differences."
        ],
        10: [
            "Create contingency table from categorical data.",
            "Compute expected frequencies and test statistic.",
            "Compare observed and expected values to evaluate association."
        ],
        11: [
            "Use PCA for dimensionality reduction in multivariate datasets.",
            "Apply clustering methods (e.g., k-means, hierarchical).",
            "Use MANOVA or discriminant analysis for group comparisons."
        ]
    }
    return workflows.get(option, ["Workflow not available yet."])
