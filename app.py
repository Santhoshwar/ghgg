import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    return None

# Function to perform basic analysis (example: Gender Distribution)
def gender_analysis(data):
    if 'Gender' in data.columns:
        gender_count = data['Gender'].value_counts()
        st.write("Gender Distribution:")
        st.bar_chart(gender_count)
    else:
        st.warning("No 'Gender' column found in the dataset!")

# Function to create visualizations based on user choice
def create_visualization(data):
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select chart type", ("Gender Analysis", "Age vs Sales", "Category Distribution"))

    if chart_type == "Gender Analysis":
        gender_analysis(data)

    elif chart_type == "Age vs Sales" and 'Age' in data.columns and 'Sales' in data.columns:
        st.write("Age vs Sales Scatter Plot")
        sns.scatterplot(x='Age', y='Sales', data=data)
        st.pyplot()

    elif chart_type == "Category Distribution" and 'Category' in data.columns:
        category_count = data['Category'].value_counts()
        st.write("Category Distribution:")
        st.bar_chart(category_count)

    else:
        st.warning("The selected columns for the analysis are not present in the dataset!")

# Main function to control the flow
def main():
    st.title("Instant Data Visualizations Website")

    st.write("""
        Welcome! Upload your CSV dataset, and select the type of visualization you'd like to view.
    """)

    # Load dataset
    data = load_data()

    if data is not None:
        # Show first few rows of data
        st.write("Dataset Preview:")
        st.dataframe(data.head())

        # Create visualizations
        create_visualization(data)

if __name__ == "__main__":
    main()
