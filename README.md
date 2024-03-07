# CLBR Calculator

The CLBR Calculator is an interactive tool developed to provide insights into the potential outcomes of assisted reproductive technology (ART) treatments, specifically in vitro fertilization (IVF). It draws upon the research findings from the paper titled "The combined effect of BMI and age on ART outcomes", published in *Human Reproduction* journal, Volume 38, Issue 5, on May 1, 2023. The study, authored by Filipa Rafael, Maria Dias Rodrigues, Jose Bellver, Mariana Canelas-Pais, Nicolas Garrido, Juan A Garcia-Velasco, Sérgio Reis Soares, and Samuel Santos-Ribeiro, explores the interplay between a woman's body mass index (BMI), her age, and the outcomes of ART treatments. The paper can be accessed [here](https://academic.oup.com/humrep/article/38/5/886/7079091?utm_source=TrendMD&utm_campaign=Human_Reproduction_TrendMD_1&utm_medium=cpc).

The research highlights a critical consideration in the field of reproductive medicine: whether women with infertility and overweight/obesity should delay IVF treatment to first promote weight loss.

This interactive CLBR Calculator allows users to input their personal health information (such as weight, height, and age) and see how these factors might influence their cumulative live birth rates (CLBR) based on the study's findings.

## Live Version

Access a live instance of the CLBR Calculator at [clbrcalculator.med.up.pt](http://clbrcalculator.med.up.pt).

## Getting Started

To run the CLBR Calculator locally using Docker, ensure you have Docker installed on your system. This setup allows you to containerize the application, simplifying the deployment process and ensuring consistency across different environments.

### Prerequisites

- Docker
- Git (optional, for cloning the repository)
- Make (optional, for simplified Docker commands)

### Setup Instructions

1. **Clone the repository** (skip this step if you have the project files already):

    ```sh
    git clone https://github.com/marianacpais/clbr_calculator.git
    cd clbr-calculator
    ```

2. **Build and run the Docker image using Make**:

    The project includes a Makefile for convenience, which contains shorthand commands to simplify Docker operations. To build the Docker image and run it as a container, execute:

    ```sh
    make docker
    ```

    This command utilizes the `docker` target in the Makefile to build a Docker image named `clbrcalculator:alfa` and runs it as a container named `clbrcalculator`, making the application accessible at `localhost:8080`.

    If you prefer not to use Make, you can achieve the same result with the following Docker commands:

    ```sh
    docker build -t clbrcalculator:alfa .
    docker run --name clbrcalculator -d -p 8080:8080 clbrcalculator:alfa
    ```

3. **Access the application**:

    Open your web browser and go to `http://localhost:8080/` to start using the CLBR Calculator.

## How to Use

Simply enter the desired details, such as weight, height, date of birth, and the interval before potentially starting IVF treatment, to receive an estimated CLBR for that case along with guidance on how different factors may affect your results.

## Contributing

We welcome contributions from the community to enhance the calculator's functionality, improve user experience, or expand the research base it covers.

## License

This project is open source, available under the [MIT License](LICENSE.md).

---

*Disclaimer: The CLBR Calculator is intended for informational purposes only and is not a substitute for professional medical advice. Please consult a healthcare provider for personalized guidance.*
