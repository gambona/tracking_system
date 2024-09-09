import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="8 Sleep Affiliates & Influencers Tracking System",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="auto",
)

data = {
    "Name": ["Peter Attia", "Doctor's Farmacy", "Doctor's Farmacy", "Shameless Mom Academy", "Chasing Excellence"],
    "Contract ID": [1, 2, 3, 4, 5],
    "Deliverable": ["YouTube Video", "Sponsored Content", "Instagram Post", "Podcast Promotion", "Blog Review"],
    "Owner": ["Bob", "David", "Charlie", "Bob", "David"],
    "Deadline": ["2025-03-01", "2025-03-01", "2024-10-24", "2025-01-24", "2024-10-13"],
    "Status": ["In Progress", "Not Started", "Completed", "Not Started", "Completed"],
    "Bank Details": ["***5678***", "***3456***", "***9876***", "***3456***", "***7890***"],
    "Last Payout": ["2024-07-11", "2024-06-21", "2024-04-14", "2024-03-16", "2024-08-27"]
}


df = pd.DataFrame(data)




def mostrar_partners():
    df_no_index = df.reset_index(drop=True)
    st.subheader("All Contracts")
    st.table(df_no_index)

def mostrar_contract ():

    st.subheader("Update Contract Status")
    contract_to_update = st.number_input("Enter Contract ID to Update", min_value=1, step=1)
    new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"], key="update_status")

    if st.button("Update Status"):
        df.loc[df['Contract ID'] == contract_to_update, 'Status'] = new_status
        df.to_csv(file_path, index=False)  # Save the updated status to the CSV
        st.success(f"Status for Contract ID {contract_to_update} updated!")

def mostrar_filters ():
    st.subheader("Filter by Partner or Status")
    partner_filter = st.selectbox("Select Partner", ["All"] + df["Name"].unique().tolist())
    status_filter = st.selectbox("Select Status", ["All", "Not Started", "In Progress", "Completed"])

    filtered_df = df
    if partner_filter != "All":
        filtered_df = filtered_df[filtered_df["Name"] == partner_filter]
    if status_filter != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status_filter]

    st.subheader("Filtered Contracts")
    st.dataframe(filtered_df)

def add_new_contact():
    st.subheader("Add a New Contract")
    partner = st.text_input("Partner Name")
    contract_id = st.number_input("Contract ID", min_value=1)
    deliverable = st.text_input("Deliverable")
    owner = st.text_input("Owner")
    deadline = st.date_input("Deadline")
    status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
    bank_details = st.text_input("Bank Details")
    last_payout = st.date_input("Last Payout")

    if st.button("Add Contract"):
        new_row = {
            "Name": partner, "Contract ID": contract_id, "Deliverable": deliverable,
            "Owner": owner, "Deadline": deadline.strftime("%Y-%m-%d"), "Status": status,
            "Bank Details": bank_details, "Last Payout": last_payout.strftime("%Y-%m-%d")
        }
        df = df.append(new_row, ignore_index=True)
        df.to_csv(file_path, index=False)  # Save new contract to the CSV
        st.success(f"Contract for {partner} added!")

def update_status():
    st.subheader("Update Contract Status")
    contract_to_update = st.number_input("Enter Contract ID to Update", min_value=1, step=1)
    new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"], key="update_status")

    if st.button("Update Status"):
        df.loc[df['Contract ID'] == contract_to_update, 'Status'] = new_status
        df.to_csv(file_path, index=False)  # Save the updated status to the CSV
        st.success(f"Status for Contract ID {contract_to_update} updated!")

with st.sidebar:
    diapositiva = st.radio(
        "Índice",
        ("Partners", "Update contract status", "Filters", "Add new contact", "Update Status"))

funciones_diapositivas = {
    "Partners": mostrar_partners,
    "Update contract status": mostrar_contract,
    "Filters": mostrar_filters,
    "Add new contact": add_new_contact,
    "Update Status": update_status

}
funciones_diapositivas[diapositiva]()
