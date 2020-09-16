##--EDA for HR Data by Aymeric Steinitz 09/2020--**

#importing libraries
import pandas as pd
import plotly.express as px
import streamlit as st

#importing Data
df = pd.read_csv('../Human_Resources.csv')


# Header
st.title("Data exploration app - Human Resources Attrition data")

st.subheader("Raw Dataset")
st.write(df)
st.write(df.describe())

#Histograms
# For univariate distributions: histogram to better understand
st.header("Histogram")
#setting a box selection to select variable from the list of available columns
histogram_x = st.selectbox("Histogram variable", options=df.columns, index=df.columns.get_loc("Attrition"))
#setting a slider to configure the bin size
histogram_bins = st.slider(label="Histogram bins", min_value=5, max_value=50, value=25, step=1)
#sorting categorical data alphabetically
histogram_cats = df[histogram_x].sort_values().unique()
#plotting the histogram
histogram_fig = px.histogram(df, x=histogram_x, nbins=histogram_bins, title=f"Histogram for  {histogram_x} variable",
                        template="plotly_white", category_orders={histogram_x: histogram_cats})
st.write(histogram_fig)

#Boxplots
st.header("Boxplot")
st.subheader("With a categorical variable - JobRole, BusinessTravel, Department, Education Field ...")
# setting a select box to allow pick up of numerical variables
boxplot_x = st.selectbox("Boxplot variable", options=df.columns, index=df.columns.get_loc("Attrition"))
# list of categorical variables
cat_var = ['BusinessTravel', "Department", "EducationField","Gender", "JobRole","MaritalStatus"]
#setting a selection box to allow pick up of categorical variables
boxplot_cat = st.selectbox("Categorical variable", cat_var, 0)
#plottinh the boxplot
boxplot_fig = px.box(df, x=boxplot_cat, y=boxplot_x, title="Box plot of " + boxplot_x,
                        template="plotly_white")
st.write(boxplot_fig)

# min filter
st.header("Correlations")
# setting 2 select boxex to allow pick up of variables to be plotted on a scatter plot
correlation_x = st.selectbox("Correlation - X variable", options=df.columns, index=df.columns.get_loc("Attrition"))
correlation_y = st.selectbox("Correlation - Y variable", options=df.columns, index=df.columns.get_loc("MonthlyIncome"))
correlation_col = st.radio("Correlation - color variable", options=["Attrition", "Department", "Gender"], index=1)
#plot the scatter plot
fig = px.scatter(df, x=correlation_x, y=correlation_y, template="plotly_white", render_mode='webgl',
                 color=correlation_col, hover_data=['MonthlyIncome', 'Department', 'DistanceFromHome'], color_continuous_scale=px.colors.sequential.OrRd
                 )
fig.update_traces(mode="markers", marker={"line": {"width": 0.4, "color": "slategrey"}})
st.subheader("Filtered scatterplot and dataframe")
st.write(fig)
st.write(df)

# correlation heatmap
#setting a radio button to pick varialbe to include on the correlation heatmap
hmap_params = st.multiselect("Select parameters to include on heatmap", options=list(df.columns), default=[p for p in df.columns if "fg" in p])
#plot the heatmap
hmap_fig = px.imshow(df[hmap_params].corr())
st.write(hmap_fig)

