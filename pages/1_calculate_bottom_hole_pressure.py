import streamlit as st

import math

st.title("Calculate Bottom Hole Pressure")

st.write("### Input Data - Imperial")
col1, col2, col3, col4, col5 = st.columns(5)

pore_pressure = col1.number_input("Pore Pressure", format="%0.1f")
mud_density = col2.number_input("Mud Weight", format="%0.1f")
total_depth = col3.number_input("Total Depth", format="%0.1f")
shoe_depth = col4.number_input("Shoe Depth", format="%0.1f")
overbalance_required = col5.number_input("Overbalance Req", format="%0.1f")

#Calculations
# Bottom Hole
Ppp = 0.052 * total_depth * pore_pressure
Pover_balance = 0.052 * overbalance_required * total_depth
bhp_target = Ppp + Pover_balance
phyd = 0.052 * total_depth * mud_density
sbp = bhp_target - phyd

#Shoe

Ppp_shoe = 0.052 * shoe_depth * pore_pressure
Pover_balance_shoe = 0.052 * overbalance_required * shoe_depth
bhp_target_shoe = Ppp_shoe + Pover_balance_shoe
phyd_shoe = 0.052 * shoe_depth * mud_density
sbp_shoe = bhp_target_shoe - phyd_shoe


st.write("### Results")
col1, col2, col3 = st.columns(3)
col1.metric(label="Static Bottom Hole Pressure psi", value=f"{sbp:,.1f} psi")
col2.metric(label="Static Shoe Pressure psi", value=f"{sbp_shoe:,.1f} psi")

st.write("### Input Data - Metric")
col1, col2, col3, col4, col5 = st.columns(5)

pore_pressure_metric = col1.number_input("Pore Pressure Metric", format="%0.1f")
mud_density_metric = col2.number_input("Mud Weight Metric", format="%0.1f")
total_depth_metric = col3.number_input("Total Depth Metric", format="%0.1f")
shoe_depth_metric = col4.number_input("Shoe Depth Metric", format="%0.1f")
overbalance_required_metric = col5.number_input("Overbalance Req M", format="%0.1f")

#Calculations

Ppp_metric = 0.00981 * total_depth_metric * pore_pressure_metric
Pover_balance_metric = 0.00981 * overbalance_required_metric * total_depth_metric
bhp_target_metric = Ppp_metric + Pover_balance_metric
phyd_metric = 0.00981 * total_depth_metric * mud_density_metric
sbp_metric = bhp_target_metric - phyd_metric

Ppp_shoe_metric = 0.00981 * shoe_depth_metric * pore_pressure_metric
Pover_balance_shoe_metric = 0.00981 * overbalance_required * shoe_depth_metric
bhp_target_shoe_metric = Ppp_shoe_metric + Pover_balance_shoe_metric
phyd_shoe_metric = 0.00981 * shoe_depth_metric * mud_density_metric
sbp_shoe_metric = bhp_target_shoe_metric - phyd_shoe_metric

st.write("### Results")
col1, col2, col3 = st.columns(3)
col1.metric(label="Static Bottom Hole Pressure m", value=f"{sbp_metric:,.1f} kPa")
col2.metric(label="Static Bottom Hole Pressure m", value=f"{sbp_shoe_metric:,.1f} kPa")
