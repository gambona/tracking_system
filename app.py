import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Partner Tracker System",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="auto",
)

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
    "Contract ID": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50
    ],
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

def mostrar_intro():
    df_no_index = df.reset_index(drop=True)
    st.subheader("Tracking Partner Performance")
    st.text('Your text here')
   
def mostrar_partners():
    df_no_index = df.reset_index(drop=True)
    st.subheader("All Partners")
    st.table(df_no_index)
    
def mostrar_contract():
    st.subheader("Contracts")
    st.subheader("Update Contract")
    contract_to_update = st.number_input("Enter Contract ID to Update", min_value=1, step=1)
    new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"], key="update_status")


    if st.button("Update Contract Status"):
        # Check if the entered contract ID exists in the DataFrame
        if contract_to_update in df['Contract ID'].values:
            # Update the status of the contract
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

    # Pie chart 
   # st.subheader("Contracts Status Distribution")
    # status_counts = df['Status'].value_counts()

    # Create the pie chart using Matplotlib
    #fig, ax = plt.subplots()
    #ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=['blue'] * len(status_counts))
    #ax.axis('equal')  # Ensure pie is drawn as a circle

    # Display the pie chart in Streamlit
    #st.pyplot(fig)

def mostrar_deliverables():
    
    deliverables_data = {
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
            "Not Started", "Completed", "In Progress", "Not Started", "Completed"]
    }
    

    
    deliverables_df = pd.DataFrame(deliverables_data)
    deliverables_df['Deadline'] = pd.to_datetime(deliverables_df['Deadline'])  # Convert deadlines to datetime
    
    # Display the full dataframe initially
    st.subheader("Deliverables Overview")
    st.dataframe(deliverables_df)
    
    # Filter by Status
    st.subheader("Filter by Status")
    status_filter = st.selectbox("Select status to filter", ["All", "Not Started", "In Progress", "Completed"])
    if status_filter != "All":
        filtered_df = deliverables_df[deliverables_df['Status'] == status_filter]
        st.write(f"Deliverables with status **{status_filter}**:")
        st.dataframe(filtered_df)
    else:
        st.write("Showing all deliverables")
        st.dataframe(deliverables_df)
    
    # Filter by Owner
    st.subheader("Filter by Owner")
    owner_filter = st.selectbox("Select an owner to view their deliverables", ["All"] + list(deliverables_df['Owner'].unique()))
    if owner_filter != "All":
        filtered_df = deliverables_df[deliverables_df['Owner'] == owner_filter]
        st.write(f"Deliverables owned by **{owner_filter}**:")
        st.dataframe(filtered_df)
    else:
        st.write("Showing all deliverables")
        st.dataframe(deliverables_df)
    
    # Filter by Due Date
    st.subheader("Filter by Due Date")
    due_date_filter = st.date_input("Select a due date to view deliverables due on or before", value=pd.Timestamp('2024-09-30'))
    filtered_df = deliverables_df[deliverables_df['Deadline'] <= pd.to_datetime(due_date_filter)]
    st.write(f"Deliverables due on or before **{due_date_filter}**:")
    st.dataframe(filtered_df)

    
    
with st.sidebar:
    st.image("Eight_Sleep_logo.png")
    diapositiva = st.radio(
        "Index",
        ("Partners", "Contracts", "Deliverables"))

funciones_diapositivas = {
    "Partners": mostrar_partners,
    "Contracts": mostrar_contract,
    "Deliverables": mostrar_deliverables
}
funciones_diapositivas[diapositiva]()
