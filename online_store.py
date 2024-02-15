import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page title and icon
st.set_page_config(page_title="Online Store Customer Data Analysis", page_icon=":bar_chart:", layout="wide")

# Load the dataset
def load_data():
    return pd.read_csv('online_store_customer_data.csv')

df = load_data()
st.sidebar.title("DASHBOARD FOR ONLINE STORE CUSTOMER")
st.title("Online Store Customer Data Analysis")
st.header("Data Visualizations")

st.markdown('---')


column1, column2 = st.columns(2)

# Visualization 1: Histogram of Age
with column1:
    
    st.subheader("HISTOGRAM OF AGE")
    st.markdown('---')
    age_range_visual1 = st.slider("Age Range", int(df['Age'].min()), int(df['Age'].max()), (20, 60))
    gender_filter_visual1 = st.selectbox("Gender", ["All"] + df['Gender'].unique().tolist())
    marital_status_filter_visual1 = st.multiselect("Marital Status", df['Marital_status'].unique())
    payment_method_filter_visual1 = st.multiselect("Payment Method", df['Payment_method'].unique())
    segment_filter_visual1 = st.multiselect("Segment", df['Segment'].unique())
    state_filter_visual1 = st.multiselect("State Names", df['State_names'].unique())
    employee_status_filter_visual1 = st.multiselect("Employee Status", df['Employees_status'].unique())
    filtered_data_visual1 = df[
    (df['Age'] >= age_range_visual1[0]) & (df['Age'] <= age_range_visual1[1]) &
    (df['Gender'].isin([gender_filter_visual1]) if gender_filter_visual1 != "All" else df['Gender'].notnull()) &
    (df['Marital_status'].isin(marital_status_filter_visual1) if marital_status_filter_visual1 else df['Marital_status'].notnull()) &
    (df['Payment_method'].isin(payment_method_filter_visual1) if payment_method_filter_visual1 else df['Payment_method'].notnull()) &
    (df['Segment'].isin(segment_filter_visual1) if segment_filter_visual1 else df['Segment'].notnull()) &
    (df['State_names'].isin(state_filter_visual1) if state_filter_visual1 else df['State_names'].notnull()) &
    (df['Employees_status'].isin(employee_status_filter_visual1) if employee_status_filter_visual1 else df['Employees_status'].notnull())
]
    st.markdown('---')
    fig, ax = plt.subplots()
    ax.hist(filtered_data_visual1['Age'], bins=20, color='lightblue', edgecolor='black')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Visualization 2: Count plot of Gender
with column2:

    st.subheader("COUNT PLOT OF GENDER")
    st.markdown('---')
    age_range_visual2 = st.slider("Age Range ", int(df['Age'].min()), int(df['Age'].max()), (20, 60))
    gender_filter_visual2 = st.selectbox("Gender ", ["All"] + df['Gender'].unique().tolist())
    marital_status_filter_visual2 = st.multiselect("Marital Status ", df['Marital_status'].unique())
    payment_method_filter_visual2 = st.multiselect("Payment Method ", df['Payment_method'].unique())
    segment_filter_visual2 = st.multiselect("Segment ", df['Segment'].unique())
    state_filter_visual2 = st.multiselect("State Names ", df['State_names'].unique())
    employee_status_filter_visual2 = st.multiselect("Employee Status ", df['Employees_status'].unique())

    filtered_data_visual2 = df[
    (df['Age'] >= age_range_visual2[0]) & (df['Age'] <= age_range_visual2[1]) &
    (df['Gender'].isin([gender_filter_visual2]) if gender_filter_visual2 != "All" else df['Gender'].notnull()) &
    (df['Marital_status'].isin(marital_status_filter_visual2) if marital_status_filter_visual2 else df['Marital_status'].notnull()) &
    (df['Payment_method'].isin(payment_method_filter_visual2) if payment_method_filter_visual2 else df['Payment_method'].notnull()) &
    (df['Segment'].isin(segment_filter_visual2) if segment_filter_visual2 else df['Segment'].notnull()) &
    (df['State_names'].isin(state_filter_visual2) if state_filter_visual2 else df['State_names'].notnull()) &
    (df['Employees_status'].isin(employee_status_filter_visual2) if employee_status_filter_visual2 else df['Employees_status'].notnull())
]
    st.markdown('---')
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data_visual2, x='Gender', palette='Blues')
    st.pyplot(fig)

# Visualization 3: Box plot of Amount Spent by Gender


with column1:
    
    st.subheader("Box plot of Amount Spent by Gender")  
    st.markdown('---')  
    age_range_visual3 = st.slider("Age Range (Visualization 3)", int(df['Age'].min()), int(df['Age'].max()), (20, 60))
    gender_filter_visual3 = st.selectbox("Gender (Visualization 3)", ["All"] + df['Gender'].unique().tolist())
    marital_status_filter_visual3 = st.multiselect("Marital Status (Visualization 3)", df['Marital_status'].unique())
    payment_method_filter_visual3 = st.multiselect("Payment Method (Visualization 3)", df['Payment_method'].unique())
    segment_filter_visual3 = st.multiselect("Segment (Visualization 3)", df['Segment'].unique())
    state_filter_visual3 = st.multiselect("State Names (Visualization 3)", df['State_names'].unique())
    employee_status_filter_visual3 = st.multiselect("Employee Status (Visualization 3)", df['Employees_status'].unique())

    filtered_data_visual3 = df[
    (df['Age'] >= age_range_visual3[0]) & (df['Age'] <= age_range_visual3[1]) &
    (df['Gender'].isin([gender_filter_visual3]) if gender_filter_visual3 != "All" else df['Gender'].notnull()) &
    (df['Marital_status'].isin(marital_status_filter_visual3) if marital_status_filter_visual3 else df['Marital_status'].notnull()) &
    (df['Payment_method'].isin(payment_method_filter_visual3) if payment_method_filter_visual3 else df['Payment_method'].notnull()) &
    (df['Segment'].isin(segment_filter_visual3) if segment_filter_visual3 else df['Segment'].notnull()) &
    (df['State_names'].isin(state_filter_visual3) if state_filter_visual3 else df['State_names'].notnull()) &
    (df['Employees_status'].isin(employee_status_filter_visual3) if employee_status_filter_visual3 else df['Employees_status'].notnull())
]
   
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_data_visual3, x='Gender', y='Amount_spent', palette='Blues')
    st.pyplot(fig)

# Visualization 4: Scatter plot of Age vs Amount Spent

with column2:
    
    st.subheader("Scatter plot of Age vs Amount Spent") 
    st.markdown('---')
    age_range_visual4 = st.slider("Age Range (Visualization 4)", int(df['Age'].min()), int(df['Age'].max()), (20, 60))
    gender_filter_visual4 = st.selectbox("Gender (Visualization 4)", ["All"] + df['Gender'].unique().tolist())
    marital_status_filter_visual4 = st.multiselect("Marital Status (Visualization 4)", df['Marital_status'].unique())
    payment_method_filter_visual4 = st.multiselect("Payment Method (Visualization 4)", df['Payment_method'].unique())
    segment_filter_visual4 = st.multiselect("Segment (Visualization 4)", df['Segment'].unique())
    state_filter_visual4 = st.multiselect("State Names (Visualization 4)", df['State_names'].unique())
    employee_status_filter_visual4 = st.multiselect("Employee Status (Visualization 4)", df['Employees_status'].unique())

    filtered_data_visual4 = df[
    (df['Age'] >= age_range_visual4[0]) & (df['Age'] <= age_range_visual4[1]) &
    (df['Gender'].isin([gender_filter_visual4]) if gender_filter_visual4 != "All" else df['Gender'].notnull()) &
    (df['Marital_status'].isin(marital_status_filter_visual4) if marital_status_filter_visual4 else df['Marital_status'].notnull()) &
    (df['Payment_method'].isin(payment_method_filter_visual4) if payment_method_filter_visual4 else df['Payment_method'].notnull()) &
    (df['Segment'].isin(segment_filter_visual4) if segment_filter_visual4 else df['Segment'].notnull()) &
    (df['State_names'].isin(state_filter_visual4) if state_filter_visual4 else df['State_names'].notnull()) &
    (df['Employees_status'].isin(employee_status_filter_visual4) if employee_status_filter_visual4 else df['Employees_status'].notnull())
]
  

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=filtered_data_visual4, x='Age', y='Amount_spent', hue='Gender', palette='Blues')
    ax.set_xlabel('Age')
    ax.set_ylabel('Amount Spent')
    ax.legend(title='Gender')
    st.pyplot(fig)


# Visualization 5: Bar plot of Average Amount Spent by Segment
with column1:

  
    st.subheader("Bar plot of Average Amount Spent by Segment")
    st.markdown('---')
    segment_filter_visual5 = st.multiselect("Segment (Visualization 5)", df['Segment'].unique())
    filtered_data_visual5 = df[
        (df['Segment'].isin(segment_filter_visual5) if segment_filter_visual5 else df['Segment'].notnull())
    ]
    st.markdown('---')
    segment_avg_amount = filtered_data_visual5.groupby('Segment')['Amount_spent'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=segment_avg_amount, x='Segment', y='Amount_spent', palette='Blues')
    ax.set_xlabel('Segment')
    ax.set_ylabel('Average Amount Spent')
    st.pyplot(fig)


# Visualization 6: Pie chart of Payment Method Distribution
with column2:
  
    
    st.subheader("Pie chart of Payment Method Distribution")
    st.markdown('---')
    payment_method_filter_visual6 = st.multiselect("Payment Method (Visualization 6)", df['Payment_method'].unique())
    filtered_data_visual6 = df[
        (df['Payment_method'].isin(payment_method_filter_visual6) if payment_method_filter_visual6 else df['Payment_method'].notnull())
    ]
    st.markdown('---')
    payment_method_counts = filtered_data_visual6['Payment_method'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(payment_method_counts, labels=payment_method_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Blues'))
    ax.axis('equal')
    st.pyplot(fig)


# Visualization 10: Line plot of Amount Spent over time
with column1:
    
    
    st.subheader("Box plot of Amount Spent by State")
    st.markdown('---')
    state_filter_visual7 = st.multiselect("State Names (Visualization 7)", df['State_names'].unique())
    filtered_data_visual7 = df[
        (df['State_names'].isin(state_filter_visual7) if state_filter_visual7 else df['State_names'].notnull())
    ]
    st.markdown('---')
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_data_visual7, x='State_names', y='Amount_spent', palette='Blues')
    ax.set_xlabel('State')
    ax.set_ylabel('Amount Spent')
    ax.tick_params(axis='x', rotation=90)
    st.pyplot(fig)

with column2:
  
  
    st.subheader("Line plot of Amount Spent over time")
    st.markdown('---')
    date_range_visual10 = st.slider("Date Range (Visualization 10)", df['Date'].min(), df['Date'].max(), (df['Date'].min(), df['Date'].max()))
    filtered_data_visual10 = df[
        (df['Date'] >= date_range_visual10[0]) & (df['Date'] <= date_range_visual10[1])
    ]
    st.markdown('---')
    fig, ax = plt.subplots()
    sns.lineplot(data=filtered_data_visual10, x='Date', y='Amount_spent', color='blue')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount Spent')
    st.pyplot(fig)