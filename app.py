import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="File Management System",
    page_icon="",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align:center;
    color:#1f77b4;
    font-size:40px;
    font-weight:bold;
}
.subtitle {
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">File Management System</p>',
            unsafe_allow_html=True)
st.markdown('<p class="subtitle">Create • Read • Update • Delete Files</p>',
            unsafe_allow_html=True)

# Sidebar
operation = st.sidebar.radio(
    "Choose Operation",
    ["Create File", "Read File", "Update File", "Delete File"]
)

# CREATE FILE
if operation == "Create File":
    st.subheader("Create New File")

    filename = st.text_input("File Name")
    content = st.text_area("Enter Content")

    if st.button("Create File"):
        path = Path(filename)

        if path.exists():
            st.error("File already exists.")
        else:
            with open(path, "w") as f:
                f.write(content)

            st.success("File created successfully!")

# READ FILE
elif operation == "Read File":
    st.subheader("Read File")

    filename = st.text_input("Enter File Name")

    if st.button("Read"):
        path = Path(filename)

        if path.exists():
            with open(path, "r") as f:
                data = f.read()

            st.success("File loaded successfully!")
            st.text_area("Content", data, height=300)

        else:
            st.error("File not found.")

# UPDATE FILE
elif operation == "Update File":
    st.subheader("Update File")

    filename = st.text_input("Enter File Name")

    update_option = st.selectbox(
        "Choose Update Type",
        ["Rename File", "Append Content", "Overwrite Content"]
    )

    path = Path(filename)

    if update_option == "Rename File":
        new_name = st.text_input("New File Name")

        if st.button("Rename"):
            if path.exists():
                path.rename(new_name)
                st.success("File renamed successfully!")
            else:
                st.error("File not found.")

    elif update_option == "Append Content":
        append_text = st.text_area("Content to Append")

        if st.button("Append"):
            if path.exists():
                with open(path, "a") as f:
                    f.write("\n" + append_text)

                st.success("Content appended successfully!")
            else:
                st.error("File not found.")

    elif update_option == "Overwrite Content":
        new_content = st.text_area("New Content")

        if st.button("Overwrite"):
            if path.exists():
                with open(path, "w") as f:
                    f.write(new_content)

                st.success("File overwritten successfully!")
            else:
                st.error("File not found.")

# DELETE FILE
elif operation == "Delete File":
    st.subheader(" Delete File")

    filename = st.text_input("Enter File Name")

    if st.button("Delete"):
        path = Path(filename)

        if path.exists():
            path.unlink()
            st.success("File deleted successfully!")
        else:
            st.error("File not found.")

# Footer
st.markdown("---")
st.markdown(
    "<center>Developed with Python & Streamlit</center>",
    unsafe_allow_html=True
)
