# Lakers-2025-Team-Fits

### Executive Summary

This analysis identifies optimal player targets for the Los Angeles Lakers to acquire in order to maximize lineup efficiency alongside LeBron James and Luka Dončić, assuming a scenario where both are on the same roster. Using ten years of lineup and playtype data sourced from the NBA and Synergy Sports APIs, the project models how specific player skills and positions have historically correlated with high net ratings when paired with either LeBron or Luka. The analysis recommends two key archetypes: defensive-oriented bigs who cut well for LeBron, and offensive-skilled wings who can spot up and post up for Luka. Top acquisition targets include Dean Wade, Mouhamed Gueye, Khris Middleton, and Harrison Barnes, with several alternative options identified based on contract flexibility and availability.

### Memo Topics

-   Introduction

-   Methodology

-   Results -- LeBron Lineups

-   Results -- Luka Lineups

-   Recommended Targets

-   Contract & Acquisition Context

-   Caveats

### Introduction

Objective

This project evaluates which teammates historically correlate with strong on-court performance when paired with LeBron James or Luka Dončić. With a forward-looking lens, it aims to recommend realistic player acquisitions that could support a hypothetical Lakers team featuring both stars.

Data Collection

The dataset was created by scraping 10 years of NBA lineup and playtype data through the Synergy Sports API. Each lineup was merged with playtype percentile data for all players, then manually annotated with player positions.

Modeling Approach

Lineups were modeled using regression analysis with features formatted as Position_OffensiveOrDefensive_PlayType (e.g., "PF_Offensive_Cut", "SG_Defensive_Handoff"). This allowed the model to quantify the impact of specific positional skills on lineup net rating.

### Results -- LeBron Lineups

Top Correlating Skills for Lineup Success

-   Defensive PRBallHandler

-   Defensive OffScreen

-   Defensive PRRollMan

-   Offensive Cut

Interpretation

Lineups featuring bigs who excel defensively---particularly in guarding ball handlers and covering screen actions---tended to yield high net ratings with LeBron. Additionally, bigs with high Offensive Cut percentiles complemented LeBron's drive-and-dish playmaking. Defensive PRBallHandler and Offensive Cut skills were especially critical given their high frequency in possessions.

### Results -- Luka Lineups

Top Correlating Skills for Lineup Success

-   Offensive SpotUp

-   Offensive PostUp

-   Offensive OffScreen

-   Defensive Handoff

Interpretation

Lineups with wings who ranked highly in perimeter shooting (spot-ups) and secondary scoring options (post-ups, off-screen actions) performed best alongside Luka. Spot-up shooting stood out as the most impactful variable due to Luka's heliocentric offensive style that frequently draws help defense and creates catch-and-shoot opportunities.

### Recommended Targets

Based on the percentile rankings in 2024--2025 playtype data and positional filtering, the following players emerged as strong fits:

Big Men for LeBron Archetype:

-   Dean Wade -- Defensive versatility and cutting ability at a low price point.

-   Bobby Portis -- Strong positional defender with reliable offensive instincts.

-   Mouhamed Gueye -- Switchable defender on a team-friendly contract.

-   Trendon Watford -- Undersized big with some switchability and offensive creation.

Wings for Luka Archetype:

-   Khris Middleton -- Elite spot-up/post-up wing but likely expensive.

-   Harrison Barnes -- Veteran shooter who can defend and post.

-   Garrison Mathews -- Sharpshooter with low acquisition cost.

-   Deni Avdija -- Dream target given youth, contract, and two-way versatility.

Secondary/Realistic Targets (Wings):

-   De'Anthony Melton -- Defensive-minded guard who can space.

-   Sam Hauser -- High-value shooter potentially available due to Celtics' cap issues.

-   Malik Beasley -- Proven shooter, likely affordable.

-   Grayson Allen -- Proven shooter with team control and availability.

### Contract & Acquisition Context

|

Player

 |

Contract Status

 |

Notes

 |
|

Dean Wade

 |

Expiring ($6.6M)

 |

Cheap and attainable

 |
|

Bobby Portis

 |

Player Option ($13M)

 |

Likely to opt in

 |
|

Mouhamed Gueye

 |

Team Control (2 yrs, ~$2M per)

 |

Developmental upside; low cost

 |
|

Trendon Watford

 |

UFA

 |

Value signing opportunity

 |
|

Khris Middleton

 |

Player Option ($34M)

 |

Likely to opt in; difficult acquisition

 |
|

Harrison Barnes

 |

Expiring ($18M)

 |

Expiring veteran; trade flexibility

 |
|

Garrison Mathews

 |

UFA

 |

Low-cost target

 |
|

Deni Avdija

 |

3 yrs control (~$14M → $12M)

 |

High value; requires significant trade capital

 |
|

De'Anthony Melton

 |

UFA

 |

Targetable player off injury

 |
|

Sam Hauser

 |

3 yrs (~$11M/yr)

 |

May be available if Celtics shed salary

 |
|

Malik Beasley

 |

UFA

 |

Shooter with Lakers familiarity

 |
|

Grayson Allen

 |

2 yrs + PO (~$18M/yr)

 |

Contract match required; Suns likely to sell

 |

### Caveats

Positional Generalization: While positions were manually labeled, some players (e.g., tweeners) may not fit neatly into one category, possibly skewing the regression's accuracy.

One-Year Snapshot for Targeting: Player percentile data was evaluated only for the 2024--2025 season. Longer-term consistency was not factored into recommendations.

Acquisition Feasibility: Some players (e.g., Deni Avdija, Sam Hauser) may only be available under specific cap or roster conditions.

Overfitting: There are potentially too many skills taken into account in the regression models, which could potentially lead to unimportant features being deemed significant.

LeBron/Luka Teammate Relationship: The model is based mostly on lineups where LeBron and Luka were not teammates, so targets may not be representative of who fits next to LeBron and Luka together.

### Contact & Additional Work

For questions or further discussion, feel free to reach out:

Email - [kevinkietle@gmail.com\
](mailto:kevinkietle@gmail.com)LinkedIn - [https://www.linkedin.com/in/kevinkietle/\
](https://www.linkedin.com/in/kevinkietle/)Website - <https://kevinkietle.github.io/Bootstrap-Website-Portfolio/>
