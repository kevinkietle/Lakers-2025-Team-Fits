import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Patch
import seaborn as sns
import streamlit as st
import os

player_percentiles = pd.read_csv('outputs/player_playtypes_percentiles_2015_2024.csv')
player_percentiles_2024 = player_percentiles[player_percentiles['SeasonYear'] == '2024-25']

playtype_data = pd.read_csv('outputs/playtype_data_2015_2024.csv')
# Group by PLAY_TYPE and TYPE_GROUPING, then sum the POSS column
playtype_summary = playtype_data.groupby(['PLAY_TYPE', 'TYPE_GROUPING'])['POSS'].sum().reset_index()
# Rename the summed column for clarity
playtype_summary.rename(columns={'POSS': 'Total_POSS'}, inplace=True)
playtype_summary['ATTR_NAME'] = playtype_summary['TYPE_GROUPING'] + '_' + playtype_summary['PLAY_TYPE']
top_play = playtype_summary['Total_POSS'].max()
playtype_summary['Frequency'] = (playtype_summary['Total_POSS'] / top_play) * 100

# Build a dictionary for quick lookup of global frequencies
frequency_map = dict(zip(playtype_summary['ATTR_NAME'], playtype_summary['Frequency']))

attributes_bigs = ['Defensive_PRBallHandler', 'Defensive_OffScreen', 'Defensive_PRRollMan', 'Offensive_Cut']
attributes_wings = ['Offensive_Postup', 'Offensive_Spotup', 'Offensive_OffScreen', 'Defensive_Handoff']
total_attributes = [attributes_bigs, attributes_wings]


st.title("Lakers Teammate Fit Explorer (LeBron/Luka Framework)")
st.write("This tool allows you to select any player in the NBA and see how they stack up in key attributes necessary to fit with LeBron and Luka.")
st.write("In my analysis, the archetype that fits with LeBron are bigs that excel in the following playtype attributes: Defensive PRBallHandler, Defensive OffScreen, Defensive PRRollMan, and Offensive Cut")
st.write("In my analysis, the archetype that fits with Luka are wings that excel in the following playtypes attributes: Offensive SpotUp, Offensive PostUp, Offensive OffScreen, and Defensive Handoff")

# Allow user to select players dynamically
player_options = player_percentiles_2024['PLAYER_NAME'].unique()
players_to_compare = st.multiselect("Select players to compare:", options=player_options)

# Let user choose the role group
role_group = st.radio("Select role type:", ["Bigs", "Wings"])
# Automatically select the corresponding attribute list
if role_group == "Bigs":
    attributes_to_compare = attributes_bigs
else:
    attributes_to_compare = attributes_wings


if players_to_compare and attributes_to_compare:
    skill_columns = attributes_to_compare 
    num_players = len(players_to_compare)
    
    fig, axs = plt.subplots(nrows=1, ncols=num_players, figsize=(6 * num_players, 6), squeeze=False)
    axs = axs[0]  # flatten to 1D for easier indexing

    for i, player in enumerate(players_to_compare):
        ax = axs[i]
        try:
            player_data = player_percentiles_2024[player_percentiles_2024['PLAYER_NAME'] == player].iloc[0]
            percentiles = [player_data[attr] * 100 for attr in skill_columns]
            player_freqs = [frequency_map.get(attr, 0) for attr in skill_columns]

            x = np.arange(len(skill_columns))
            bar_width = 0.35

            # Bar plot
            ax.bar(x - bar_width/2, percentiles, width=bar_width, color='lemonchiffon', label='Percentile')
            ax.bar(x + bar_width/2, player_freqs, width=bar_width, color='plum', label='Frequency')

            ax.set_xticks(x)
            ax.set_xticklabels([attr.replace('_', '\n') for attr in skill_columns], rotation=0, ha='center')
            ax.set_ylim(0, 100)
            ax.set_title(f"{player}", fontsize=16)
            ax.grid(True, linestyle='--', color='lightgray', alpha=0.7)

            # Remove plot borders
            for spine in ['top', 'right', 'left', 'bottom']:
                ax.spines[spine].set_visible(False)

            # Add legend only once
            if i == 0:
                legend_elements = [
                    Patch(facecolor='lemonchiffon', label='Percentile'),
                    Patch(facecolor='plum', label='Frequency')
                ]
                ax.legend(handles=legend_elements, loc='upper left')

            # Optional: Add player image (if exists)
            image_path = f'images/{player.lower().replace(" ", "_")}.png'
            if os.path.exists(image_path):
                try:
                    img = mpimg.imread(image_path)
                    img_ax = fig.add_axes([
                        ax.get_position().x1 - 0.07,
                        ax.get_position().y1 - 0.12,
                        0.1, 0.1
                    ])
                    img_ax.imshow(img)
                    img_ax.axis('off')
                except Exception as e:
                    print(f"Image error for {player}: {e}")

        except IndexError:
            print(f"No data found for {player}")
            ax.set_visible(False)

    fig.suptitle("Key Attribute Percentiles and Frequencies – Select Players", fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    st.pyplot(fig)

st.write("The bigs we identified as targets that excel in this framework are Dean Wade, Bobby Portis, Mouhamed Gueye, and Trendon Watford.")
st.write("The wings we identified as targets that excel in this framework are Khris Middleton, Harrison Barnes, Garrison Mathews, Deni Avdija. (Secondary: De’Anthony Melton, Sam Hauser, Malik Beasley, Grayson Allen)")