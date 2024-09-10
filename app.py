import streamlit as st
import pandas as pd
import numpy as np
import datetime
import smtplib
from email.mime.text import MIMEText
import matplotlib.pyplot as plt
from matplotlib import dates as mdates

# Set page configuration
st.set_page_config(
    page_title="Tracking Partner Performance",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="auto",
)

# Sample Data
data = {
    "Name": [
        "Peter Attia", "Doctor's Farmacy", "Doctor's Farmacy", "Shameless Mom Academy", "Chasing Excellence", 
        "Jay Shetty", "Morning Brew", "Tom O'Bryan", "The Model Health Show", "The Keto Diet Podcast", 
        "Shameless Mom Academy", "The Art of Charm", "Gretchen Rubin", "Peter Attia", "Dr. Will Cole", 
        "Doctor's Farmacy", "Matt D'Avella", "Brendon Burchard", "The Tim Ferriss Show", "The Life Coach School", 
        "The Model Health Show", "Bulletproof Radio", "Lewis Howes", "Impact Theory", "Chasing Excellence", 
        "Whoop Team", "Jillian Michaels", "Health Coach Radio", "Hannah Bronfman", "The Model Health Show", 
        "Matt D'Avella", "Gabby Bernstein", "Tom O'Bryan", "Shawn Stevenson", "Ali Abdaal", 
        "Morning Brew", "The Tim Ferriss Show", "Jillian Michaels", "Brendon Burchard", "Shameless Mom Academy", 
        "Eric Thomas", "The Life Coach School", "Gary Vee", "Hannah Bronfman", "Peter Attia", 
        "The Life Coach School", "The Skinny Confidential", "Tony Robbins", "The Art of Charm", "The Skinny Confidential"
    ],
    "Contract ID": list(range(1, 51)),
    "Deliverables": [
        "YouTube Video", "Sponsored Content", "Instagram Post", "Podcast Promotion", "Blog Review", 
        "Sponsored Content", "Sponsored Content", "YouTube Video", "Instagram Post", "Instagram Post", 
        "Sponsored Content", "Blog Review", "Instagram Post", "Podcast Promotion", "YouTube Video", 
        "YouTube Video", "Instagram Post", "Blog Review", "YouTube Video", "Podcast Promotion", 
        "Blog Review", "Podcast Promotion", "Podcast Promotion", "Instagram Post", "Sponsored Content", 
        "Podcast Promotion", "YouTube Video", "Podcast Promotion", "Instagram Post", "Sponsored Content", 
        "YouTube Video", "Podcast Promotion", "Sponsored Content", "Instagram Post", "Sponsored Content", 
        "Podcast Promotion", "Instagram Post", "Blog Review", "Instagram Post", "Sponsored Content", 
        "Instagram Post", "Podcast Promotion", "Blog Review", "YouTube Video", "YouTube Video", 
        "Instagram Post", "Sponsored Content", "YouTube Video", "Instagram Post", "Instagram Post"
    ],
    "Owner": [
        "Bob", "David", "Charlie", "Bob", "David", 
        "Alice", "Emma", "Charlie", "Bob", "David", 
        "Charlie", "Emma", "David", "Charlie", "Bob", 
        "Alice", "David", "Emma", "Charlie", "Bob", 
        "David", "Emma", "Bob", "David", "Charlie", 
        "Bob", "Emma", "Charlie", "David", "Alice", 
        "Bob", "Emma", "David", "Alice", "Charlie", 
        "David", "Bob", "Emma", "Charlie", "David", 
        "Bob", "Emma", "Alice", "David", "Charlie", 
        "Emma", "Bob", "David", "Alice", "Charlie"
    ],
    "Deadline": [
        "2025-03-01", "2025-03-01", "2024-10-24", "2025-01-24", "2024-10-13", 
        "2025-02-10", "2025-01-05", "2024-11-23", "2024-12-29", "2025-03-12", 
        "2025-01-07", "2025-02-15", "2024-10-28", "2025-03-02", "2025-03-04", 
        "2024-12-01", "2025-01-15", "2024-11-10", "2025-03-11", "2025-01-06", 
        "2024-11-29", "2025-02-25", "2025-03-01", "2024-10-19", "2025-02-05", 
        "2025-01-03", "2024-12-15", "2025-03-12", "2024-10-18", "2025-01-20", 
        "2025-02-02", "2024-11-17", "2025-02-19", "2024-10-20", "2025-03-05", 
        "2025-01-22", "2024-12-28", "2025-02-12", "2024-10-14", "2025-02-28", 
        "2025-03-06", "2024-12-03", "2025-01-21", "2025-02-11", "2024-10-29", 
        "2025-03-15", "2024-12-10", "2024-11-22", "2024-10-15", "2025-02-07"
    ],
    "Status": [
        "In Progress", "Not Started", "Completed", "Not Started", "Completed", 
        "Not Started", "Not Started", "In Progress", "Not Started", "Completed", 
        "In Progress", "Completed", "Completed", "Not Started", "Completed", 
        "Not Started", "Completed", "In Progress", "In Progress", "In Progress", 
        "In Progress", "Completed", "Not Started", "Completed", "Not Started", 
        "Completed", "In Progress", "Not Started", "In Progress", "In Progress", 
        "Completed", "In Progress", "Completed", "Completed", "In Progress", 
        "Not Started", "In Progress", "Not Started", "Completed", "Not Started", 
        "Completed", "In Progress", "Not Started", "Completed", "In Progress", 
        "Not Started", "Completed", "In Progress", "Not Started", "Completed"
    ],
    "Bank Details": [
        "***5678***", "***3456***", "***9876***", "***3456***", "***7890***", 
        "***9876***", "***5678***", "***3456***", "***7890***", "***1234***", 
        "***3456***", "***9876***", "***9876***", "***9876***", "***7890***", 
        "***3456***", "***3456***", "***5678***", "***1234***", "***9876***", 
        "***3456***", "***9876***", "***6543***", "***1234***", "***7890***", 
        "***5678***", "***9876***", "***6543***", "***6543***", "***9876***", 
        "***7890***", "***3456***", "***7890***", "***7890***", "***7890***", 
        "***3456***", "***9876***", "***1234***", "***6543***", "***5678***", 
        "***6543***", "***5678***", "***9876***", "***1234***", "***7890***", 
        "***5678***", "***5678***", "***7890***", "***1234***", "***7890***"
    ]
}

df = pd.DataFrame(data)
df['Deadline'] = pd.to_datetime(df['Deadline'])

# Function to send emails
def send_email(to, subject, body):
    # Please replace these with your actual email credentials
    EMAIL_ADDRESS = st.secrets["EMAIL_ADDRESS"]
    EMAIL_PASSWORD = st.secrets["EMAIL_PASSWORD"]

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email to {to}: {e}")
        return False

# Function to check deadlines and send reminders
def check_and_send_reminders(df):
    today = pd.Timestamp.today()
    upcoming = df[(df['Deadline'] >= today) & (df['Deadline'] <= today + pd.Timedelta(days=7))]
    overdue = df[df['Deadline'] < today]

    for _, row in upcoming.iterrows():
        subject = "Upcoming Deliverable Deadline"
        body = f"Hello {row['Owner']},\n\nThis is a reminder that your deliverable '{row['Deliverables']}' for contract ID {row['Contract ID']} is due on {row['Deadline'].date()}.\n\nPlease ensure it is completed on time.\n\nBest,\nTeam"
        send_email(row.get('Owner_email', 'owner@example.com'), subject, body)  # Replace with actual email

    for _, row in overdue.iterrows():
        subject = "Overdue Deliverable"
        body = f"Hello {row['Owner']},\n\nThe deliverable '{row['Deliverables']}' for contract ID {row['Contract ID']} was due on {row['Deadline'].date()} and is now overdue.\n\nPlease address this as soon as possible.\n\nBest,\nTeam"
        send_email(row.get('Owner_email', 'owner@example.com'), subject, body)  # Replace with actual email

# Function to highlight deadlines
def highlight_deadlines(row):
    today = pd.Timestamp.today()
    if row['Deadline'] < today:
        return ['background-color: red'] * len(row)
    elif row['Deadline'] < today + pd.Timedelta(days=7):
        return ['background-color: yellow'] * len(row)
    else:
        return [''] * len(row)

# Function to display summary metrics
def display_metrics(df):
    total = df.shape[0]
    completed = df[df['Status'] == "Completed"].shape[0]
    in_progress = df[df['Status'] == "In Progress"].shape[0]
    not_started = df[df['Status'] == "Not Started"].shape[0]
    overdue = df[df['Deadline'] < pd.Timestamp.today()].shape[0]

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Deliverables", total)
    col2.metric("Completed", completed)
    col3.metric("In Progress", in_progress)
    col4.metric("Not Started", not_started)
    col5.metric("Overdue", overdue)

# Function to visualize data
def visualize_data(df):
    st.subheader("Deliverables Status Distribution")
    status_counts = df['Status'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'orange', 'red'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    st.subheader("Deliverables by Owner")
    owner_counts = df['Owner'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(10,6))
    ax2.bar(owner_counts.index, owner_counts.values, color='skyblue')
    ax2.set_xlabel('Owner')
    ax2.set_ylabel('Number of Deliverables')
    ax2.set_title('Number of Deliverables per Owner')
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

# Function to display deliverables with conditional formatting
def display_deliverables(df):
    st.subheader("📦 Deliverables Overview")
    styled_df = df.copy()
    styled_df['Deadline'] = styled_df['Deadline'].dt.date

    # Apply conditional formatting
    styled = styled_df.style.apply(highlight_deadlines, axis=1)
    st.write("**Highlighted Deliverables**")
    st.dataframe(styled_df)  # Streamlit doesn't support styled dataframe directly

    # Alternative: Use colored text or emojis
    def deadline_status(deadline):
        today = pd.Timestamp.today()
        if deadline < today:
            return "🔴 " + deadline.strftime("%Y-%m-%d")
        elif deadline < today + pd.Timedelta(days=7):
            return "🟡 " + deadline.strftime("%Y-%m-%d")
        else:
            return "🟢 " + deadline.strftime("%Y-%m-%d")

    display_df = styled_df.copy()
    display_df['Deadline'] = display_df['Deadline'].apply(deadline_status)
    st.table(display_df)

# Function to filter and display contracts
def mostrar_contract(df):
    st.subheader("Contracts")
    st.subheader("Update Contract Status")
    contract_to_update = st.number_input("Enter Contract ID to Update", min_value=1, step=1, max_value=df['Contract ID'].max())
    new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"], key="update_status")

    if st.button("Update Contract Status"):
        if contract_to_update in df['Contract ID'].values:
            df.loc[df['Contract ID'] == contract_to_update, 'Status'] = new_status
            st.success(f"Contract ID {contract_to_update} updated to {new_status}")
        else:
            st.error(f"Contract ID {contract_to_update} not found")

    st.subheader("Filter Contracts by Status")
    status_filter = st.selectbox("Select Status to Filter", ["All", "Not Started", "In Progress", "Completed"], key="filter_status")

    if status_filter != "All":
        filtered_df = df[df['Status'] == status_filter]
    else:
        filtered_df = df

    st.write("Filtered Contracts:")
    st.dataframe(filtered_df)

    visualize_data(filtered_df)

# Function to display partners
def mostrar_partners(df):
    df_no_index = df.reset_index(drop=True)
    st.subheader("All Partners")
    st.table(df_no_index[['Name', 'Contract ID', 'Deliverables', 'Owner', 'Deadline', 'Status']])

# Function to display deliverables
def mostrar_deliverables(df):
    display_metrics(df)
    display_deliverables(df)

    st.subheader("Filter by Status")
    status_filter = st.selectbox("Select status to filter", ["All", "Not Started", "In Progress", "Completed"])
    if status_filter != "All":
        filtered_df = df[df['Status'] == status_filter]
        st.write(f"Deliverables with status **{status_filter}**:")
        st.dataframe(filtered_df)
    else:
        st.write("Showing all deliverables")
        st.dataframe(df)

    st.subheader("Filter by Owner")
    owner_filter = st.selectbox("Select an owner to view their deliverables", ["All"] + list(df['Owner'].unique()))
    if owner_filter != "All":
        filtered_df = df[df['Owner'] == owner_filter]
        st.write(f"Deliverables owned by **{owner_filter}**:")
        st.dataframe(filtered_df)
    else:
        st.write("Showing all deliverables")
        st.dataframe(df)

    st.subheader("Filter by Due Date")
    due_date_filter = st.date_input("Select a due date to view deliverables due on or before", value=datetime.date.today() + datetime.timedelta(days=30))
    filtered_df = df[df['Deadline'] <= pd.to_datetime(due_date_filter)]
    st.write(f"Deliverables due on or before **{due_date_filter}**:")
    st.dataframe(filtered_df)

    visualize_data(df)

# Sidebar with navigation
with st.sidebar:
    st.image("Eight_Sleep_logo.png", use_column_width=True)
    diapositiva = st.radio(
        "Index",
        ("Partners", "Contracts", "Deliverables"))

# Main content based on navigation
if 'Owner_email' not in df.columns:
    # Placeholder for owner emails
    df['Owner_email'] = 'owner@example.com'  # Replace with actual emails

funciones_diapositivas = {
    "Partners": lambda: mostrar_partners(df),
    "Contracts": lambda: mostrar_contract(df),
    "Deliverables": lambda: mostrar_deliverables(df)
}

funciones_diapositivas[diapositiva]()

# Button to send reminders
if st.button("Send Email Reminders"):
    check_and_send_reminders(df)
    st.success("Email reminders have been sent.")

