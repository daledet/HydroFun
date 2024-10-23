import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Big Dawg's Hydraulics")

st.write("### Input Data")
col1, col2, col3, col4 = st.columns(4)

hole_md = col1.number_input("Measured Depth ft.", format="%0.1f")
hole_tvd = col2.number_input("True Vertical Depth ft.", format="%0.1f")

casing_id = col1.number_input("Casing ID in.", format="%0.1f")
casing_shoe = col2.number_input("Casing Shoe ft.", format="%0.1f" )

drill_pipe_od = col1.number_input("Drill Pipe OD in.", format="%0.1f")
bha_od = col2.number_input("BHA OD in.", format="%0.1f")

open_hole_size = col1.number_input("Hole Diameter in.", format="%0.1f")
open_hole_depth = col2.number_input("Hole Depth ft.", format="%0.1f")

mud_weight = col1.number_input("Mud Weight ppg", format="%0.1f")

annular_friction_pressure = col2.number_input("AFP ppg", format="%0.1f")

# Calculations

bottom_hole_pressure = hole_tvd * mud_weight * 0.052
dynamic_bottom_hole_pressure = (hole_tvd * mud_weight * 0.052) + annular_friction_pressure
casing_volume = ((casing_id ** 2 - drill_pipe_od ** 2) / 1029.4) * casing_shoe
open_home_volume = ((open_hole_size ** 2 - bha_od ** 2) / 1029.4) * (open_hole_depth - casing_shoe)

hole_volume = casing_volume + open_home_volume

# Display

st.write("### Results")
col1, col2, col3 = st.columns(3)
col1.metric(label="Static Bottom Hole Pressure psi", value=f"{bottom_hole_pressure:,.1f} psi")
col2.metric(label="Dynamic Bottom Hole Pressure psi", value=f"{dynamic_bottom_hole_pressure:,.1f} psi")
col3.metric(label="Hole Volume bbls", value=f"{hole_volume:,.2f}")





