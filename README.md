# Lakers 2025 Offseason Targets - LeBron and Luka Fits

### TL;DR

Models lineup fit for LeBron James and Luka Dončić using 10 years of NBA + Synergy playtype data.
Identifies ideal archetypes:

- Defensively versatile bigs for LeBron who can also cut on offense

- Scoring wings for Luka with an emphasized importance on spot up ability

Exploratory web app - <https://lakers-2025-team-fits.streamlit.app/>

### How to Run

1. Clone the repo
2. Create and activate a virtual environment
`python -m venv venv`
On Mac/Linux:
`source venv/bin/activate`
On Windows:
`venv\Scripts\activate` <br>
3. Install dependencies: `pip install -r dev-requirements.txt`
4. Run analysis in /scripts folder
- web_scraping/lakers_fits_web_scraping_stats
- lakers_fits_data_cleaning
- lakers_fits_lebron_analysis
- lakers_fits_luka_analysis
- lakers_fits_acquisition_recommendations

### Executive Summary

This analysis identifies optimal player targets for the Los Angeles Lakers to acquire in order to maximize lineup efficiency alongside LeBron James and Luka Dončić, assuming a scenario where both are on the same roster. Using ten years of lineup and playtype data sourced from the NBA and Synergy Sports APIs, the project models how specific player skills and positions have historically correlated with high net ratings when paired with either LeBron or Luka. The analysis recommends two key archetypes: defensive-oriented bigs who cut well for LeBron, and offensive-skilled wings who can spot up and post up for Luka. Top acquisition targets include Dean Wade, Mouhamed Gueye, Harrison Barnes, and Garrison Mathews with several alternative options identified based on contract flexibility and availability.

In addition to these target recommendations, you can compare any NBA players and how they stack up with the two player archetypes (defensive-oriented bigs who cut well for LeBron and offensive-skilled wings who can spot up and post up for Luka) in the interactive web app we built using Streamlit - <https://lakers-2025-team-fits.streamlit.app/>

### Memo Topics

-   Introduction

-   Methodology

-   Results - LeBron Lineups

-   Results - Luka Lineups

-   Recommended Targets

-   Contract & Acquisition Context

-   Caveats

### Introduction

**Objective**

This project evaluates which teammates historically correlate with strong on-court performance when paired with LeBron James or Luka Dončić. With a forward-looking lens, it aims to recommend realistic player acquisitions that could support a hypothetical Lakers team featuring both stars.

**Data Collection**

The dataset was created by scraping 10 years of NBA lineup and playtype data through the Synergy Sports API. Each lineup was merged with playtype percentile data for all players, then manually annotated with player positions.

**Modeling Approach**

Lineups were modeled using regression analysis with features formatted as Position_OffensiveOrDefensive_PlayType (e.g., "PF_Offensive_Cut", "SG_Defensive_Handoff"). This allowed the model to quantify the impact of specific positional skills on lineup net rating.

### Results - LeBron Lineups

**Top Correlating Skills for Lineup Success**

-   Defensive PRBallHandler

-   Defensive OffScreen

-   Defensive PRRollMan

-   Offensive Cut

**Interpretation**

Lineups featuring bigs who excel defensively-particularly in guarding ball handlers and covering screen actions-tended to yield high net ratings with LeBron. Additionally, bigs with high Offensive Cut percentiles complemented LeBron's drive-and-dish playmaking. Defensive PRBallHandler and Offensive Cut skills were especially critical given their high frequency in possessions.

### Results - Luka Lineups

**Top Correlating Skills for Lineup Success**

-   Offensive SpotUp

-   Offensive PostUp

-   Offensive OffScreen

-   Defensive Handoff

**Interpretation**

Lineups with wings who ranked highly in perimeter shooting (spot-ups) and secondary scoring options (post-ups, off-screen actions) performed best alongside Luka. Spot-up shooting stood out as the most impactful variable due to Luka's heliocentric offensive style that frequently draws help defense and creates catch-and-shoot opportunities.

### Recommended Targets

Based on the percentile rankings in 2024-2025 playtype data and positional filtering, the following players emerged as strong fits:

**Big Men for LeBron Archetype:**

-   **Dean Wade** - Defensive versatility and cutting ability at a low price point.

-   **Bobby Portis** - Strong positional defender with reliable offensive instincts.

-   **Mouhamed Gueye** - Switchable defender on a team-friendly contract.

-   **Trendon Watford** - Undersized big with some switchability and offensive creation.

![Image](https://github.com/user-attachments/assets/d198f258-2c73-450e-9603-ed012d8a975b)
![Image](https://github.com/user-attachments/assets/9a772986-8698-4bc4-9683-5b457f5e2d9e)

**Wings for Luka Archetype:**

-   **Khris Middleton** - Elite spot-up/post-up wing but likely expensive.

-   **Harrison Barnes** - Veteran shooter who can defend and post.

-   **Garrison Mathews** - Sharpshooter with low acquisition cost.

-   **Deni Avdija** - Dream target given youth, contract, and two-way versatility.

![Image](https://github.com/user-attachments/assets/830674e3-1b55-4dda-9f05-ea3265db0a35)

**Secondary/Realistic Targets (Wings):**

-   **De'Anthony Melton** - Defensive-minded guard who can space.

-   **Sam Hauser** - High-value shooter potentially available due to Celtics' cap issues.

-   **Malik Beasley** - Proven shooter, likely affordable.

-   **Grayson Allen** - Proven shooter with team control and availability.

![Image](https://github.com/user-attachments/assets/708e4f1b-b886-479c-b064-3d82fcacbd0b)
![Image](https://github.com/user-attachments/assets/1713080c-2a3c-40a0-a956-817d3b536f68)

### Contract & Acquisition Context

<table style="border-collapse: collapse; width: 100%; border: 2px solid black;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">Player</th>
      <th style="border: 1px solid black; padding: 8px;">Contract Status</th>
      <th style="border: 1px solid black; padding: 8px;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Dean Wade</td>
      <td style="border: 1px solid black; padding: 8px;">Expiring ($6.6M)</td>
      <td style="border: 1px solid black; padding: 8px;">Cheap and attainable</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Bobby Portis</td>
      <td style="border: 1px solid black; padding: 8px;">Player Option ($13M)</td>
      <td style="border: 1px solid black; padding: 8px;">Likely to opt in; moderate trade value</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Mouhamed Gueye</td>
      <td style="border: 1px solid black; padding: 8px;">Team Control (2 yrs, ~$2M)</td>
      <td style="border: 1px solid black; padding: 8px;">Developmental upside; low cost</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Trendon Watford</td>
      <td style="border: 1px solid black; padding: 8px;">UFA</td>
      <td style="border: 1px solid black; padding: 8px;">Unrestricted; value signing opportunity</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Khris Middleton</td>
      <td style="border: 1px solid black; padding: 8px;">Player Option ($34M)</td>
      <td style="border: 1px solid black; padding: 8px;">Likely to opt in; difficult acquisition</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Harrison Barnes</td>
      <td style="border: 1px solid black; padding: 8px;">Expiring ($18M)</td>
      <td style="border: 1px solid black; padding: 8px;">Expiring veteran; trade flexibility</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Garrison Mathews</td>
      <td style="border: 1px solid black; padding: 8px;">UFA</td>
      <td style="border: 1px solid black; padding: 8px;">Low-cost UFA</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Deni Avdija</td>
      <td style="border: 1px solid black; padding: 8px;">3 yrs control (~$14M → $12M)</td>
      <td style="border: 1px solid black; padding: 8px;">High value; requires significant trade capital</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">De’Anthony Melton</td>
      <td style="border: 1px solid black; padding: 8px;">UFA</td>
      <td style="border: 1px solid black; padding: 8px;">Targetable role player</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Sam Hauser</td>
      <td style="border: 1px solid black; padding: 8px;">3 yrs (~$11M/yr)</td>
      <td style="border: 1px solid black; padding: 8px;">May be available if Celtics shed salary</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Malik Beasley</td>
      <td style="border: 1px solid black; padding: 8px;">UFA</td>
      <td style="border: 1px solid black; padding: 8px;">Shooter with Lakers familiarity</td>
    </tr>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">Grayson Allen</td>
      <td style="border: 1px solid black; padding: 8px;">2 yrs + PO (~$18M/yr)</td>
      <td style="border: 1px solid black; padding: 8px;">Contract match required; price should be modest</td>
    </tr>
  </tbody>
</table>

### Caveats

**Positional Generalization:** While positions were manually labeled, some players (e.g., tweeners) may not fit neatly into one category, possibly skewing the regression's accuracy.

**One-Year Snapshot for Targeting:** Player percentile data was evaluated only for the 2024--2025 season. Longer-term consistency was not factored into recommendations.

**Acquisition Feasibility:** Some players (e.g., Deni Avdija, Sam Hauser) may only be available under specific cap or roster conditions.

**Overfitting:** There are potentially too many skills taken into account in the regression models, which could potentially lead to unimportant features being deemed significant.

**LeBron/Luka Teammate Relationship:** The model is based mostly on lineups where LeBron and Luka were not teammates, so targets may not be representative of who fits next to LeBron and Luka together.

### Contact & Additional Work

For questions or further discussion, feel free to reach out:

Email - [kevinkietle@gmail.com\
](mailto:kevinkietle@gmail.com)LinkedIn - [https://www.linkedin.com/in/kevinkietle/\
](https://www.linkedin.com/in/kevinkietle/)Website - <https://kevinkietle.github.io/Bootstrap-Website-Portfolio/>
